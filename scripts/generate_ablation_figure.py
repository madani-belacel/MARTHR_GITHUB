import csv
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "estimated" / "table2_ablation.csv"
OUTPUT = ROOT / "manuscript" / "Figures" / "marthr_ablation_figure.png"


def main() -> None:
    with INPUT.open("r", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    if rows and "variant" in rows[0]:
        variants = [row["variant"] for row in rows]
        trust = [float(row["trust"]) for row in rows]
        energy = [float(row["energy"]) for row in rows]
        qos = [float(row["qos"]) for row in rows]
        mcs = [float(row["mcs"]) for row in rows]
    else:
        variants = [row["scenario"] for row in rows]
        trust = [0.0 for _ in rows]
        energy = [0.0 for _ in rows]
        qos = [0.0 for _ in rows]
        mcs = [float(row["mean_mcs"]) for row in rows]

    x = range(len(variants))
    width = 0.18

    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    ax.bar([i - 1.5 * width for i in x], trust, width=width, label="Trust")
    ax.bar([i - 0.5 * width for i in x], energy, width=width, label="Energy")
    ax.bar([i + 0.5 * width for i in x], qos, width=width, label="QoS")
    ax.bar([i + 1.5 * width for i in x], mcs, width=width, label="MCS")
    ax.set_xticks(list(x))
    ax.set_xticklabels(variants, rotation=18)
    ax.set_ylabel("Normalized score")
    ax.set_title("Exploratory scenario proxies (not controlled ablation)")
    ax.set_ylim(0.0, 1.0)
    ax.legend(loc="upper left", frameon=False)
    ax.grid(axis="y", alpha=0.25)

    fig.tight_layout()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT, dpi=220)
    plt.close(fig)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
