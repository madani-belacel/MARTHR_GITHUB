# MANET-Trust-Aware Hierarchical Routing Protocol (MARTHR)
## High-Quality Research Project Proposal

**Project Location:** `/home/madani/MARTHR`  
**Start Date:** July 5, 2026  
**Target Venue:** IEEE/ACM networking conference (2026/2027)

---

## 1. LITERATURE REVIEW & RECENT CONTRIBUTIONS (7 Key Publications 2026)

### 1.1 Recent Publications Analysis (2026 & Late 2025)

#### Publication 1: FANET Routing Resilience via Fuzzy-Bio-Inspired Methods
- **Reference:** arXiv:2606.26124 (June 2026)
- **Title:** "Enhancing FANET Routing Resilience: A Fuzzy-Driven Bio-Inspired Approach and Its Quantitative Evaluation"
- **Authors:** Xinwang Yuan, Jinshu Su, Yusheng Xia, Congxi Song
- **Key Contribution:** Bio-inspired (swarm intelligence) + fuzzy logic for FANET routing resilience
- **Future Work:** Real-world deployment, 3D topology dynamics, heterogeneous aerial swarms
- **Gap Identified:** No trust/security integration; limited to aerial networks

#### Publication 2: Federated Learning in Tactical MANETs
- **Reference:** arXiv:2606.09504 (June 2026)
- **Title:** "Hierarchical Federated Learning for Unsupervised Waveform Classification over Tactical MANETs"
- **Authors:** Charles E. Thornton, Daniel J. Jakubisin
- **Key Contribution:** Distributed machine learning on contested radio networks; privacy-preserving waveform sensing
- **Future Work:** Real-time ML deployment, energy-efficient models, dynamic topology learning
- **Gap Identified:** No routing protocol integration; focus on signal processing only

#### Publication 3: OLSR Security via Passive ML Reconnaissance
- **Reference:** arXiv:2606.00184 (June 2026)
- **Title:** "Passive Reconnaissance of Routing-Layer Defenses in OLSR-Based MANETs using ML"
- **Authors:** Nadav Schweitzer, Kiril Danilchenko, Ariel Stulman
- **Key Contribution:** ML-based detection of routing-layer attacks without active probing
- **Future Work:** Multi-protocol security analysis, real-time mitigation, zero-trust frameworks
- **Gap Identified:** Defensive analysis only; no proactive protocol redesign for defense

#### Publication 4: Hybrid Secure Routing in MANETs
- **Reference:** arXiv:2602.13204 (February 2026, submitted January 2026)
- **Title:** "Hybrid Secure Routing in Mobile Ad-hoc Networks (MANETs)"
- **Authors:** Soundes Oumaima Boufaida et al.
- **Key Contribution:** Hybrid approach combining cryptographic and trust-based routing
- **Future Work:** Energy efficiency analysis, scalability to large topologies, IoT integration
- **Gap Identified:** High overhead; no adaptive context-awareness; no energy metrics

#### Publication 5: SDN-Driven MANET Innovations
- **Reference:** arXiv:2601.10544 (January 2026)
- **Title:** "SDN-Driven Innovations in MANETs and IoT: A Path to Smarter Networks"
- **Authors:** Andrea Piroddi, Riccardo Fonti
- **Key Contribution:** SDN centralization paradigm applied to decentralized MANETs
- **Future Work:** Hybrid centralized/decentralized control, edge AI placement, 6G integration
- **Gap Identified:** Control overhead; relies on global knowledge; weak for highly dynamic scenarios

#### Publication 6: Beaconless Geocast Protocols (Theoretical)
- **Reference:** arXiv:2512.02663 (December 2025)
- **Title:** "Theoretical analysis of beaconless geocast protocols in 1D"
- **Authors:** Joachim Gudmundsson et al.
- **Key Contribution:** Formal complexity analysis of location-aware routing without beacons
- **Future Work:** 2D/3D analysis, practical implementation, topology-aware optimization
- **Gap Identified:** Limited to 1D; no empirical validation; no energy/latency trade-offs

#### Publication 7: DTN-Based Opportunistic Routing for Disaster Recovery
- **Reference:** arXiv:2511.15710 (November 2025)
- **Title:** "Improving Resiliency of Vital Services in Flood-Affected Regions of Bangladesh Using Next-Generation Opportunistic DTN Edge Ad Hoc Networks"
- **Authors:** Md Main Uddin Hasan, Milena Radenkovic
- **Key Contribution:** Delay-tolerant networks + opportunistic forwarding for disaster/emergency scenarios
- **Future Work:** Cross-layer optimization, 5G/satellite integration, real-time SLA guarantees
- **Gap Identified:** Disaster-specific; no multi-criteria optimization; limited to emergency contexts

---

## 2. RESEARCH GAPS & OPPORTUNITIES

