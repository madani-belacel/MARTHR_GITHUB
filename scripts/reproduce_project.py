import subprocess
import sys
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(cmd: list[str], cwd: Path | None = None) -> None:
    print(f"$ {' '.join(cmd)}")
    subprocess.run(cmd, cwd=cwd, check=True)


def check_output(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Expected output file is missing: {path}")


def main() -> None:
    steps = [
        [sys.executable, "scripts/run_simulation_campaign.py"],
        [sys.executable, "scripts/regenerate_tables.py"],
        [sys.executable, "scripts/generate_sample_dataset.py"],
        [sys.executable, "scripts/statistics/summary_stats.py"],
        [sys.executable, "scripts/statistics/analyze_metrics.py"],
        [sys.executable, "scripts/analyze_campaigns.py"],
        [sys.executable, "scripts/generate_latex_table.py"],
        [sys.executable, "scripts/generate_ieee_figures.py"],
        [sys.executable, "scripts/generate_missing_figures.py"],
        [sys.executable, "scripts/generate_ablation_figure.py"],
        [sys.executable, "scripts/generate_scientific_figure.py"],
        [sys.executable, "scripts/generate_simple_plot.py"],
    ]

    for cmd in steps:
        run(cmd, cwd=ROOT)

    expected_outputs = [
        ROOT / "data" / "estimated" / "simulations" / "campaign_lossless_baseline_aggregated.csv",
        ROOT / "data" / "estimated" / "simulations" / "campaign_lossy_network_aggregated.csv",
        ROOT / "data" / "estimated" / "simulations" / "campaign_attack_high_threat_aggregated.csv",
        ROOT / "data" / "estimated" / "simulations" / "campaign_energy_stress_aggregated.csv",
        ROOT / "data" / "estimated" / "simulations" / "campaign_stress_large_grid_aggregated.csv",
        ROOT / "data" / "estimated" / "simulations" / "campaign_mobility_dynamic_aggregated.csv",
        ROOT / "data" / "estimated" / "simulations" / "campaign_qos_sensitive_aggregated.csv",
        ROOT / "data" / "estimated" / "simulations" / "campaign_mixed_attack_energy_aggregated.csv",
        ROOT / "data" / "estimated" / "table2_ablation.csv",
        ROOT / "data" / "estimated" / "table3_summary.csv",
        ROOT / "data" / "raw" / "marthr_sample.csv",
        ROOT / "manuscript" / "tables" / "results_table.tex",
        ROOT / "manuscript" / "tables" / "ablation_table.tex",
    ]

    for output in expected_outputs:
        check_output(output)

    skip_latex = "--skip-latex" in sys.argv
    if skip_latex:
        print("Skipping LaTeX compilation (--skip-latex flag)")
    elif shutil.which("latexmk"):
        run(["latexmk", "-pdf", "-interaction=nonstopmode", "main.tex"], cwd=ROOT / "manuscript")
    else:
        print("WARNING: latexmk not found, skipping LaTeX compilation")

    print("Reproduction pipeline completed successfully.")


if __name__ == "__main__":
    main()
