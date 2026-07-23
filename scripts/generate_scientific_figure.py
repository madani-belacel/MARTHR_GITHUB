import csv
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "estimated" / "summary_stats.csv"
OUTPUT = ROOT / "manuscript" / "Figures" / "marthr_scientific_figure.png"


def main() -> None:
    with INPUT.open("r", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    scenarios = [row["scenario"] for row in rows]
    energy = np.array([float(row["mean_energy"]) for row in rows])
    mcs = np.array([float(row["mean_mcs"]) for row in rows])
    qos = np.array([float(row["mean_qos_latency"]) for row in rows])

    x = np.arange(len(scenarios))
    width = 0.25

    fig, ax1 = plt.subplots(figsize=(7.2, 4.2))
    color1 = "#1f4e79"
    color2 = "#c0504d"
    color3 = "#9bbb59"

    ax1.set_ylabel("Energy / MCS", color=color1)
    ax1.bar(x - width, energy, width=width, color=color1, label="Mean Energy")
    ax1.bar(x, mcs, width=width, color=color2, label="Mean MCS")
    ax1.tick_params(axis="y", labelcolor=color1)
    ax1.set_xticks(x)
    ax1.set_xticklabels(scenarios, rotation=20)
    ax1.set_ylim(0.0, 1.05)
    ax1.grid(axis="y", alpha=0.25)

    ax2 = ax1.twinx()
    ax2.plot(x + width, qos, color=color3, marker="o", linewidth=2.2, label="Mean QoS Latency")
    ax2.set_ylabel("QoS Latency", color=color3)
    ax2.tick_params(axis="y", labelcolor=color3)
    ax2.set_ylim(0.0, 1.0)

    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc="upper left", frameon=False)

    ax1.set_title("MARTHR performance under representative scenarios")
    fig.tight_layout()

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT, dpi=220)
    plt.close(fig)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
