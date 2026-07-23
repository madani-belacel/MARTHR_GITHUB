import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
METRICS_CSV = ROOT / "data" / "estimated" / "metric_summary.csv"
OUTPUT = ROOT / "manuscript" / "tables" / "results_table.tex"


def read_rows(csv_path: Path):
    with csv_path.open("r", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_table(output_path: Path) -> None:
    metric_rows = read_rows(METRICS_CSV)
    lines = []
    lines.append("\\begin{table}[t]")
    lines.append("\\centering")
    lines.append("\\caption{Descriptive statistics of MARTHR metrics across the available campaign outputs.}")
    lines.append("\\label{tab:results}")
    lines.append("\\begin{tabular}{lccc}")
    lines.append("\\toprule")
    lines.append("Metric & Mean & Min & Max \\\\ ")
    lines.append("\\midrule")
    for row in metric_rows:
        metric_name = {
            'trust': 'Trust',
            'energy': 'Energy',
            'latency': 'Normalized latency',
            'mcs_score': 'MCS',
        }.get(row['metric'], row['metric'].replace('_', '\\_'))
        lines.append(f"{metric_name} & {row['mean']} & {row['min']} & {row['max']} \\\\ ")
    lines.append("\\bottomrule")
    lines.append("\\end{tabular}")
    lines.append("\\end{table}")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    write_table(OUTPUT)
    print(f"Wrote {OUTPUT}")
