# MARTHR architecture specification

## 1. Objective
MARTHR is a context-aware routing objective that combines trust, energy, and QoS in a single rank computation.

## 2. Multi-criteria score
The core score is:

MCS = alpha * trust + beta * energy + gamma * qos

The weights are adapted from the current context:
- safety-critical: alpha=0.60, beta=0.20, gamma=0.20
- high-safety: alpha=0.45, beta=0.30, gamma=0.25
- normal: alpha=0.35, beta=0.40, gamma=0.25
- best-effort: alpha=0.30, beta=0.50, gamma=0.20

Threat and energy states slightly shift the distribution to favor trust or energy.

## 3. Trust model
- Each node stores local trust values for neighbors.
- Successes increase trust using a weighted update rule.
- Failures reduce trust more aggressively.
- Trust values remain bounded to the [0, 1] interval.

## 4. Metric logging
Each rank update emits a structured record with:
- node_id
- parent_id
- rank
- trust
- energy
- qos_latency
- mcs_score

## 5. Implementation status
The current repository contains:
- a portable core implementation in code_source/
- a Python validation test in code_source/tests/
- a reproducible synthetic data pipeline in scripts/

## 6. Next implementation steps
1. Translate the logic into a Contiki-NG objective function.
2. Add simulation scenarios and parsers.
3. Extend the analysis pipeline for ablation studies.
