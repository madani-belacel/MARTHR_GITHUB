from dataclasses import dataclass, field
from typing import List


@dataclass
class Context:
    safety_level: str = "normal"
    threat_level: str = "normal"
    energy_state: str = "normal"

    def weights(self) -> tuple[float, float, float]:
        alpha, beta, gamma = 0.35, 0.40, 0.25
        if self.safety_level == "critical":
            alpha, beta, gamma = 0.60, 0.20, 0.20
        elif self.safety_level == "high":
            alpha, beta, gamma = 0.45, 0.30, 0.25
        elif self.safety_level == "best-effort":
            alpha, beta, gamma = 0.30, 0.50, 0.20

        if self.threat_level == "high":
            alpha += 0.05
            gamma += 0.03
        elif self.threat_level == "low":
            beta += 0.04

        if self.energy_state == "critical":
            beta += 0.08
            alpha -= 0.03
        elif self.energy_state == "sufficient":
            beta -= 0.03
            gamma += 0.02

        total = alpha + beta + gamma
        if total > 1.0 + 1e-5:
            return alpha / total, beta / total, gamma / total
        return alpha, beta, gamma


@dataclass
class TrustEntry:
    node_id: int
    trust_score: float = 0.5
    failures: int = 0
    successes: int = 0
    last_seen: int = 0


@dataclass
class TrustTable:
    entries: List[TrustEntry] = field(default_factory=list)

    def update_success(self, node_id: int, link_quality: float) -> None:
        entry = self._find(node_id)
        if entry is None:
            entry = TrustEntry(node_id=node_id)
            self.entries.append(entry)
        entry.successes += 1
        entry.trust_score = entry.trust_score * 0.7 + link_quality * 0.3
        entry.last_seen += 1

    def update_failure(self, node_id: int) -> None:
        entry = self._find(node_id)
        if entry is None:
            entry = TrustEntry(node_id=node_id)
            self.entries.append(entry)
        entry.failures += 1
        entry.trust_score = max(0.0, entry.trust_score - 0.15)
        entry.last_seen += 1

    def get(self, node_id: int) -> float:
        entry = self._find(node_id)
        return 0.5 if entry is None else entry.trust_score

    def _find(self, node_id: int) -> TrustEntry | None:
        for entry in self.entries:
            if entry.node_id == node_id:
                return entry
        return None


def compute_score(trust: float, energy: float, qos: float, ctx: Context) -> float:
    alpha, beta, gamma = ctx.weights()
    score = alpha * trust + beta * energy + gamma * qos
    return max(0.0, min(1.0, score))


def log_metric(entry: dict, out=None) -> None:
    if out is None:
        out = print
    out(
        f"node={entry['node_id']} parent={entry['parent_id']} rank={entry['rank']:.4f} "
        f"trust={entry['trust']:.4f} energy={entry['energy']:.4f} "
        f"qos_latency={entry['qos_latency']:.4f} mcs={entry['mcs_score']:.4f}"
    )
