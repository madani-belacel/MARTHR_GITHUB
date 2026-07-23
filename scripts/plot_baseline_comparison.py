import csv
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "estimated" / "baseline_comparison.csv"
OUTPUT = ROOT / "manuscript" / "Figures" / "baseline_comparison.png"


def main() -> None:
    with INPUT.open("r", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    protocols = [row["protocol"] for row in rows]
    trust = [float(row["mean_trust"]) for row in rows]
    latency = [float(row["mean_latency"]) for row in rows]

    fig, ax = plt.subplots(figsize=(6, 3.8))
    x = range(len(protocols))
    ax.bar([i - 0.18 for i in x], trust, width=0.36, color="#1f4e79", label="Mean trust")
    ax.bar([i + 0.18 for i in x], latency, width=0.36, color="#c0504d", label="Mean latency")
    ax.set_xticks(list(x))
    ax.set_xticklabels(protocols)
    ax.set_ylabel("Normalized value")
    ax.set_title("MARTHR vs. MRHOF baseline")
    ax.grid(axis="y", alpha=0.3)
    ax.legend(frameon=False)
    fig.tight_layout()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT, dpi=220)
    plt.close(fig)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
