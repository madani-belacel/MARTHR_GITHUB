"""
MARTHR Network Simulator - Python Implementation
Lightweight simulation for validation before NS-3 integration
"""

import random
import math
from pathlib import Path


class MarthrContext:
    """Context-aware weight adaptation (ported from C)"""
    
    SAFETY_CRITICAL = 0
    SAFETY_HIGH = 1
    SAFETY_NORMAL = 2
    SAFETY_BEST_EFFORT = 3
    
    THREAT_HIGH = 0
    THREAT_NORMAL = 1
    THREAT_LOW = 2
    
    ENERGY_CRITICAL = 0
    ENERGY_NORMAL = 1
    ENERGY_SUFFICIENT = 2
    
    def __init__(self):
        pass
    
    def adapt_weights(self, safety, threat, energy):
        """Adapt weights based on context (matches C implementation exactly)"""
        # Safety-driven base weights (switch-case model from marthr_context.c)
        if safety == self.SAFETY_CRITICAL:
            alpha, beta, gamma = 0.60, 0.20, 0.20
        elif safety == self.SAFETY_HIGH:
            alpha, beta, gamma = 0.45, 0.30, 0.25
        elif safety == self.SAFETY_NORMAL:
            alpha, beta, gamma = 0.35, 0.40, 0.25
        else:  # SAFETY_BEST_EFFORT
            alpha, beta, gamma = 0.30, 0.50, 0.20
        
        # Threat-driven adjustments
        if threat == self.THREAT_HIGH:
            alpha += 0.05
            gamma += 0.03
        elif threat == self.THREAT_LOW:
            beta += 0.04
        
        # Energy-driven adjustments
        if energy == self.ENERGY_CRITICAL:
            beta += 0.08
            alpha -= 0.03
        elif energy == self.ENERGY_SUFFICIENT:
            beta -= 0.03
            gamma += 0.02
        
        # Renormalize if sum exceeds 1.0
        total = alpha + beta + gamma
        if total > 1.0 + 1e-5:
            alpha /= total
            beta /= total
            gamma /= total
        
        return alpha, beta, gamma


class MarthrTrustTable:
    """Trust table management (ported from C)"""
    
    MAX_ENTRIES = 64
    
    def __init__(self):
        self.entries = {}  # node_id -> {'trust_score': float, 'successes': int, 'failures': int}
    
    def update_success(self, node_id, link_quality):
        """Update trust on successful transmission"""
        if node_id not in self.entries:
            self.entries[node_id] = {'trust_score': 0.5, 'successes': 0, 'failures': 0}
        
        entry = self.entries[node_id]
        entry['successes'] += 1
        # Update: 70% of previous + 30% of new quality
        entry['trust_score'] = self._clamp(entry['trust_score'] * 0.7 + link_quality * 0.3)
    
    def update_failure(self, node_id):
        """Update trust on failed transmission"""
        if node_id not in self.entries:
            self.entries[node_id] = {'trust_score': 0.5, 'successes': 0, 'failures': 0}
        
        entry = self.entries[node_id]
        entry['failures'] += 1
        # Penalty: reduce by 15%
        entry['trust_score'] = self._clamp(entry['trust_score'] - 0.15)
    
    def get(self, node_id):
        """Get current trust value for node"""
        if node_id not in self.entries:
            return 0.5  # Unknown node: neutral trust
        return self.entries[node_id]['trust_score']
    
    def decay(self, node_id, decay_amount):
        """Apply trust decay"""
        if node_id not in self.entries:
            return
        self.entries[node_id]['trust_score'] = self._clamp(
            self.entries[node_id]['trust_score'] - decay_amount
        )
    
    @staticmethod
    def _clamp(value):
        """Clamp to [0.0, 1.0]"""
        return max(0.0, min(1.0, value))


