# MARTHR: MANET-Trust-Aware Hierarchical Routing Protocol

**A high-quality research project proposal for ad-hoc network routing with unified trust, energy, and QoS optimization.**

---

## 🔬 Scientific Rigor and Reproduction Workflow

This project now follows a stricter research workflow inspired by the reproduction and evaluation checklists in the Temps folder. The goal is to make the work more robust, more reproducible, and more credible for scientific review.

### Quality principles applied here
- Verify before claiming success.
- Keep a clear link between data, scripts, figures, and manuscript text.
- Search for placeholders, inconsistencies, and undocumented assumptions.
- Re-run the full pipeline after each correction.
- Document the provenance of every result used in the paper.

### Project-specific validation flow
1. Reproduce the project pipeline with the command below.
2. Inspect the raw and estimated data files.
3. Ensure that figures and tables are generated from those files.
4. Rebuild the manuscript and verify that the PDF is up to date.

```bash
cd /home/madani/MARTHR
. .venv/bin/activate
python3 scripts/reproduce_project.py
```

### Key reference documents
- [EXECUTION_PLAN.md](EXECUTION_PLAN.md) for the detailed roadmap.
- [conversation_opencode_vscode/CHECKLIST_REPRODUCTION.md](conversation_opencode_vscode/CHECKLIST_REPRODUCTION.md) for the reproduction checklist.
- [conversation_opencode_vscode/METHODOLOGIE_EVALUATION.md](conversation_opencode_vscode/METHODOLOGIE_EVALUATION.md) for the evaluation methodology.

---

## 🎯 Project Overview

### Vision
Design and evaluate **MARTHR**, a novel routing protocol that **simultaneously optimizes**:

This is not a short-hour prototype. The project is structured to require a minimum of one full week of sustained work for a first complete implementation cycle, including setup, coding, validation, and documentation.
- **Trust metrics** (node reputation, link quality)
- **Energy awareness** (residual energy, energy budget)
- **QoS requirements** (latency, bandwidth, reliability)

through a unified **Multi-Criteria Score (MCS)** with **adaptive context-aware weights**.

### Why MARTHR?

Recent publications (2026) show that:
- ✅ FANET protocols optimize routing but ignore trust
- ✅ Secure routing protocols add trust but ignore QoS & energy
- ✅ SDN approaches centralize control (not realistic for ad-hoc)
- ❌ **No protocol unifies trust + energy + QoS with ablation studies**

**MARTHR fills this gap** by providing:
1. **Unified multi-objective framework** (trust, energy, QoS)
2. **Adaptive context fusion** (safety level, threat level, energy budget)
3. **Federated trust aggregation** (scalable to large networks)
4. **Heterogeneous topology support** (aerial, ground, sensors)
5. **Reproducible ablation mechanisms** (transparent measurement of each lever)

---

## 📚 Quick Start

### 1. Read the Proposal and the Quality Workflow
```bash
cd /home/madani/MARTHR
cat PROJECT_PROPOSAL.md          # High-level overview
cat LITERATURE_REVIEW.md         # Analysis of 7 recent papers
cat EXECUTION_PLAN.md            # Detailed phase-by-phase plan
cat conversation_opencode_vscode/CHECKLIST_REPRODUCTION.md
cat conversation_opencode_vscode/METHODOLOGIE_EVALUATION.md
```

### 2. Understand the Architecture
```
MARTHR = Multi-Criteria Score (MCS) + Federated Trust + RPL Integration

MCS = α·trust + β·energy + γ·qos

where α, β, γ are context-aware weights that adapt based on:
  - safety_level: critical | high | normal | best-effort
  - threat_level: high_attack | normal | low
  - energy_budget: critical | normal | sufficient
```

### 3. Project Structure

```
proposed_projet/
├── PROJECT_PROPOSAL.md          ← Start here (10-min overview)
├── LITERATURE_REVIEW.md         ← 7 recent papers (2026) analysis
├── EXECUTION_PLAN.md            ← Complete roadmap (A to Z)
├── code_source/                 ← Firmware (Contiki-NG)
│   ├── marthr_ocp.c / .h        ← Rank computation
│   ├── marthr_trust.c / .h      ← Trust management
│   ├── marthr_context.c / .h    ← Context fusion
│   ├── marthr_metric_log.c / .h ← Logging
│   ├── simulations/             ← Cooja simulation files
│   ├── tests/                   ← Unit tests
│   └── Makefile
├── data/
│   ├── raw/                     ← Cooja simulation logs
│   ├── estimated/               ← Parsed CSVs
│   └── README_DATA_PROVENANCE.md
├── scripts/
│   ├── regenerate_base_csvs.py  ← Log → CSV parser
│   ├── statistics/
│   │   └── compute_ablation_stats.py  ← Mann-Whitney tests
│   ├── generate_marthr_figures.py  ← CSV → PDF figures
│   └── figures_manifest.csv
├── manuscript/
│   ├── main.tex                 ← LaTeX manuscript
│   ├── sections/                ← Included .tex files
│   ├── Figures/                 ← PDF figures + captions
│   ├── tables/                  ← LaTeX tables
│   ├── bib/references.bib       ← Bibliography
│   └── main.pdf                 ← Compiled output
├── internal/
│   ├── PHASE1_ROADMAP.md        ← Detailed implementation steps
│   ├── METHODOLOGY_AUDIT.md     ← Verification workflow
│   ├── PROJECT_HEALTH_REPORT.md ← Build & test status
│   └── compile.sh               ← Build automation
├── requirements.txt             ← Python dependencies
├── BUILD_NOTES.txt              ← System setup guide
├── README.md                    ← This file
├── MASTER_TRACKER.md            ← High-level status
└── LICENSE                      ← GPL 3.0
```