### 2.1 Identified Gaps Across Publications
1. **Trust Integration:** No publication combines trust metrics WITH energy/QoS metrics in a unified framework
2. **Adaptive Context Fusion:** No protocol adapts routing decisions based on network state, threat level, and energy budget simultaneously
3. **Security + Performance Trade-off:** Existing work treats security as orthogonal; no Pareto optimization
4. **Heterogeneous Topology Support:** Limited support for mixed aerial, ground, and IoT nodes in a single routing protocol
5. **Energy-Aware Trust Decay:** No model for how trust degrades when nodes are energy-constrained
6. **Multi-Objective Ablation:** No ablation studies showing individual contribution of each metric

### 2.2 Opportunity: MARTHR (MANET-Trust-Aware Hierarchical Routing Protocol)
A **context-aware, multi-objective hierarchical routing protocol** that:
- Integrates **trust metrics** (node reputation, link quality) with **energy awareness** and **QoS requirements**
- Adapts **rank computation** based on application domain (safety-critical vs. best-effort)
- Uses **federated trust aggregation** for scalability in large networks
- Supports **heterogeneous topologies** (aerial, ground, sensor nodes)
- Provides **transparent ablation mechanisms** for research repeatability

---

## 3. PROPOSED CONTRIBUTIONS

### 3.1 Core Innovation: MARTHR Protocol
**Architecture:**
```
┌─────────────────────────────────────────────────────────────┐
│ Application Layer (QoS Requirement: safety_level, data_rate)│
├─────────────────────────────────────────────────────────────┤
│ Trust Aggregation Layer (Federated Trust + Link Metrics)    │
│  - Node Reputation (peer feedback, historical success)     │
│  - Link Quality (PRR, latency, RSSI)                        │
│  - Threat Context (intrusion detection feedback)           │
├─────────────────────────────────────────────────────────────┤
│ Rank Computation (Multi-Criteria Score + Hysteresis)       │
│  - MCS = α·trust + β·energy + γ·qos                        │
│  - Safety-critical: trust weights = 60%, energy = 20%, QoS = 20%
│  - Best-effort: trust = 30%, energy = 50%, QoS = 20%      │
├─────────────────────────────────────────────────────────────┤
│ RPL (Routing Protocol for LLN) Integration                 │
│  - Custom Objective Function (OCP 9): MARTHR-MCS          │
│  - Hysteresis bounds on context changes                    │
├─────────────────────────────────────────────────────────────┤
│ MAC & PHY Layers (Link Estimation, Trust Feedback)         │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 Key Differentiators vs. Prior Work

| Aspect | Prior Work | MARTHR |
|--------|-----------|--------|
| Trust + Energy | Separate concerns | **Unified MCS** |
| Context Adaptation | Fixed weights | **Dynamic α,β,γ** per domain |
| Scalability | Centralized | **Federated trust aggregation** |
| Heterogeneous Nodes | Single-tier | **Multi-tier hierarchy** |
| Ablation Support | Ad-hoc | **Configurable protocol levers** |
| Security-Performance | Trade-off only | **Pareto analysis** |

### 3.3 Scientific Contributions

1. **MARTHR Protocol Definition**
   - Formal MCS model with context fusion
   - Federated trust computation rules
   - Integration roadmap with RPL/MRHOF

2. **Empirical Evaluation**
   - Multi-seed Cooja simulation ($N \geq 20$ seeds)
   - 25–100 node topologies (ground + aerial mix)
   - Metrics: PDR, latency, energy, trust convergence time
   - Attack scenario testing (selective forwarding, rank inflation)

3. **Ablation Studies (A1–A3)**
   - A1: Trust disabled → energy-aware routing only
   - A2: Energy disabled → trust-based routing only
   - A3: QoS disabled → trust+energy trade-off
   - Show individual contribution of each lever

4. **Open-Source Implementation**
   - Contiki-NG firmware (rpl-lite + MARTHR OCP)
   - CSV-to-figure pipeline for reproducibility
   - Docker environment for repeatable builds

---

## 4. PROJECT ROADMAP (Phase 1: Simulation & Validation)

### Phase 1A: Foundation & Implementation (Month 1–2)
- [ ] Design MCS model and context-fusion rules
- [ ] Implement MARTHR-OCP in Contiki-NG rpl-lite
- [ ] Create federated trust aggregation module
- [ ] Unit tests on single-node simulation

### Phase 1B: Cooja Campaign Baseline (Month 2–3)
- [ ] Setup 25-node reference topology (grid + random)
- [ ] Run lossless reference runs ($N=4$ seeds, 1800s each)
- [ ] Collect baseline PDR/latency/energy for MRHOF, MARTHR-trust-only, MARTHR-energy-only, MARTHR-full
- [ ] Archive CSVs and commit to repository

### Phase 1C: Attack Simulation & Stress Testing (Month 3–4)
- [ ] Inject selective-forwarding attacks (10%, 25%, 50% attacker nodes)
- [ ] Rank inflation attacks (fake MCS reports)
- [ ] Measure detection latency and FPR
- [ ] Stress test: 2× traffic load, 50% link loss, high node mobility

### Phase 1D: Ablation Studies & Analysis (Month 4–5)
- [ ] Run ablations A1–A3 on same topology
- [ ] Mann–Whitney statistical tests ($N \geq 20$ seeds)
- [ ] Generate Pareto frontier plots (trust vs. energy vs. latency)
- [ ] Document trust convergence time per scenario

### Phase 1E: Figure Generation & Manuscript (Month 5–6)
- [ ] Regenerate all figures from committed CSVs
- [ ] Write methodology, results, discussion sections
- [ ] Prepare camera-ready PDF for venue submission

---

## 5. REPRODUCIBILITY & OPEN-SOURCE STRUCTURE

```
proposed_projet/
├── code_source/
│   ├── marthr_ocp.c / .h         # Objective Function implementation
│   ├── marthr_trust.c / .h       # Federated trust module
│   ├── marthr_context.c / .h     # Context-fusion rules
│   ├── project-conf.h            # Build configuration
│   ├── Makefile
│   ├── simulations/
│   │   ├── 25node_grid.csc       # Reference topology
│   │   ├── 25node_random.csc
│   │   ├── attack_sf_10pct.csc
│   │   ├── stress_2xtrafic.csc
│   │   └── scripts/
│   │       └── parse_marthr_metrics.py  # Log parser
│   ├── tests/
│   │   └── unit_*_test.c
│   └── README.md
├── data/
│   ├── raw/
│   │   ├── baseline_seed*.csv
│   │   ├── attack_*.csv
│   │   └── stress_*.csv
│   ├── estimated/
│   │   ├── *_pdr.csv
│   │   ├── *_latency.csv
│   │   ├── *_energy.csv
│   │   └── *_trust_convergence.csv
│   └── README_DATA_PROVENANCE.md
├── scripts/
│   ├── regenerate_base_csvs.py   # From raw → estimated
│   ├── statistics/
│   │   └── compute_ablation_stats.py
│   ├── generate_marthr_figures.py # CSV → PDF figures
│   └── figures_manifest.csv
├── manuscript/
│   ├── main.tex                  # Main LaTeX
│   ├── abstract.tex
│   ├── introduction.tex
│   ├── architecture.tex
│   ├── evaluation.tex
│   ├── ablation.tex
│   ├── discussion.tex
│   ├── conclusion.tex
│   ├── sections/
│   ├── Figures/
│   │   ├── CAPTIONS_EN.tex
│   │   ├── Fig_*_Architecture.pdf
│   │   ├── Fig_*_PDR.pdf
│   │   ├── Fig_*_Ablation.pdf
│   │   └── ...
│   ├── tables/
│   ├── bib/
│   │   └── references.bib
│   ├── main.pdf
│   └── README.md
├── internal/
│   ├── PHASE1_ROADMAP.md         # This file (expanded)
│   ├── METHODOLOGY_AUDIT.md      # Verification workflow
│   ├── PROJECT_HEALTH_REPORT.md
│   ├── FIGURE_DEPENDENCIES.md
│   ├── compile.sh                # Build automation
│   └── UBUNTU_EXECUTION_PLAN.md
├── requirements.txt              # Python + system dependencies
├── README.md                     # Public-facing guide
├── BUILD_NOTES.txt              # Build troubleshooting
├── MASTER_TRACKER.md            # High-level status
└── LICENSE                      # Open-source (GPL 3.0)
```

---

## 6. SUCCESS CRITERIA

### Quantitative Metrics
1. **PDR Improvement:** MARTHR ≥ 5% higher than MRHOF under attacks
2. **Energy Efficiency:** ≤ 15% overhead vs. MRHOF in non-stressed scenarios
3. **Trust Convergence:** < 30 seconds to stabilize in 25-node network
4. **Reproducibility:** All figures regenerable from committed CSVs
5. **Statistical Significance:** Mann–Whitney p < 0.05 for ablations

### Qualitative Metrics
1. Open-source code + CSV pipeline available
2. Manuscript accepted at top-tier venue (IEEE/ACM)
3. Clear documentation for future reproduction/extension
4. Zero gaps between narrative, figures, and committed data

---

## 7. COLLABORATION & FUTURE PHASES

### Phase 2 (Real Deployment)
- Energest-calibrated energy profiling on testbed
- Real UAV swarms (if resources available)
- Certification on battery-constrained nodes

### Phase 3 (Machine Learning Integration)
- Q-learning for adaptive context fusion
- Deep RL for attack prediction
- Federated learning across untrusted nodes

### Phase 4 (Standardization)
- RFC proposal for IETF (if applicable)
- RFC 6550 (RPL) alignment and extension discussion

---

## 8. REFERENCES & LITERATURE BASE

See: `LITERATURE_REVIEW.md` (included)

---

**Next Step:** Proceed to Phase 1A implementation with firmware coding.