class MarthrScore:
    """Multi-criteria score computation (ported from C)"""
    
    def __init__(self, context):
        self.context = context
    
    def compute_score(self, trust, energy, qos, safety, threat, energy_state):
        """Compute MCS = alpha*trust + beta*energy + gamma*qos"""
        alpha, beta, gamma = self.context.adapt_weights(safety, threat, energy_state)
        mcs = alpha * self._clamp(trust) + beta * self._clamp(energy) + gamma * self._clamp(qos)
        return self._clamp(mcs)
    
    @staticmethod
    def _clamp(value):
        return max(0.0, min(1.0, value))


class MarthrRank:
    """OCP/RPL rank computation (ported from C)"""
    
    def __init__(self):
        self.rank_scale = 1000.0  # Scale factor for rank computation
    
    def compute_rank(self, mcs, hop_count=1):
        """Compute routing rank from MCS and hop count.
        Lower rank = better (closer to root). MCS is inverted so higher MCS = lower rank."""
        # Invert MCS: higher MCS should give lower (better) rank
        inverted_mcs = 1.0 - self._clamp(mcs)
        # Add hop penalty: more hops = higher (worse) rank
        hop_penalty = hop_count * 0.1
        raw_rank = inverted_mcs + hop_penalty
        return self._clamp(raw_rank)
    
    def apply_hysteresis(self, candidate_rank, current_rank, hysteresis):
        """Apply hysteresis to avoid rank oscillation"""
        difference = candidate_rank - current_rank
        
        if difference >= hysteresis or difference <= -hysteresis:
            return candidate_rank
        
        return current_rank
    
    @staticmethod
    def is_better(rank_a, rank_b):
        return rank_a < rank_b
    
    @staticmethod
    def _clamp(value):
        return max(0.0, min(1.0, value))


class MRHOFBaseline:
    """Simplified MRHOF baseline using ETX-based rank computation.
    
    MRHOF selects the parent with the lowest ETX (Expected Transmission Count).
    This implementation estimates ETX from link quality and uses hop count as tiebreaker.
    No trust, no energy awareness, no context adaptation.
    """
    
    def __init__(self):
        self.rank_scale = 1000.0
    
    def compute_rank(self, etx, hop_count):
        """Compute rank = ETX + hop_count * 0.1 (MRHOF convention).
        Lower rank = better."""
        rank = etx + hop_count * 0.1
        return rank
    
    def estimate_etx(self, link_quality):
        """Estimate ETX from link quality. ETX = 1 / PRR (Packet Reception Ratio)."""
        prr = max(0.01, min(1.0, link_quality))
        etx = 1.0 / prr
        return etx


