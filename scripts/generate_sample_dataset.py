import csv
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from marthr_simulator import MarthrSimulator, MarthrContext

OUTPUT = ROOT / "data" / "raw" / "marthr_sample.csv"


def run_scenario(scenario_name, grid_size, rounds, packet_loss_prob, safety, threat, seeds=20):
    """Run one scenario across multiple seeds and collect metrics."""
    rows = []
    for seed in range(seeds):
        sim = MarthrSimulator(grid_size=grid_size, seed=seed)
        sim.run_simulation(
            rounds=rounds,
            packet_loss_prob=packet_loss_prob,
            safety=safety,
            threat=threat
        )
        # Collect per-node final metrics
        for node_id, node in sim.nodes.items():
            if node_id == 1:
                continue
            rows.append({
                "seed": seed,
                "scenario": scenario_name,
                "node_id": node_id,
                "parent": node.parent if node.parent else 0,
                "rank": round(node.rank, 4),
                "trust": round(node.trust_table.get(node.parent) if node.parent else 0.0, 4),
                "energy": round(node.energy, 4),
                "qos_latency": round(1.0 - node.last_mcs, 4) if node.last_mcs > 0 else 1.0,
                "mcs": round(node.last_mcs, 4),
                "hop_count": node.hop_count,
                "convergence_time": node.convergence_time,
                "packet_loss_rate": round(node.packet_loss_rate, 4),
            })
    return rows


def main() -> None:
    all_rows = []

    # Scenario 1: Lossless baseline
    all_rows.extend(run_scenario(
        "lossless", grid_size=5, rounds=100,
        packet_loss_prob=0.0,
        safety=MarthrContext.SAFETY_NORMAL,
        threat=MarthrContext.THREAT_NORMAL
    ))

    # Scenario 2: Lossy network
    all_rows.extend(run_scenario(
        "lossy", grid_size=5, rounds=100,
        packet_loss_prob=0.20,
        safety=MarthrContext.SAFETY_NORMAL,
        threat=MarthrContext.THREAT_NORMAL
    ))

    # Scenario 3: Attack scenario
    all_rows.extend(run_scenario(
        "attack", grid_size=5, rounds=100,
        packet_loss_prob=0.05,
        safety=MarthrContext.SAFETY_CRITICAL,
        threat=MarthrContext.THREAT_HIGH
    ))

    os.makedirs(OUTPUT.parent, exist_ok=True)
    fieldnames = ["seed", "scenario", "node_id", "parent", "rank", "trust",
                  "energy", "qos_latency", "mcs", "hop_count",
                  "convergence_time", "packet_loss_rate"]
    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_rows)

    print(f"Wrote {len(all_rows)} rows to {OUTPUT}")


if __name__ == "__main__":
    main()
