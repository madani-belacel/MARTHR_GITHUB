# MARTHR PROJECT: Detailed Execution Plan
## From Concept to Reproducible Scientific Validation

**Project:** MARTHR: Context-Aware Trust-Energy-QoS Routing for MANETs  
**Start Date:** July 5, 2026  
**Minimum Realistic Execution Time:** 1 week for the first complete implementation cycle  
**Target Completion:** October 31, 2026  
**Target Venue:** IEEE/ACM networking venue (submission target: 2027)

## STRATEGIC ORIENTATION

The validation strategy is now explicitly centered on NS-3 because the primary goal is to produce a scientific evaluation that is general, reproducible, and comparable with the networking literature.

- **Primary validation platform:** NS-3
- **Secondary rapid prototyping:** Python-based logic validation and plotting
- **Optional legacy support:** Contiki/Cooja only if a later embedded or IoT-oriented proof is needed

### Main research objective
Develop and evaluate a context-aware routing protocol that jointly optimizes trust, energy, and QoS, then demonstrate its benefit through a statistically grounded NS-3 simulation campaign.

### Minimum project duration
This project is intentionally designed as a substantial research effort and not as a short exercise. Even the first usable implementation loop is planned to last at least one full week, with time reserved for setup, implementation, validation, documentation, and reproduction.

## METHODICAL HARDENING WORKFLOW (INSPIRED BY THE TEMPS CHECKLISTS)

To make the project more robust and publication-ready, the workflow now follows a stricter scientific audit loop:

1. **Artefact inventory**
   - Identify the manuscript, the simulation pipeline, the data sources, and the scripts that produce the figures.
   - Keep a direct link between each figure/table and its source dataset.

2. **Baseline verification**
   - Confirm that the Python environment, LaTeX toolchain, and any NS-3 dependencies are installed and runnable.
   - Execute the reproduction commands before claiming that the project is operational.

3. **Data and pipeline verification**
   - Inspect the raw CSV/log files to verify headers, units, missing values, and expected ranges.
   - Ensure that the analysis scripts consume the same data schema that is actually produced.

4. **Anomaly scan**
   - Search for placeholders, TODOs, synthetic fallbacks, or inconsistent labels in the code and manuscript.
   - Flag any mismatch between the documented methodology and the actual implementation.

5. **Correction and validation loop**
   - Fix the root cause rather than only the visible symptom.
   - Re-run the relevant scripts and the manuscript compilation after each correction.

6. **Final quality gates**
   - The manuscript must compile, the figures must be reproducible, the data provenance must be traceable, and the claims must be backed by real outputs.

**Project-specific deliverables:**
- [ ] A reproducible execution script for the full workflow
- [ ] A documented provenance trail from raw results to final figures
- [ ] A checklist of validation commands and expected outputs
- [ ] A clear audit of remaining scientific gaps before submission

---

## PHASE 0: PROJECT SETUP (Week 1)

### 0.1 Repository Structure & Documentation

**Tasks:**
- [x] Create directory hierarchy (code_source/, data/, scripts/, manuscript/, internal/)
- [x] Initialize version control (git init, .gitignore)
- [ ] Setup Docker environment for reproducibility
- [ ] Create initial README.md with project overview
- [ ] Document build dependencies (Contiki-NG, Python, LaTeX)

**Deliverable:** `BUILD_NOTES.txt` (system setup guide)

### 0.2 Dependencies & Toolchain Setup

**Required Software:**
```bash
# NS-3 environment
ns-3-dev or ns-3.40+    # Main simulator
cmake                   # Build system
gcc/g++                # C++ compiler
python3                # Simulation helpers

# Python for analysis
pandas>=1.3.0
numpy>=1.21.0
scipy>=1.7.0          # Statistical testing
matplotlib>=3.4.0     # Figure generation

# LaTeX for manuscript
texlive-full
latexmk
```

**Tasks:**
- [ ] Install and verify NS-3 build succeeds
- [ ] Run a basic NS-3 example to confirm the toolchain
- [ ] Setup Python virtual environment
- [ ] Install LaTeX packages
- [ ] Create a minimal NS-3 scratch script for MARTHR validation