class MarthrNode:
    """Simulated network node with MARTHR routing"""
    
    def __init__(self, node_id, x, y):
        self.node_id = node_id
        self.x = x
        self.y = y
        self.energy = 1.0  # 100% initially
        self.parent = None
        self.rank = 1.0  # Start at 1.0 (worst) so any MCS > 0 gives better rank
        self.trust_table = MarthrTrustTable()
        self.context = MarthrContext()
        self.score_engine = MarthrScore(self.context)
        self.rank_engine = MarthrRank()
        self.metrics_log = []
        self.convergence_time = -1  # Round when parent first selected
        self.hop_count = 0
        self.last_mcs = 0.0
        self.last_qos = 0.0
        self.packet_loss_rate = 0.0  # Simulated PLR
    
    def get_energy_level(self):
        """Determine energy state"""
        if self.energy < 0.2:
            return MarthrContext.ENERGY_CRITICAL
        elif self.energy > 0.7:
            return MarthrContext.ENERGY_SUFFICIENT
        return MarthrContext.ENERGY_NORMAL
    
    def compute_qos(self, link_quality, distance, hop_count):
        """Compute QoS metric based on link quality, distance, and hop count.
        Returns value in [0,1] where higher is better (lower latency)."""
        # Base QoS from link quality (inverse of packet loss)
        qos_from_link = link_quality
        # Latency penalty from hop count (each hop adds ~5ms equivalent)
        hop_penalty = min(0.5, hop_count * 0.05)
        # Distance penalty (longer distance = higher propagation delay)
        dist_penalty = min(0.3, distance * 0.15)
        # Combine: higher link quality is better, penalties reduce QoS
        qos = max(0.0, min(1.0, qos_from_link - hop_penalty - dist_penalty))
        return round(qos, 4)
    
    def update_parent(self, candidate_parent_id, link_quality, distance=1.0,
                     safety=MarthrContext.SAFETY_NORMAL, 
                     threat=MarthrContext.THREAT_NORMAL,
                     current_round=0):
        """Update parent based on candidate"""
        trust = self.trust_table.get(candidate_parent_id)
        energy_state = self.get_energy_level()
        
        # Compute hop count through candidate parent
        parent_hop = 1
        if hasattr(self, '_sim') and hasattr(self._sim, 'nodes'):
            if candidate_parent_id in self._sim.nodes:
                parent_hop = self._sim.nodes[candidate_parent_id].hop_count
        candidate_hop = parent_hop + 1
        
        # Compute QoS based on network conditions
        qos = self.compute_qos(link_quality, distance, candidate_hop)
        
        # Compute score for candidate (use candidate parent's energy, not self)
        candidate_energy = 1.0
        if hasattr(self, '_sim') and hasattr(self._sim, 'nodes'):
            if candidate_parent_id in self._sim.nodes:
                candidate_energy = self._sim.nodes[candidate_parent_id].energy
        mcs = self.score_engine.compute_score(
            trust, candidate_energy, qos,
            safety, threat, energy_state
        )
        candidate_rank = self.rank_engine.compute_rank(mcs, candidate_hop)
        
        # Apply hysteresis (avoid oscillation)
        new_rank = self.rank_engine.apply_hysteresis(
            candidate_rank, self.rank, hysteresis=0.05
        )
        
        # Accept if better (lower rank = better, higher MCS = lower rank)
        if self.rank_engine.is_better(new_rank, self.rank):
            old_parent = self.parent
            self.parent = candidate_parent_id
            self.rank = new_rank
            self.hop_count = candidate_hop
            self.last_mcs = mcs
            self.last_qos = qos
            self.trust_table.update_success(candidate_parent_id, link_quality)
            if old_parent is None and self.convergence_time == 0:
                self.convergence_time = current_round
            return True
        elif candidate_parent_id == self.parent:
            # Re-selected same parent: update trust to reflect continued use
            self.trust_table.update_success(candidate_parent_id, link_quality)
            return True
        else:
            # Do NOT penalize trust for candidates not selected as parent.
            # Trust reflects actual transmission outcomes, not routing decisions.
            # Non-parent trust decay is handled in simulate_round().
            return False
    
    def log_metrics(self, timestamp):
        """Log current routing metrics"""
        parent_trust = self.trust_table.get(self.parent) if self.parent else 0.0
        return {
            'timestamp': timestamp,
            'node_id': self.node_id,
            'parent': self.parent if self.parent else 0,
            'rank': round(self.rank, 4),
            'trust': round(parent_trust, 4),
            'energy': round(self.energy, 4),
            'qos_latency': round(self.last_qos, 4) if self.last_qos > 0 else round(1.0 - self.last_mcs, 4),
            'mcs': round(self.last_mcs, 4),
            'hop_count': self.hop_count,
            'convergence_time': self.convergence_time,
            'packet_loss_rate': round(self.packet_loss_rate, 4)
        }


