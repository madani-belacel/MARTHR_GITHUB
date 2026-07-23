import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SIMULATIONS_DIR = ROOT / "data" / "estimated" / "simulations"
OUTPUT = ROOT / "data" / "estimated" / "metric_summary.csv"


def main() -> None:
    """Compute summary statistics from simulation campaign files."""
    all_rows = []
    
    for csv_file in sorted(SIMULATIONS_DIR.glob("campaign_*.csv")):
        with csv_file.open("r", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            for row in reader:
                all_rows.append(row)
    
    if not all_rows:
        raise SystemExit(f"No campaign data found in {SIMULATIONS_DIR}")

    def mean(values):
        return sum(values) / len(values)

    trust_values = [float(row["trust"]) for row in all_rows]
    energy_values = [float(row["energy"]) for row in all_rows]
    latency_values = [float(row["qos_latency"]) for row in all_rows]
    mcs_values = [float(row["mcs"]) for row in all_rows]

    summary = [
        ["metric", "mean", "min", "max"],
        ["trust", round(mean(trust_values), 4), round(min(trust_values), 4), round(max(trust_values), 4)],
        ["energy", round(mean(energy_values), 4), round(min(energy_values), 4), round(max(energy_values), 4)],
        ["latency", round(mean(latency_values), 4), round(min(latency_values), 4), round(max(latency_values), 4)],
        ["mcs_score", round(mean(mcs_values), 4), round(min(mcs_values), 4), round(max(mcs_values), 4)],
    ]

    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerows(summary)

    print(f"Wrote {OUTPUT}")
    print(OUTPUT.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
