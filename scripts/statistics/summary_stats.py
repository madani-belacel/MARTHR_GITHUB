import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INPUT = ROOT / "data" / "raw" / "marthr_sample.csv"
OUTPUT = ROOT / "data" / "estimated" / "summary_stats.csv"


def main() -> None:
    rows = []
    with INPUT.open("r", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)

    by_scenario = {}
    for row in rows:
        scenario = row["scenario"]
        by_scenario.setdefault(scenario, []).append(row)

    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["scenario", "mean_rank", "mean_trust", "mean_energy", "mean_qos_latency", "mean_mcs"])
        for scenario, items in sorted(by_scenario.items()):
            mean_rank = sum(float(item["rank"]) for item in items) / len(items)
            mean_trust = sum(float(item["trust"]) for item in items) / len(items)
            mean_energy = sum(float(item["energy"]) for item in items) / len(items)
            mean_qos = sum(float(item["qos_latency"]) for item in items) / len(items)
            mean_mcs = sum(float(item["mcs"]) for item in items) / len(items)
            writer.writerow([scenario, round(mean_rank, 4), round(mean_trust, 4), round(mean_energy, 4), round(mean_qos, 4), round(mean_mcs, 4)])

    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