---

## 🔬 Scientific Contributions

### 1. **MARTHR Protocol**
   - Formal MCS model with context-adaptive weights
   - Federated trust computation (no central authority)
   - RPL/MRHOF-compatible design
   - Energy-aware trust decay

### 2. **Empirical Evaluation**
   - 8 simulation scenarios (normal, attack, stress)
   - N ≥ 20 seeds for statistical power
   - Mann–Whitney U tests for significance
   - Ablation studies (A1–A3) showing individual lever contribution

### 3. **Reproducibility**
   - Open-source firmware (Contiki-NG)
   - CSV-to-PDF figure generation pipeline
   - Committed data + scripts (no re-running simulations needed)
   - Docker environment (optional)

---

## 📊 Key Differentiators vs. Recent Work

| Aspect | FANET Fuzzy | Tactical FL | OLSR Defense | Hybrid Sec | SDN MANET | DTN Disaster | **MARTHR** |
|--------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| Trust | ❌ | ❌ | ✅ (detect) | ✅ | ❌ | ❌ | ✅ |
| Energy | ❌ | ⚠️ | ❌ | ❌ | ❌ | ⚠️ | ✅ |
| QoS | ✅ | ❌ | ⚠️ | ❌ | ✅ | ⚠️ | ✅ |
| **All 3 unified** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | **✅** |
| Adaptive context | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ |
| Federated | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Heterogeneous | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Ablation studies | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | **✅** |

---

## 🛠️ Building the Project

### Phase 0: Setup (Week 1)
```bash
# 1. Clone or navigate to project
cd /home/madani/MARTHR

# 2. Install dependencies
pip install -r requirements.txt
apt-get install texlive-full latexmk  # LaTeX for manuscript

# 3. Verify Contiki-NG environment
cd code_source/
make clean
make TARGET=cooja LINK_FLAGS=-ffunction-sections
```

### Phase 1: Implementation (Weeks 2–4)
```bash
# 1. Implement firmware modules
# Edit: marthr_ocp.c, marthr_trust.c, marthr_context.c, marthr_metric_log.c

# 2. Run unit tests
make TARGET=cooja test

# 3. Compile firmware variants
make TARGET=cooja VARIANT=MARTHR_FULL
make TARGET=cooja VARIANT=MARTHR_TRUST_ONLY
```

### Phase 2–3: Simulation & Analysis (Weeks 5–8)
```bash
# 1. Run Cooja simulations (in GUI or batch mode)
java -Xmx2g -jar contiki/tools/cooja/dist/cooja.jar \
  -nogui simulations/25node_grid.csc -logdir=data/raw/

# 2. Parse logs to CSV
python3 scripts/regenerate_base_csvs.py \
  --input data/raw/ \
  --output data/estimated/

# 3. Compute statistics + ablation tests
python3 scripts/statistics/compute_ablation_stats.py \
  --input data/estimated/ \
  --output results/ablation_report.csv
```

### Phase 4: Figure Generation (Weeks 9–10)
```bash
# Generate all publication-quality figures
python3 scripts/generate_marthr_figures.py \
  --input data/estimated/ \
  --output manuscript/Figures/

# Build LaTeX manuscript
cd manuscript/
latexmk -pdf main.tex
```

### Phase 5: Manuscript (Weeks 11–15)
```bash
# Edit manuscript sections
vim sections/architecture.tex
vim sections/evaluation.tex

# Rebuild PDF
latexmk -pdf main.tex

# Verify reproducibility
./compile.sh              # Full build from scratch
```

---

## 📖 Documentation Structure

### Essential Reading Order
1. **PROJECT_PROPOSAL.md** (20 min)
   - Vision, contributions, success criteria
   
2. **LITERATURE_REVIEW.md** (30 min)
   - Analysis of 7 recent papers (June 2026)
   - Gap identification
   - Why MARTHR is novel

3. **EXECUTION_PLAN.md** (60 min)
   - Phase-by-phase roadmap
   - Deliverables per week
   - Timeline & resource planning

