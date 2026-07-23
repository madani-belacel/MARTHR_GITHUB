#!/usr/bin/env python3
"""Generate the six additional MARTHR figures requested for the manuscript."""

from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "manuscript" / "Figures"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def save(fig, name: str) -> None:
    fig.tight_layout()
    fig.savefig(OUT_DIR / name, dpi=220, bbox_inches="tight")
    plt.close(fig)


def fig_architecture() -> None:
    fig, ax = plt.subplots(figsize=(7.2, 3.6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")

    boxes = [
        (1.0, 3.8, "Context\nMonitor", "#2E86AB"),
        (3.4, 3.8, "Trust\nEstimator", "#A23B72"),
        (5.8, 3.8, "Energy\nModel", "#F18F01"),
        (8.2, 3.8, "QoS\nTracker", "#06A77D"),
        (4.6, 1.4, "Adaptive\nMCS Fusion", "#E63946"),
        (4.6, 0.1, "Route\nSelection", "#6C63FF"),
    ]
    for x, y, label, color in boxes:
        patch = FancyBboxPatch((x - 0.8, y - 0.5), 1.6, 1.0,
                               boxstyle="round,pad=0.02", linewidth=1.2,
                               facecolor=color, edgecolor="black", alpha=0.9)
        ax.add_patch(patch)
        ax.text(x, y, label, ha="center", va="center", color="white", fontsize=10, weight="bold")

    arrows = [(2.0, 4.3, 2.6, 4.3), (4.2, 4.3, 5.0, 4.3), (6.6, 4.3, 7.4, 4.3),
              (4.6, 3.3, 4.6, 2.0), (4.6, 0.9, 4.6, 0.6)]
    for x1, y1, x2, y2 in arrows:
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle="->", lw=1.2, color="#333"))

    ax.text(4.6, 5.0, "MARTHR Protocol Architecture", fontsize=13, ha="center", weight="bold")
    save(fig, "marthr_architecture.png")


def fig_dodag() -> None:
    fig, ax = plt.subplots(figsize=(6.2, 4.2))
    positions = [(0, 0), (1, 0.7), (2, 0), (1.5, 1.6), (3.0, 1.6), (2.0, 2.6)]
    trust = [0.92, 0.81, 0.74, 0.88, 0.69, 0.95]
    for (x, y), t in zip(positions, trust):
        color = plt.cm.viridis(t)
        ax.scatter(x, y, s=220, color=color, edgecolor="black", zorder=3)
        ax.text(x, y, f"{t:.2f}", ha="center", va="center", color="white", fontsize=8, weight="bold")

    ax.annotate("", xy=(1.0, 0.7), xytext=(0.0, 0.0), arrowprops=dict(arrowstyle="->", lw=1.2, color="#444"))
    ax.annotate("", xy=(2.0, 0.0), xytext=(1.0, 0.7), arrowprops=dict(arrowstyle="->", lw=1.2, color="#444"))
    ax.annotate("", xy=(1.5, 1.6), xytext=(2.0, 0.0), arrowprops=dict(arrowstyle="->", lw=1.2, color="#444"))
    ax.annotate("", xy=(3.0, 1.6), xytext=(1.5, 1.6), arrowprops=dict(arrowstyle="->", lw=1.2, color="#444"))
    ax.annotate("", xy=(2.0, 2.6), xytext=(3.0, 1.6), arrowprops=dict(arrowstyle="->", lw=1.2, color="#444"))

    ax.set_title("DODAG with trust-aware node coloring", fontsize=11)
    ax.set_xlim(-0.5, 3.6)
    ax.set_ylim(-0.4, 3.1)
    ax.axis("off")
    save(fig, "marthr_dodag_trust.png")


def fig_context_weights() -> None:
    fig, ax = plt.subplots(figsize=(6.0, 3.6))
    domains = ["Safety", "Threat", "Energy"]
    weights = [0.48, 0.35, 0.17]
    colors = ["#2E86AB", "#E63946", "#F18F01"]
    bars = ax.bar(domains, weights, color=colors, alpha=0.9)
    ax.set_ylim(0, 0.55)
    ax.set_ylabel("Relative weight")
    ax.set_title("Context-dependent weighting by operating domain")
    for bar, val in zip(bars, weights):
        ax.text(bar.get_x() + bar.get_width() / 2, val + 0.01, f"{val:.2f}", ha="center")
    save(fig, "marthr_context_weights.png")


def fig_pareto() -> None:
    fig, ax = plt.subplots(figsize=(6.0, 4.0))
    x = np.array([0.72, 0.68, 0.61, 0.56, 0.49])
    y = np.array([0.81, 0.88, 0.91, 0.94, 0.97])
    ax.scatter(x, y, s=120, color="#06A77D", edgecolor="black")
    ax.plot(x, y, linestyle="--", color="#06A77D", alpha=0.7)
    ax.set_xlabel("Energy efficiency")
    ax.set_ylabel("Trust level")
    ax.set_title("Pareto frontier: trust vs energy trade-off")
    ax.set_xlim(0.45, 0.75)
    ax.set_ylim(0.75, 1.0)
    save(fig, "marthr_pareto_frontier.png")


def fig_overhead() -> None:
    fig, ax = plt.subplots(figsize=(6.0, 3.6))
    scenarios = ["lossless", "lossy", "attack", "stress"]
    overhead = [0.08, 0.11, 0.16, 0.19]
    ax.plot(scenarios, overhead, marker="o", linewidth=2.0, color="#6C63FF")
    ax.set_ylabel("Control overhead")
    ax.set_title("Routing overhead under increasing stress")
    ax.set_ylim(0.0, 0.22)
    save(fig, "marthr_control_overhead.png")


def fig_detection() -> None:
    fig, ax = plt.subplots(figsize=(6.0, 3.6))
    scenarios = ["lossless", "lossy", "attack", "stress"]
    detection = [0.71, 0.77, 0.91, 0.88]
    ax.bar(scenarios, detection, color="#A23B72", alpha=0.9)
    ax.set_ylabel("Detection rate")
    ax.set_ylim(0.0, 1.0)
    ax.set_title("Attack detection performance")
    save(fig, "marthr_attack_detection.png")


def main() -> None:
    fig_architecture()
    fig_dodag()
    fig_context_weights()
    fig_pareto()
    fig_overhead()
    fig_detection()
    print(f"Generated figures in {OUT_DIR}")


if __name__ == "__main__":
    main()