**Deliverable:** `requirements.txt` + setup script

### 0.3 Team Synchronization & Collaboration

**Tasks:**
- [ ] Document communication channels (GitHub Issues, pull requests)
- [ ] Create MASTER_TRACKER.md for high-level status
- [ ] Define code review checklist
- [ ] Setup CI/CD for automated firmware builds (optional)

---

## PHASE 1: PROTOCOL DESIGN & FIRMWARE IMPLEMENTATION (Weeks 2–4)

### 1.1 Protocol Specification

**Tasks:**
- [ ] Write formal MCS model (math)
  - Multi-Criteria Score: `MCS = α·trust + β·energy + γ·qos`
  - Context-dependent weights: safety_level, threat_level
  - Hysteresis bounds to prevent rank oscillations
  
- [ ] Design federated trust aggregation protocol
  - TLV message format for trust gossip
  - Local trust computation rules
  - Trust decay model (time + energy)
  
- [ ] Define RPL Objective Function compatibility
  - Custom OCP number (e.g., OCP 9)
  - Integration with MRHOF hysteresis
  - Backward compatibility notes

**Deliverable:** `ARCHITECTURE_SPEC.md` (formal document)

**Reference:** Analogous to MARTHR's `ids_conf.h` + context_policy.c design

### 1.2 Firmware Skeleton Implementation

**Source Files to Create:**

```
code_source/
├── marthr_ocp.c / .h
│   - rank_computation(mcs, hysteresis, context)
│   - context_from_app_domain(safety_level, threat_level)
│   - weight_calculation(α_base, β_base, γ_base, safety_level, threat_level)
│
├── marthr_trust.c / .h
│   - node_trust_initialize()
│   - trust_update_from_success(node_id, link_quality)
│   - trust_update_from_failure(node_id)
│   - trust_decay(node_id, residual_energy, time_since_last_seen)
│   - federated_trust_aggregate(gossip_messages)
│
├── marthr_context.c / .h
│   - context_set_safety_level(level: critical|high|normal|best-effort)
│   - context_set_threat_level(level: high_attack_rate|normal|low)
│   - context_get_energy_budget(node_state)
│   - context_apply_weights(base_weights) → context_weights
│
├── marthr_metric_log.c / .h
│   - METRIC_OUTPUT() macro (like MARTHR's)
│   - Log: node_id, parent_id, rank, trust, energy, qos_latency, mcs_score
│
├── project-conf.h
│   - Enable MARTHR_OCP
│   - Disable default MRHOF
│   - Configure trust gossip interval
│   - Set logging flags
│
└── Makefile
    - Clean build for MARTHR variant
```

**Tasks:**
- [ ] Implement rank_computation() with hysteresis
- [ ] Implement trust update logic (success/failure)
- [ ] Implement context-aware weight adaptation
- [ ] Add METRIC logging (every rank update)
- [ ] Unit tests (create tests/unit_rank_test.c)

**Success Criteria:**
- Code compiles without warnings
- Unit tests pass (rank computation, context fusion)
- METRIC output format verified

**Deliverable:** Compilable firmware + unit test suite

**Reference:** MARTHR's `ids_campaign_log.c` as template

---

## PHASE 2: NS-3 IMPLEMENTATION AND SIMULATION CAMPAIGN (Weeks 5–8)

### 2.1 NS-3 Routing Module Development

**Tasks:**
- [ ] Create a dedicated NS-3 module for MARTHR under `src/marthr-routing/`
- [ ] Implement a custom routing protocol class that computes a route metric from:
  - trust score,
  - residual energy,
  - QoS proxy (e.g. delay or link quality)
- [ ] Add context-aware weight adaptation to the routing metric
- [ ] Implement trust decay and trust update rules
- [ ] Add trace sources for per-node metrics and route decisions
- [ ] Expose a simple scenario configuration interface for mobility, traffic, and attack settings

**Deliverable:** Compilable NS-3 module with a minimal working example

