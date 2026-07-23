#!/usr/bin/env python3
"""
MARTHR Simulation Campaign Runner
Executes simulations with multiple seeds for statistical robustness
"""

import sys
import csv
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from marthr_simulator import MarthrSimulator, MarthrContext, MrhofSimulator


def run_simulation_campaign(scenario_name, scenario_func, num_seeds=20):
    """Run one scenario with multiple seeds and export aggregated results."""
    print(f"\n{'='*60}")
    print(f"🎯 Campaign: {scenario_name}")
    print(f"{'='*60}")
    
    output_dir = ROOT / "data" / "estimated" / "simulations"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    aggregated_logs = []
    
    for seed in range(num_seeds):
        print(f"\n  Seed {seed+1}/{num_seeds}...", end=" ", flush=True)
        
        try:
            sim = scenario_func(seed)
            
            # Add seed info to logs
            for log in sim.all_logs:
                log['seed'] = seed
                log['scenario'] = scenario_name
            
            aggregated_logs.extend(sim.all_logs)
            print(f"✅ {len(sim.all_logs)} metrics")
        except Exception as e:
            print(f"❌ {e}")
            import traceback
            traceback.print_exc()
            return None
    
    # Export aggregated results
    output_file = output_dir / f"campaign_{scenario_name}_aggregated.csv"
    with open(output_file, 'w', newline='') as f:
        fieldnames = ['scenario', 'seed', 'timestamp', 'node_id', 'parent', 'rank',
                     'trust', 'energy', 'qos_latency', 'mcs', 'hop_count',
                     'convergence_time', 'packet_loss_rate']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(aggregated_logs)
    
    print(f"\n  ✅ Exported {len(aggregated_logs)} total metrics to {output_file.name}")
    return output_file


# Scenario definitions - each returns a configured simulator with logs
def scenario_lossless(seed):
    """Lossless baseline: perfect links, no attacks, sufficient energy"""
    sim = MarthrSimulator(grid_size=5, seed=seed)
    sim.run_simulation(
        rounds=100,
        packet_loss_prob=0.0,
        safety=MarthrContext.SAFETY_NORMAL,
        threat=MarthrContext.THREAT_NORMAL
    )
    return sim


def scenario_lossy(seed):
    """Lossy network: 20% packet loss on all links"""
    sim = MarthrSimulator(grid_size=5, seed=seed)
    sim.run_simulation(
        rounds=100,
        packet_loss_prob=0.20,
        safety=MarthrContext.SAFETY_NORMAL,
        threat=MarthrContext.THREAT_NORMAL
    )
    return sim


def scenario_attack(seed):
    """High threat attack: selective forwarding from malicious nodes"""
    sim = MarthrSimulator(grid_size=5, seed=seed)
    
    # Mark nodes 3 and 5 as malicious - they forward only 30% of packets
    malicious_nodes = {3, 5}
    
    for round_num in range(100):
        # Malicious nodes degrade trust for their neighbors
        for node_id in sim.nodes.keys():
            if node_id in malicious_nodes:
                # Malicious node: pretend to have good links but actually drop packets
                neighbors = sim.get_neighbors(node_id)
                for neighbor_id, _ in neighbors:
                    # Malicious node reports false high link quality
                    sim.nodes[neighbor_id].trust_table.update_failure(node_id)
        
        # Normal simulation with high threat context
        sim.simulate_round(
            packet_loss_prob=0.05,  # Normal loss besides attacks
            safety=MarthrContext.SAFETY_CRITICAL,
            threat=MarthrContext.THREAT_HIGH
        )
        
        # Log metrics every 10 rounds
        if round_num % 10 == 0:
            for node_id in sim.nodes.keys():
                metrics = sim.nodes[node_id].log_metrics(sim.current_time)
                sim.all_logs.append(metrics)
    
    return sim


def scenario_energy(seed):
    """Energy stress: rapid battery depletion"""
    sim = MarthrSimulator(grid_size=5, seed=seed)
    
    for round_num in range(100):
        # Extra energy drain beyond normal transmission
        for node_id in sim.nodes.keys():
            if node_id != 1:  # Root has unlimited power
                extra_drain = 0.008 + random.random() * 0.007  # 0.8% to 1.5% per round
                sim.nodes[node_id].energy = max(0.0, sim.nodes[node_id].energy - extra_drain)
        
        # Normal simulation with energy-critical context
        sim.simulate_round(
            packet_loss_prob=0.02,
            safety=MarthrContext.SAFETY_NORMAL,
            threat=MarthrContext.THREAT_NORMAL
        )
        
        if round_num % 10 == 0:
            for node_id in sim.nodes.keys():
                metrics = sim.nodes[node_id].log_metrics(sim.current_time)
                sim.all_logs.append(metrics)
    
    return sim


def scenario_stress(seed):
    """Large grid stress: 8x8 = 64 nodes, more hops, higher load"""
    sim = MarthrSimulator(grid_size=8, seed=seed)
    sim.run_simulation(
        rounds=100,
        packet_loss_prob=0.05,
        safety=MarthrContext.SAFETY_NORMAL,
        threat=MarthrContext.THREAT_NORMAL
    )
    return sim