class MrhofNode:
    """Simulated network node with MRHOF (ETX-based) routing"""
    
    def __init__(self, node_id, x, y):
        self.node_id = node_id
        self.x = x
        self.y = y
        self.energy = 1.0
        self.parent = None
        self.rank = 1.0
        self.hop_count = 0
        self.last_mcs = 0.0
        self.last_qos = 0.0
        self.packet_loss_rate = 0.0
        self.convergence_time = 0
        self.mrhof = MRHOFBaseline()
        self.metrics_log = []
    
    def update_parent(self, candidate_parent_id, link_quality, distance=1.0, current_round=0):
        """Update parent based on MRHOF ETX metric"""
        etx = self.mrhof.estimate_etx(link_quality)
        
        parent_hop = 1
        if hasattr(self, '_sim') and hasattr(self._sim, 'nodes'):
            if candidate_parent_id in self._sim.nodes:
                parent_hop = self._sim.nodes[candidate_parent_id].hop_count
        candidate_hop = parent_hop + 1
        
        candidate_rank = self.mrhof.compute_rank(etx, candidate_hop)
        
        difference = candidate_rank - self.rank
        if abs(difference) < 0.05:
            new_rank = self.rank
        else:
            new_rank = candidate_rank
        
        if new_rank < self.rank:
            old_parent = self.parent
            self.parent = candidate_parent_id
            self.rank = new_rank
            self.hop_count = candidate_hop
            self.last_mcs = 1.0 - etx  # Proxy for comparison
            if old_parent is None and self.convergence_time == 0:
                self.convergence_time = current_round
            return True
        return False
    
    def log_metrics(self, timestamp):
        parent_trust = 0.0
        return {
            'timestamp': timestamp,
            'node_id': self.node_id,
            'parent': self.parent if self.parent else 0,
            'rank': round(self.rank, 4),
            'trust': round(parent_trust, 4),
            'energy': round(self.energy, 4),
            'qos_latency': round(self.last_qos, 4) if self.last_qos > 0 else round(1.0 - self.last_mcs, 4),
            'mcs': round(self.last_mcs, 4),
            'hop_count': self.hop_count,
            'convergence_time': self.convergence_time,
            'packet_loss_rate': round(self.packet_loss_rate, 4)
        }


class MrhofSimulator:
    """MRHOF baseline simulator (ETX-based, no trust, no energy, no context)"""
    
    def __init__(self, grid_size=5, seed=None):
        self.grid_size = grid_size
        self.nodes = {}
        self.current_time = 0.0
        self.all_logs = []
        self.seed = seed
        if seed is not None:
            random.seed(seed)
        self._init_grid()
        self._link_sim_to_nodes()
    
    def _init_grid(self):
        node_id = 1
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                self.nodes[node_id] = MrhofNode(node_id, x, y)
                node_id += 1
    
    def _link_sim_to_nodes(self):
        for node in self.nodes.values():
            node._sim = self
    
    def get_neighbors(self, node_id, max_distance=1.5):
        node = self.nodes[node_id]
        neighbors = []
        for other_id, other_node in self.nodes.items():
            if other_id == node_id:
                continue
            dist = ((node.x - other_node.x)**2 + (node.y - other_node.y)**2)**0.5
            if dist <= max_distance:
                neighbors.append((other_id, dist))
        return neighbors
    
    def compute_link_quality(self, distance, packet_loss_prob=0.0):
        base_quality = max(0.0, 1.0 - (distance / 2.0))
        if random.random() < packet_loss_prob:
            base_quality *= 0.3
        noise = random.gauss(0, 0.05)
        return max(0.0, min(1.0, base_quality + noise))
    
    def simulate_round(self, duration=1.0, packet_loss_prob=0.0):
        for node_id in sorted(self.nodes.keys()):
            if node_id == 1:
                self.nodes[node_id].parent = 0
                self.nodes[node_id].rank = 0.0
                self.nodes[node_id].hop_count = 0
                self.nodes[node_id].last_mcs = 1.0
                continue
            
            neighbors = self.get_neighbors(node_id)
            if not neighbors:
                continue
            
            for neighbor_id, distance in neighbors:
                link_quality = self.compute_link_quality(distance, packet_loss_prob)
                self.nodes[node_id].update_parent(
                    neighbor_id, link_quality, distance, self.current_time
                )
            
            if self.nodes[node_id].parent:
                decay = 0.005 + random.random() * 0.01
                self.nodes[node_id].energy = max(0.0, self.nodes[node_id].energy - decay)
                self.nodes[node_id].packet_loss_rate = (
                    self.nodes[node_id].packet_loss_rate * 0.9 + packet_loss_prob * 0.1
                )
        
        self.current_time += duration
    
    def run_simulation(self, rounds=100, packet_loss_prob=0.0):
        for round_num in range(rounds):
            self.simulate_round(packet_loss_prob=packet_loss_prob)
            if round_num % 10 == 0:
                for node_id in self.nodes.keys():
                    metrics = self.nodes[node_id].log_metrics(self.current_time)
                    self.all_logs.append(metrics)
    
    def export_csv(self, filename):
        import csv
        with open(filename, 'w', newline='') as f:
            fieldnames = ['timestamp', 'node_id', 'parent', 'rank', 'trust',
                         'energy', 'qos_latency', 'mcs', 'hop_count',
                         'convergence_time', 'packet_loss_rate']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.all_logs)
    
    def print_summary(self):
        print("\n=== MRHOF Baseline Summary ===")
        print(f"Grid size: {self.grid_size}x{self.grid_size} ({len(self.nodes)} nodes)")
        if self.all_logs:
            ranks = [log['rank'] for log in self.all_logs if log['node_id'] != 1]
            if ranks:
                print(f"  Mean Rank: {sum(ranks)/len(ranks):.4f}")