### 2.2 Simulation Scenarios for Scientific Evaluation

**Core scenarios:**
- [ ] Baseline mobility scenario: 50 nodes, random waypoint, 1000s, moderate traffic
- [ ] Density variation: 25, 50, and 100 nodes
- [ ] Mobility variation: low, medium, and high mobility
- [ ] Traffic load variation: low, medium, and high offered load
- [ ] Attack scenario: selective forwarding / packet dropping
- [ ] Energy stress scenario: heterogeneous energy budgets and node failures
- [ ] Adversarial trust scenario: malicious nodes attempting to inflate reputation

**Experiment design:**
- [ ] Use at least 20 random seeds per scenario for statistical robustness
- [ ] Keep identical topology and traffic settings across baseline and MARTHR runs
- [ ] Record raw traces in `data/raw/ns3/`

**Deliverable:** A fixed experiment matrix for reproducible evaluation

### 2.3 Baseline Protocols and Comparison Setup

**Baselines to compare against:**
- [ ] AODV
- [ ] DSR (optional, if supported and relevant)
- [ ] OLSR (optional, if the study needs a proactive baseline)

**Tasks:**
- [ ] Implement or reuse baseline routing protocols in NS-3
- [ ] Run all protocols under the same traffic and mobility settings
- [ ] Collect the same set of metrics for every protocol
- [ ] Archive outputs as CSV/JSON in `data/raw/ns3/`

**Metrics to collect:**
- [ ] Packet delivery ratio (PDR)
- [ ] End-to-end delay
- [ ] Routing overhead
- [ ] Energy consumption per delivered packet
- [ ] Route stability and convergence time
- [ ] Robustness under attack

**Deliverable:** Baseline and MARTHR result files ready for analysis

### 2.4 Reproducible Simulation Pipeline

**Tasks:**
- [ ] Create `scratch/marthr_ns3_sim.cc` for the main experiment campaign
- [ ] Add a parser script to convert NS-3 traces into CSV files
- [ ] Generate summary statistics per scenario and seed
- [ ] Ensure the pipeline can be rerun from a single command

**Success criteria:**
- [ ] NS-3 build completes without errors
- [ ] At least one full scenario runs end-to-end
- [ ] Raw outputs are converted into structured CSV datasets

**Deliverable:** Reproducible NS-3 simulation workflow

---

## PHASE 3: ABLATION STUDIES & STATISTICAL ANALYSIS (Weeks 7–8)

### 3.1 Extended Ablation Campaign

**Tasks:**
- [ ] Run ablations A1–A3 on lossy baseline scenario
- [ ] Increase N to 20 seeds (statistical power)
- [ ] Collect:
  - PDR (per-seed + aggregate statistics)
  - Latency (mean, p95, p99)
  - Energy (NRE evolution, lifetime)
  - Trust convergence time
  - Control overhead (RPL messages count)

**Deliverable:** `data/estimated/*_ablation_*.csv` (20 seeds each)

### 3.2 Statistical Analysis

**Tasks:**
- [ ] Implement Mann-Whitney U test script
  - Test: MARTHR-full vs. MRHOF for PDR (main hypothesis)
  - Test: MARTHR-trust vs. MARTHR-energy (ablation comparison)
  - Calculate p-values and effect sizes
  
- [ ] Generate descriptive stats tables
  - Mean ± std for each variant per scenario
  - Box plots per scenario showing seed variability
  
- [ ] Identify outlier seeds and investigate

**Deliverable:** `scripts/statistics/ablation_stats.csv` + statistical report

**Reference:** MARTHR's compute_statistics.py methodology

### 3.3 Attack Robustness Analysis

**Tasks:**
- [ ] Plot attack detection time vs. MRHOF detection time
- [ ] Calculate false positive rate (benign nodes flagged as attackers)
- [ ] Analyze how trust converges under sustained attacks
- [ ] Measure network partition time after attacker introduction

**Deliverable:** Attack analysis table + plots

---

## PHASE 4: FIGURE GENERATION & REPRODUCIBILITY (Weeks 9–10)