def scenario_mobility(seed):
    """Dynamic mobility: nodes move, links change frequently"""
    sim = MarthrSimulator(grid_size=6, seed=seed)
    
    for round_num in range(80):
        # Simulate mobility by randomly adjusting node positions slightly
        for node_id in sim.nodes.keys():
            if node_id != 1:  # Root stays fixed
                dx = random.gauss(0, 0.15)
                dy = random.gauss(0, 0.15)
                sim.nodes[node_id].x = max(0, min(sim.grid_size - 1, sim.nodes[node_id].x + dx))
                sim.nodes[node_id].y = max(0, min(sim.grid_size - 1, sim.nodes[node_id].y + dy))
        
        # Higher packet loss due to mobility
        sim.simulate_round(
            packet_loss_prob=0.10,
            safety=MarthrContext.SAFETY_NORMAL,
            threat=MarthrContext.THREAT_LOW
        )
        
        if round_num % 10 == 0:
            for node_id in sim.nodes.keys():
                metrics = sim.nodes[node_id].log_metrics(sim.current_time)
                sim.all_logs.append(metrics)
    
    return sim


def scenario_qos_sensitive(seed):
    """QoS-sensitive: low latency requirements, real-time traffic"""
    sim = MarthrSimulator(grid_size=4, seed=seed)
    
    for round_num in range(80):
        sim.simulate_round(
            packet_loss_prob=0.03,
            safety=MarthrContext.SAFETY_BEST_EFFORT,  # Prioritize QoS
            threat=MarthrContext.THREAT_LOW
        )
        
        if round_num % 10 == 0:
            for node_id in sim.nodes.keys():
                metrics = sim.nodes[node_id].log_metrics(sim.current_time)
                sim.all_logs.append(metrics)
    
    return sim


def scenario_mixed(seed):
    """Mixed attack + energy: simultaneous adversarial and resource constraints"""
    sim = MarthrSimulator(grid_size=6, seed=seed)
    
    malicious_nodes = {4, 8, 12}
    
    for round_num in range(80):
        # Energy depletion
        for node_id in sim.nodes.keys():
            if node_id != 1:
                sim.nodes[node_id].energy = max(0.0, sim.nodes[node_id].energy - 0.012)
        
        # Attack: malicious nodes degrade trust
        for node_id in sim.nodes.keys():
            if node_id in malicious_nodes:
                neighbors = sim.get_neighbors(node_id)
                for neighbor_id, _ in neighbors:
                    if random.random() < 0.4:  # 40% chance of triggering trust update
                        sim.nodes[neighbor_id].trust_table.update_failure(node_id)
        
        sim.simulate_round(
            packet_loss_prob=0.08,
            safety=MarthrContext.SAFETY_HIGH,
            threat=MarthrContext.THREAT_HIGH
        )
        
        if round_num % 10 == 0:
            for node_id in sim.nodes.keys():
                metrics = sim.nodes[node_id].log_metrics(sim.current_time)
                sim.all_logs.append(metrics)
    
    return sim


def mrhof_lossless(seed):
    """MRHOF baseline: lossless, ETX-only routing"""
    sim = MrhofSimulator(grid_size=5, seed=seed)
    sim.run_simulation(rounds=100, packet_loss_prob=0.0)
    return sim


def mrhof_lossy(seed):
    """MRHOF baseline: lossy, ETX-only routing"""
    sim = MrhofSimulator(grid_size=5, seed=seed)
    sim.run_simulation(rounds=100, packet_loss_prob=0.20)
    return sim


def mrhof_attack(seed):
    """MRHOF baseline: attack scenario, ETX-only routing"""
    sim = MrhofSimulator(grid_size=5, seed=seed)
    sim.run_simulation(rounds=100, packet_loss_prob=0.05)
    return sim


def main():
    print("\n🚀 MARTHR Simulation Campaign Launcher")
    print("="*60)
    
    campaigns = [
        ("lossless_baseline", scenario_lossless),
        ("lossy_network", scenario_lossy),
        ("attack_high_threat", scenario_attack),
        ("energy_stress", scenario_energy),
        ("stress_large_grid", scenario_stress),
        ("mobility_dynamic", scenario_mobility),
        ("qos_sensitive", scenario_qos_sensitive),
        ("mixed_attack_energy", scenario_mixed),
        ("mrhof_lossless", mrhof_lossless),
        ("mrhof_lossy", mrhof_lossy),
        ("mrhof_attack", mrhof_attack),
    ]
    
    results = []
    for scenario_name, scenario_func in campaigns:
        try:
            output_file = run_simulation_campaign(scenario_name, scenario_func, num_seeds=20)
            if output_file:
                results.append(output_file)
        except Exception as e:
            print(f"❌ Campaign {scenario_name} failed: {e}")
    
    print(f"\n{'='*60}")
    print(f"✅ Campaign Complete: {len(results)}/8 scenarios successful")
    print(f"{'='*60}\n")
    
    return results


if __name__ == "__main__":
    main()
