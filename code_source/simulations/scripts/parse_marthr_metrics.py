import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
INPUT = ROOT / "data" / "raw" / "simulation_log.txt"
OUTPUT = ROOT / "data" / "estimated" / "parsed_simulation_metrics.csv"


def parse_log(path: Path) -> list[dict]:
    if not path.exists():
        return []

    rows = []
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        m = re.search(r"node=(\d+) parent=(\d+) rank=([0-9.]+) trust=([0-9.]+) energy=([0-9.]+) qos_latency=([0-9.]+) mcs=([0-9.]+)", line)
        if m:
            rows.append({
                "node_id": int(m.group(1)),
                "parent_id": int(m.group(2)),
                "rank": float(m.group(3)),
                "trust": float(m.group(4)),
                "energy": float(m.group(5)),
                "qos_latency": float(m.group(6)),
                "mcs_score": float(m.group(7)),
            })
    return rows


def main() -> None:
    rows = parse_log(INPUT)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["node_id", "parent_id", "rank", "trust", "energy", "qos_latency", "mcs_score"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"Parsed {len(rows)} metric rows into {OUTPUT}")


if __name__ == "__main__":
    main()