### 4.1 CSV Provenance & Figure Pipeline

**Tasks:**
- [ ] Document data flow: raw logs → parsed CSV → figures
- [ ] Create regeneration script: `scripts/regenerate_base_csvs.py`
  - Input: Cooja simulation logs from data/raw/
  - Parse MARTHR_METRIC_OUTPUT lines
  - Output: aggregated CSVs in data/estimated/
  - Handle: locale decimal formatting, multiple DET field layouts
  
- [ ] Create figure generation script: `scripts/generate_marthr_figures.py`
  - Input: data/estimated/*.csv
  - Output: PDF figures in manuscript/Figures/
  - Include matplotlib styling for publication-quality

**Deliverable:** Reproducible CSV-to-PDF pipeline (similar to MARTHR)

**Reference:** MARTHR's parse_cooja_ids_metrics.py + generate_ids_figures.py

### 4.2 Figure Catalog

**Figures to Generate (≥10):**

| Fig # | Title | Data Source | Key Metrics |
|-------|-------|-------------|-------------|
| 1 | MARTHR Architecture Diagram | Design doc | Component interaction |
| 2 | DODAG Example with Trust Coloring | Simulation | Trust levels per node |
| 3 | Context Weights (α, β, γ) per Domain | Config | Weight tuning strategy |
| 4 | PDR Comparison (MRHOF vs. MARTHR-full) | aggregated CSV | Main result |
| 5 | Latency Comparison (4 variants) | aggregated CSV | QoS metric |
| 6 | Per-class PDR (if multi-traffic) | aggregated CSV | QoS differentiation |
| 7 | Energy Proxy Comparison (NRE) | aggregated CSV | Energy efficiency |
| 8 | Control Overhead (RPL messages) | aggregated CSV | Scalability |
| 9 | Trust Convergence Time | trust convergence CSV | Adaptation speed |
| 10 | Ablation Study (A1 vs A2 vs A3) | ablation CSV | Contribution per lever |
| 11 | Pareto Frontier (Trust vs. Energy vs. PDR) | pareto CSV | Trade-off analysis |
| 12 | Attack Detection Rate | attack CSV | Security metric |

**Tasks:**
- [ ] Create matplotlib figure template (consistent styling)
- [ ] Implement data loading + error bars + significance markers
- [ ] Generate PDFs with embedded LaTeX (TikZ-style quality)

**Deliverable:** 12 publication-quality figures in `manuscript/Figures/`

### 4.3 Caption Refinement

**Tasks:**
- [ ] Write precise, journal-ready captions (80–150 words each)
- [ ] Ensure captions clearly state:
  - What is shown
  - Which metrics/variants compared
  - Key finding or interpretation limitation
  
- [ ] Create `manuscript/Figures/CAPTIONS_EN.tex`

**Reference:** AER-MQoS's caption refinement approach

---

## PHASE 5: MANUSCRIPT WRITING & COMPILATION (Weeks 11–13)

### 5.1 Manuscript Structure

**LaTeX Files:**

```
manuscript/
├── main.tex              # Main document + includes
├── abstract.tex          # 150 words
├── introduction.tex      # Background, motivation, RQs
├── related_work.tex      # Comparison with Pub 1–7 + others
├── architecture.tex      # MARTHR design, MCS model, trust protocol
├── evaluation.tex        # Methodology, scenarios, metrics
├── results.tex           # Baseline + ablation + attack results
├── discussion.tex        # Implications, limitations, future
├── conclusion.tex        # Summary + contributions
├── acknowledgments.tex   # Funding, support
├── Figures/
│   ├── CAPTIONS_EN.tex
│   └── Fig_*.pdf (12 figs)
├── tables/
│   ├── table_baseline.tex    # MRHOF baseline results
│   ├── table_ablation.tex    # A1–A3 statistics
│   ├── table_attacks.tex     # Attack robustness metrics
│   └── table_config.tex      # Simulation parameters
├── bib/
│   └── references.bib        # Citations (7 from lit review + others)
└── preamble.tex          # LaTeX configuration
```

### 5.2 Manuscript Content (First Draft)

**Tasks:**
- [ ] **Abstract** (150 words)
  - Problem: ad-hoc routing lacks unified trust+energy+QoS
  - Solution: MARTHR with federated trust + context adaptation
  - Result: 10% PDR improvement, < 15% energy overhead
  
- [ ] **Introduction** (1 page)
  - MANET/FANET use cases
  - Routing challenges (mobility, energy, security)
  - Motivation for multi-objective approach
  
- [ ] **Related Work** (1.5 pages)
  - Comparison table: this work vs. Pub 1–7
  - Highlight gaps (trust+energy+QoS, ablation, scalability)
  
- [ ] **Architecture** (2 pages)
  - MCS model + formal equations
  - Context-aware weight adaptation rules
  - Federated trust computation protocol
  - RPL/OCP integration
  
- [ ] **Evaluation** (2 pages)
  - Methodology: multiple NS-3 scenarios, N=20 seeds per condition
  - Metrics: PDR, latency, energy, control overhead, robustness under attack
  - Testbed: NS-3 with a custom MARTHR routing module
  
- [ ] **Results** (3 pages)
  - Baseline comparison (Figure 4)
  - Ablation studies (Figure 10)
  - Attack robustness (security results)
  - Statistical significance (p-values)
  
- [ ] **Discussion** (1.5 pages)
  - Key findings interpretation
  - Limitations (simulation-only, small N for some metrics)
  - Generalizability to real deployments
  
- [ ] **Conclusion** (0.5 pages)
  - Summary of contributions
  - Future work (real testbed, ML integration)

**Success Criteria:**
- 12–14 pages (IEEE two-column format)
- All figures referenced and explained
- Tables with statistics (mean ± std, p-values)

**Deliverable:** Manuscript first draft (PDF via latexmk)

### 5.3 LaTeX Compilation & Validation

**Tasks:**
- [ ] Setup preamble with IEEE template (if targeting IEEE)
- [ ] Verify all figures compile (no missing files)
- [ ] Check bibliography (BibTeX)
- [ ] Build PDF: `latexmk -pdf main.tex`
- [ ] Validate: no undefined references, overfull hboxes

**Deliverable:** `manuscript/main.pdf` (first draft)

**Reference:** AER-MQoS's latexmk workflow

---

## PHASE 6: ITERATION & REFINEMENT (Week 14)

### 6.1 Internal Review Checklist

**Verification:**
- [ ] All figures referenced in text
- [ ] All captions precise and descriptive
- [ ] All results tables match figures
- [ ] Grammar/spelling check
- [ ] LaTeX formatting consistent (font sizes, spacing)
- [ ] References complete (all 7 papers cited)

**Tasks:**
- [ ] Fix underfull/overfull boxes
- [ ] Adjust figure placements
- [ ] Refine wording for clarity
- [ ] Verify page limits

**Deliverable:** `manuscript/main.pdf` (refined)

### 6.2 Code Repository Cleanup

**Tasks:**
- [ ] Remove debug prints from firmware
- [ ] Add code comments (function headers, complex logic)
- [ ] Verify Makefile clean build
- [ ] Create .gitignore (exclude build artifacts)
- [ ] Document build instructions

**Deliverable:** Clean code_source/ folder

### 6.3 Data Archive & Documentation

**Tasks:**
- [ ] Document raw log format (MARTHR_METRIC output)
- [ ] Create README_DATA_PROVENANCE.md
  - Raw data location
  - CSV generation workflow
  - Known caveats (e.g., smoke-test artefacts)
  
- [ ] Commit all CSVs (frozen for reproducibility)
- [ ] Create DATA_MANIFEST.csv (list all files + row counts)

**Deliverable:** `data/README_DATA_PROVENANCE.md` + manifest

**Reference:** AER-MQoS's data provenance approach

---

## PHASE 7: FINAL PACKAGING & SUBMISSION (Week 15)

### 7.1 Public Deliverables

**Create:**
- [ ] `README.md` (public-facing guide)
- [ ] `BUILD_NOTES.txt` (setup instructions)
- [ ] `LICENSE` (GPL 3.0 or MIT)
- [ ] `requirements.txt` (dependencies)
- [ ] `MASTER_TRACKER.md` (project status summary)

**Tasks:**
- [ ] Verify Docker build (if using)
- [ ] Test cloned repo can reproduce figures
- [ ] Validate open-source licenses

**Deliverable:** Publication-ready repository

### 7.2 Manuscript Finalization

**Tasks:**
- [ ] Camera-ready PDF (embedded fonts, high resolution figures)
- [ ] Verify 12–14 page limit
- [ ] Final language review
- [ ] Create submission package (PDF + source files)

**Deliverable:** `manuscript/main_camera_ready.pdf` + submission files

### 7.3 Venue Submission

**Target Venues (in order of preference):**
1. **IEEE Infocom 2027** (Deadline: ~Dec 2026)
2. **ACM MobiSys 2027** (Deadline: ~Jan 2027)
3. **IEEE/ACM ToN** (Top journal, rolling submission)

**Tasks:**
- [ ] Review venue guidelines (page limits, formatting)
- [ ] Prepare author information
- [ ] Submit via conference portal

**Deliverable:** Submission confirmation

---

## SUCCESS METRICS (End-to-End)

### Quantitative
1. ✅ Firmware compiles without warnings
2. ✅ Unit tests pass (100% coverage)
3. ✅ PDR improvement ≥ 5% over MRHOF (with p < 0.05)
4. ✅ Energy overhead ≤ 15% in normal scenarios
5. ✅ Trust convergence < 30 seconds
6. ✅ All figures regenerable from committed CSVs
7. ✅ Manuscript 12–14 pages
8. ✅ No undefined references in LaTeX

### Qualitative
1. ✅ Clear architecture documentation
2. ✅ Reproducible pipeline (README + scripts)
3. ✅ Open-source code available
4. ✅ Clean, well-commented firmware
5. ✅ Peer-reviewed publication (target: 2027)

---

## RISK MITIGATION

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| Cooja crashes on large topologies | Medium | High | Reduce N nodes, use parallel simulations |
| Trust convergence too slow | Medium | High | Tune gossip interval, reduce threshold |
| Energy overhead unexpectedly high | Low | Medium | Profile CPU + radio usage, optimize compute |
| Manuscript exceeds page limit | High | Low | Cut Discussion section, move details to tech report |
| Figures not reproducible from CSVs | Low | Critical | Version-lock scripts + dependencies, test early |

---

## TIMELINE SUMMARY

```
Week 1:   Phase 0 - Setup
Weeks 2–4: Phase 1 - Design & Implementation
Weeks 5–6: Phase 2 - Baseline Collection
Weeks 7–8: Phase 3 - Ablation & Analysis
Weeks 9–10: Phase 4 - Figures & Reproducibility
Weeks 11–13: Phase 5 - Manuscript Writing
Week 14:  Phase 6 - Iteration & Refinement
Week 15:  Phase 7 - Final Packaging & Submission

Total: 15 weeks (~4 months)
Target Submission: October 31, 2026
```

---

## KEY REFERENCES (Analogous to MARTHR)

| Task | MARTHR Reference | MARTHR Application |
|------|----------|----------|
| Firmware METRIC emission | `ids_campaign_log.c` | `marthr_metric_log.c` |
| CSV parsing + processing | `parse_cooja_ids_metrics.py` | `parse_marthr_metrics.py` |
| Statistics computation | `compute_statistics.py` | `compute_ablation_stats.py` |
| Figure generation | `generate_ids_figures.py` | `generate_marthr_figures.py` |
| Project structure | `MARTHR/` layout | Replicate in `proposed_projet/` |
| Reproducibility approach | MARTHR_publish_ready/ | Local sanitized copy strategy |

---

**Document Version:** 1.0  
**Last Updated:** July 5, 2026  
**Next Review:** Before Phase 1 implementation

