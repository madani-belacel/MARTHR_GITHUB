import csv
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "estimated" / "summary_stats.csv"
OUTPUT = ROOT / "manuscript" / "Figures" / "marthr_summary_plot.png"


def main() -> None:
    rows = []
    with INPUT.open("r", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)

    scenarios = [row["scenario"] for row in rows]
    energy = [float(row["mean_energy"]) for row in rows]
    mcs = [float(row["mean_mcs"]) for row in rows]

    fig, ax = plt.subplots(figsize=(6, 3.5))
    x = range(len(scenarios))
    ax.bar([i - 0.18 for i in x], energy, width=0.36, label="Mean Energy")
    ax.bar([i + 0.18 for i in x], mcs, width=0.36, label="Mean MCS")
    ax.set_xticks(list(x))
    ax.set_xticklabels(scenarios, rotation=20)
    ax.set_ylabel("Value")
    ax.set_title("MARTHR summary metrics")
    ax.legend()
    ax.grid(axis="y", alpha=0.3)

    fig.tight_layout()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT, dpi=200)
    plt.close(fig)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