4. **ARCHITECTURE_SPEC.md** (40 min) — *to be created in Phase 1*
   - Formal MCS model
   - Trust aggregation protocol
   - RPL integration

5. **BUILD_NOTES.txt** (20 min)
   - System dependencies
   - Build troubleshooting
   - Environment setup

---

## 🚀 Key Milestones

| Week | Milestone | Status |
|------|-----------|--------|
| 1 | ✅ Project setup + documentation | **DONE** |
| 4 | 🔄 Firmware implementation + unit tests | In Progress |
| 6 | 🔄 Baseline data collection (N=4 seeds) | Pending |
| 8 | 🔄 Ablation studies (N=20 seeds) | Pending |
| 10 | 🔄 Figure generation + reproducibility | Pending |
| 13 | 🔄 Manuscript first draft | Pending |
| 14 | 🔄 Iteration & refinement | Pending |
| 15 | 🔄 Camera-ready submission | Pending |

---

## 🎓 Aligned with MARTHR Methodology

This project follows the proven workflow from the **MARTHR** project:

| Component | MARTHR | MARTHR |
|-----------|---------|--------|
| Firmware emission | `ids_campaign_log.c` METRIC | `marthr_metric_log.c` METRIC |
| Log parsing | `parse_cooja_ids_metrics.py` | `parse_marthr_metrics.py` |
| Statistics | `compute_statistics.py` | `compute_ablation_stats.py` |
| Figure generation | `generate_ids_figures.py` | `generate_marthr_figures.py` |
| Project structure | Multi-phase roadmap | Same approach |
| Reproducibility | CSV-driven pipeline | Same reproducibility model |

---

## 🔐 Reproducibility Guarantees

✅ **All figures regenerable from committed CSVs**
- No dependency on online services
- No randomness in figure generation
- Bit-exact PDF reproduction possible

✅ **Firmware builds deterministically**
- Version-locked dependencies (requirements.txt)
- Makefile with clean targets
- Docker environment (optional)

✅ **Statistical tests are transparent**
- Mann–Whitney U test implementation documented
- Effect sizes computed and reported
- p-values and confidence intervals included

✅ **Data provenance fully documented**
- Raw logs → parsed CSVs workflow explained
- Known caveats noted (e.g., simulation artifacts)
- Archive format and retention policy defined

---

## 📞 Support & Questions

### For Phase-Specific Questions
- **Phase 1 (Implementation):** See `EXECUTION_PLAN.md` Section 1
- **Phase 2 (Simulation):** See `EXECUTION_PLAN.md` Section 2
- **Phase 4 (Reproducibility):** See `scripts/regenerate_base_csvs.py`

### For Building/Troubleshooting
- **Build errors:** See `BUILD_NOTES.txt`
- **Cooja crashes:** Check `internal/PROJECT_HEALTH_REPORT.md`
- **Figure generation:** Check matplotlib version in `requirements.txt`

### For Methodology Questions
- **Protocol design:** See `ARCHITECTURE_SPEC.md` (Phase 1)
- **Evaluation approach:** See `EXECUTION_PLAN.md` Section 3–4
- **Statistical analysis:** See `scripts/statistics/compute_ablation_stats.py`

---

## 📋 License & Citation

**License:** GPL 3.0 (or your choice)

**If you use MARTHR in your research, please cite:**
```bibtex
@article{marthr2026,
  title={MARTHR: A Multi-Objective Trust-Aware Hierarchical Routing Protocol for Mobile Ad-Hoc Networks},
  author={Anonymous Authors},
  year={2026},
  journal={IEEE Transactions on Network Science and Engineering}
}
```

---

## 🎯 Next Steps

### Start Now (This Week)
1. [ ] Read PROJECT_PROPOSAL.md (10 min)
2. [ ] Skim LITERATURE_REVIEW.md (20 min)
3. [ ] Review EXECUTION_PLAN.md phases 0–1 (30 min)
4. [ ] Setup dependencies: `pip install -r requirements.txt`

### Begin Phase 1 (Week 2)
1. [ ] Write `ARCHITECTURE_SPEC.md` (formal MCS model)
2. [ ] Implement `marthr_ocp.c` (rank computation)
3. [ ] Create unit tests
4. [ ] Verify firmware compiles

### Full Timeline
See **EXECUTION_PLAN.md** for complete 15-week roadmap.

---

## 📞 Questions?

Refer to the comprehensive documentation:
- **High-level overview:** PROJECT_PROPOSAL.md
- **Literature context:** LITERATURE_REVIEW.md
- **Implementation guide:** EXECUTION_PLAN.md
- **Build troubleshooting:** BUILD_NOTES.txt
- **Reproducibility:** scripts/ folder + README_DATA_PROVENANCE.md

---

**Last Updated:** July 5, 2026  
**Project Status:** Phase 0 - Documentation Ready ✅  
**Next Review:** Before Phase 1 implementation (Week 2)