class MarthrSimulator:
    """MARTHR network simulator"""
    
    def __init__(self, grid_size=5, seed=None):
        self.grid_size = grid_size
        self.nodes = {}
        self.current_time = 0.0
        self.all_logs = []
        self.seed = seed
        if seed is not None:
            random.seed(seed)
        self._init_grid()
        self._link_sim_to_nodes()
    
    def _init_grid(self):
        """Initialize grid topology"""
        node_id = 1
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                self.nodes[node_id] = MarthrNode(node_id, x, y)
                node_id += 1
    
    def _link_sim_to_nodes(self):
        """Give nodes reference to simulator for hop count computation"""
        for node in self.nodes.values():
            node._sim = self
    
    def get_neighbors(self, node_id, max_distance=1.5):
        """Get nodes within communication range"""
        node = self.nodes[node_id]
        neighbors = []
        for other_id, other_node in self.nodes.items():
            if other_id == node_id:
                continue
            dist = ((node.x - other_node.x)**2 + (node.y - other_node.y)**2)**0.5
            if dist <= max_distance:
                neighbors.append((other_id, dist))
        return neighbors
    
    def compute_link_quality(self, distance, packet_loss_prob=0.0):
        """Compute link quality based on distance and packet loss probability.
        Returns value in [0,1] where higher is better."""
        # Base quality from distance (closer = better signal)
        base_quality = max(0.0, 1.0 - (distance / 2.0))
        # Apply packet loss (simulates unreliable links)
        if random.random() < packet_loss_prob:
            base_quality *= 0.3  # Significant degradation on lost packets
        # Add some noise to make it realistic
        noise = random.gauss(0, 0.05)
        return max(0.0, min(1.0, base_quality + noise))
    
    def simulate_round(self, duration=1.0, packet_loss_prob=0.0,
                      safety=MarthrContext.SAFETY_NORMAL,
                      threat=MarthrContext.THREAT_NORMAL):
        """Simulate one routing round"""
        for node_id in sorted(self.nodes.keys()):
            if node_id == 1:  # Root node
                self.nodes[node_id].parent = 0
                self.nodes[node_id].rank = 0.0
                self.nodes[node_id].hop_count = 0
                self.nodes[node_id].last_mcs = 1.0
                continue
            
            neighbors = self.get_neighbors(node_id)
            if not neighbors:
                continue
            
            # Try each neighbor, pick best
            best_neighbor = None
            for neighbor_id, distance in neighbors:
                # Link quality with noise and packet loss
                link_quality = self.compute_link_quality(distance, packet_loss_prob)
                
                # Try to update parent
                if self.nodes[node_id].update_parent(
                    neighbor_id, link_quality, distance,
                    safety, threat, self.current_time
                ):
                    best_neighbor = neighbor_id
            
            # Energy decay (simulate transmission cost)
            # Higher packet loss requires more retransmissions, increasing energy drain
            if best_neighbor:
                base_decay = 0.005 + random.random() * 0.01  # 0.5% to 1.5%
                retransmission_penalty = packet_loss_prob * 0.008  # extra drain from retransmissions
                decay = base_decay + retransmission_penalty
                self.nodes[node_id].energy = max(0.0, self.nodes[node_id].energy - decay)
                # Simulate packet loss tracking
                self.nodes[node_id].packet_loss_rate = (
                    self.nodes[node_id].packet_loss_rate * 0.9 + packet_loss_prob * 0.1
                )
            
            # Apply trust decay for non-parent entries
            for other_id in list(self.nodes[node_id].trust_table.entries.keys()):
                if other_id != self.nodes[node_id].parent:
                    self.nodes[node_id].trust_table.decay(other_id, 0.002)
        
        self.current_time += duration
    
    def run_simulation(self, rounds=100, packet_loss_prob=0.0,
                      safety=MarthrContext.SAFETY_NORMAL,
                      threat=MarthrContext.THREAT_NORMAL):
        """Run full simulation"""
        for round_num in range(rounds):
            self.simulate_round(
                packet_loss_prob=packet_loss_prob,
                safety=safety,
                threat=threat
            )
            
            # Log metrics every 10 rounds
            if round_num % 10 == 0:
                for node_id in self.nodes.keys():
                    metrics = self.nodes[node_id].log_metrics(self.current_time)
                    self.all_logs.append(metrics)
    
    def export_csv(self, filename):
        """Export metrics to CSV"""
        import csv
        with open(filename, 'w', newline='') as f:
            fieldnames = ['timestamp', 'node_id', 'parent', 'rank', 'trust',
                         'energy', 'qos_latency', 'mcs', 'hop_count',
                         'convergence_time', 'packet_loss_rate']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.all_logs)
        print(f"✅ Exported {len(self.all_logs)} metrics to {filename}")
    
    def print_summary(self):
        """Print simulation summary"""
        print("\n=== MARTHR Simulation Summary ===")
        print(f"Grid size: {self.grid_size}x{self.grid_size} ({len(self.nodes)} nodes)")
        print(f"Simulation time: {self.current_time} seconds")
        print(f"Total logs: {len(self.all_logs)}")
        
        if self.all_logs:
            ranks = [log['rank'] for log in self.all_logs if log['node_id'] != 1]
            trusts = [log['trust'] for log in self.all_logs if log['node_id'] != 1]
            energies = [log['energy'] for log in self.all_logs if log['node_id'] != 1]
            mcs_vals = [log['mcs'] for log in self.all_logs if log['node_id'] != 1]
            qos_vals = [log['qos_latency'] for log in self.all_logs if log['node_id'] != 1]
            
            if ranks:
                print(f"\nMetrics (mean, excl. root):")
                print(f"  Rank: {sum(ranks)/len(ranks):.4f}")
                print(f"  Trust: {sum(trusts)/len(trusts):.4f}")
                print(f"  Energy: {sum(energies)/len(energies):.4f}")
                print(f"  MCS: {sum(mcs_vals)/len(mcs_vals):.4f}")
                print(f"  QoS Latency: {sum(qos_vals)/len(qos_vals):.4f}")


if __name__ == "__main__":
    ROOT = Path(__file__).resolve().parents[1]
    print("🚀 Starting MARTHR Simulator...")
    sim = MarthrSimulator(grid_size=5)
    sim.run_simulation(rounds=100)
    sim.print_summary()
    sim.export_csv(str(ROOT / "data" / "raw" / "marthr_simulation_trace.csv"))
