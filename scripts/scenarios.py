"""
MARTHR Simulation Scenarios
Generates diverse simulation traces for validation
"""

import os
import sys
import random
from pathlib import Path
from marthr_simulator import MarthrSimulator, MarthrContext


def scenario_lossless_baseline(output_dir):
    """Scenario 1: Lossless baseline (perfect links)"""
    print("📊 Running: Lossless Baseline")
    sim = MarthrSimulator(grid_size=5)
    
    # Perfect conditions
    sim.run_simulation(rounds=100)
    
    output_file = os.path.join(output_dir, "scenario_lossless_baseline.csv")
    sim.export_csv(output_file)
    sim.print_summary()
    return output_file


def scenario_lossy_network(output_dir, loss_rate=0.2):
    """Scenario 2: Lossy network (packet loss)"""
    print(f"📊 Running: Lossy Network (loss={loss_rate})")
    sim = MarthrSimulator(grid_size=5)
    
    for round_num in range(100):
        sim.simulate_round(packet_loss_prob=loss_rate)
    
    output_file = os.path.join(output_dir, "scenario_lossy_network.csv")
    sim.export_csv(output_file)
    sim.print_summary()
    return output_file


def scenario_attack_high_threat(output_dir):
    """Scenario 3: High threat (malicious nodes)"""
    print("📊 Running: High Threat Attack Scenario")
    sim = MarthrSimulator(grid_size=5)
    
    for round_num in range(100):
        sim.simulate_round(safety=MarthrContext.SAFETY_CRITICAL,
                          threat=MarthrContext.THREAT_HIGH)
    
    output_file = os.path.join(output_dir, "scenario_attack_high_threat.csv")
    sim.export_csv(output_file)
    sim.print_summary()
    return output_file


def scenario_energy_stress(output_dir):
    """Scenario 4: Energy-stressed network"""
    print("📊 Running: Energy Stress Scenario")
    sim = MarthrSimulator(grid_size=5)
    
    for round_num in range(100):
        sim.simulate_round()
        # Extra energy drain for stress scenario
        for node_id in sim.nodes:
            if node_id != 1:
                sim.nodes[node_id].energy = max(0.0, sim.nodes[node_id].energy - 0.01)
    
    output_file = os.path.join(output_dir, "scenario_energy_stress.csv")
    sim.export_csv(output_file)
    sim.print_summary()
    return output_file


def scenario_context_switching(output_dir):
    """Scenario 5: Dynamic context switches"""
    print("📊 Running: Context Switching Scenario")
    sim = MarthrSimulator(grid_size=5)
    
    contexts = [
        (MarthrContext.SAFETY_NORMAL, MarthrContext.THREAT_NORMAL),
        (MarthrContext.SAFETY_CRITICAL, MarthrContext.THREAT_HIGH),
        (MarthrContext.SAFETY_BEST_EFFORT, MarthrContext.THREAT_LOW),
    ]
    
    for round_num in range(100):
        context_idx = (round_num // 33) % len(contexts)
        safety, threat = contexts[context_idx]
        sim.simulate_round(safety=safety, threat=threat)
    
    output_file = os.path.join(output_dir, "scenario_context_switching.csv")
    sim.export_csv(output_file)
    sim.print_summary()
    return output_file


def scenario_mixed_conditions(output_dir):
    """Scenario 6: Mixed realistic conditions"""
    print("📊 Running: Mixed Realistic Conditions")
    sim = MarthrSimulator(grid_size=5)
    
    for round_num in range(100):
        loss_rate = 0.1 + 0.1 * (round_num / 100.0)
        safety = MarthrContext.SAFETY_HIGH if round_num < 50 else MarthrContext.SAFETY_NORMAL
        threat = MarthrContext.THREAT_NORMAL
        sim.simulate_round(packet_loss_prob=loss_rate, safety=safety, threat=threat)
    
    output_file = os.path.join(output_dir, "scenario_mixed_conditions.csv")
    sim.export_csv(output_file)
    sim.print_summary()
    return output_file


ROOT = Path(__file__).resolve().parents[1]

def run_all_scenarios(output_dir=None):
    """Run all scenarios and aggregate results"""
    output_dir = Path(output_dir) if output_dir else ROOT / "data" / "estimated" / "simulations"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    scenarios = [
        scenario_lossless_baseline,
        scenario_lossy_network,
        scenario_attack_high_threat,
        scenario_energy_stress,
        scenario_context_switching,
        scenario_mixed_conditions,
    ]
    
    results = []
    for scenario_func in scenarios:
        try:
            output_file = scenario_func(output_dir)
            results.append(output_file)
        except Exception as e:
            print(f"❌ Error in {scenario_func.__name__}: {e}")
    
    print(f"\n✅ Generated {len(results)} scenario traces")
    return results


if __name__ == "__main__":
    run_all_scenarios()
