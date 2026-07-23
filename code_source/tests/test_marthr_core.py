from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from marthr_core import Context, TrustTable, compute_score, log_metric


def main() -> int:
    ctx = Context(safety_level="critical", threat_level="high", energy_state="critical")
    alpha, beta, gamma = ctx.weights()
    assert alpha > 0.5
    assert beta > 0.2
    assert gamma > 0.1

    table = TrustTable()
    table.update_success(1, 0.9)
    table.update_success(1, 0.8)
    table.update_failure(1)
    trust = table.get(1)
    assert 0.0 <= trust <= 1.0

    score = compute_score(trust, 0.8, 0.7, ctx)
    assert 0.0 <= score <= 1.0

    log_metric({
        "node_id": 1,
        "parent_id": 2,
        "rank": 0.42,
        "trust": trust,
        "energy": 0.8,
        "qos_latency": 0.7,
        "mcs_score": score,
    })

    print("marthr_core_tests: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
