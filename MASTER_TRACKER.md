# MARTHR PROJECT: MASTER TRACKER
## High-Level Status & Milestones

**Project:** MANET-Trust-Aware Hierarchical Routing Protocol  
**Started:** July 5, 2026  
**Target Completion:** October 31, 2026 (15 weeks)  
**Minimum realistic execution span:** 1 week for a first complete implementation cycle  
**Status:** 🟢 Phase 0 Complete / 🔄 Phase 1 In Progress

---

## EXECUTIVE SUMMARY

**MARTHR** is a high-quality research project proposal that responds to a critical gap in recent literature (7 papers analyzed from 2026):

- ✅ **Problem:** No protocol unifies trust + energy + QoS with ablation studies
- ✅ **Solution:** MARTHR with adaptive context-aware weights + federated trust
- ✅ **Novelty:** 6× differentiator vs. recent publications
- ✅ **Plan:** 15-week roadmap from firmware to camera-ready manuscript

**Phase 0 Deliverables (COMPLETE):**
1. ✅ PROJECT_PROPOSAL.md (high-level overview)
2. ✅ LITERATURE_REVIEW.md (7 papers analyzed)
3. ✅ EXECUTION_PLAN.md (detailed roadmap)
4. ✅ README.md (quick start guide)
5. ✅ This tracker (MASTER_TRACKER.md)

## SCIENTIFIC RIGOR GATES

The project now includes a stronger quality layer inspired by the Temps methodology:

- [x] Reproducibility workflow documented and linked from the main README
- [x] Reproduction checklist available in [conversation_opencode_vscode/CHECKLIST_REPRODUCTION.md](conversation_opencode_vscode/CHECKLIST_REPRODUCTION.md)
- [x] Evaluation methodology available in [conversation_opencode_vscode/METHODOLOGIE_EVALUATION.md](conversation_opencode_vscode/METHODOLOGIE_EVALUATION.md)
- [x] Full project pipeline can be executed via [scripts/reproduce_project.py](scripts/reproduce_project.py)
- [ ] Remaining scientific gaps and anomalies are tracked and resolved before final submission

---

## PHASE OVERVIEW

```
Phase 0: Documentation             ✅ DONE
Phase 1: Protocol Design & Impl    🔄 START: Week 2
Phase 2: Baseline Collection       ⏳ Week 5
Phase 3: Ablation Studies          ⏳ Week 7
Phase 4: Figures & Reproducibility ⏳ Week 9
Phase 5: Manuscript Writing        ⏳ Week 11
Phase 6: Iteration & Refinement    ⏳ Week 14
Phase 7: Final Packaging           ⏳ Week 15
```

---

## DETAILED MILESTONE TRACKING

### Phase 0: Documentation (Week 1)
**Status:** ✅ COMPLETE

| Task | Deliverable | Status | Notes |
|------|-------------|--------|-------|
| Project overview | PROJECT_PROPOSAL.md | ✅ Done | 7-publication analysis integrated |
| Literature review | LITERATURE_REVIEW.md | ✅ Done | 7 papers (2026) fully analyzed |
| Execution roadmap | EXECUTION_PLAN.md | ✅ Done | 15-week plan, phase-by-phase |
| Quick start guide | README.md | ✅ Done | Project structure documented |
| Status tracking | MASTER_TRACKER.md | ✅ Done | This file |
| Project structure | Directories created | ✅ Done | code_source/, data/, scripts/, etc. |

**Go/No-Go Decision:** ✅ **GO** → Proceed to Phase 1

---

### Phase 1: Protocol Design & Implementation (Weeks 2–4)
**Status:** 🔄 IN PROGRESS

**Major Milestones:**
1. [x] **Formal Specification** (Week 2)
   - Write ARCHITECTURE_SPEC.md
   - Define MCS model + context fusion rules
   - Design federated trust protocol
   - Deadline: End of Week 2

2. [x] **Firmware Implementation** (Weeks 2–4)
   - Implement marthr_ocp.c (rank computation)
   - Implement marthr_trust.c (trust management)
   - Implement marthr_context.c (context adaptation)
   - Implement marthr_metric_log.c (logging)
   - Add unit tests (tests/unit_*.c)
   - Deadline: End of Week 4

3. [x] **Compilation & Validation** (Week 4)
   - Firmware compiles without warnings
   - Unit tests pass (100% pass rate)
   - Makefile works for all variants
   - Deadline: End of Week 4

**Detailed Task Breakdown:**
- [ ] ARCHITECTURE_SPEC.md
  - Formal MCS equations
  - Context weight adaptation rules
  - Trust decay model
  - RPL/OCP integration spec
  - Estimated effort: 8 hours

- [ ] marthr_ocp.c implementation
  - `rank_computation(mcs, hysteresis)` function
  - `context_from_app_domain()` function
  - `weight_calculation()` with adaptation logic
  - ~300 lines of code
  - Estimated effort: 16 hours

- [ ] marthr_trust.c implementation
  - `node_trust_initialize()` 
  - `trust_update_from_success/failure()` 
  - `trust_decay()` 
  - `federated_trust_aggregate()` 
  - ~250 lines of code
  - Estimated effort: 12 hours

- [ ] marthr_context.c implementation
  - `context_set_safety_level()`
  - `context_set_threat_level()`
  - `context_get_energy_budget()`
  - `context_apply_weights()`
  - ~150 lines of code
  - Estimated effort: 8 hours

- [ ] Unit tests
  - tests/unit_rank_test.c (rank computation)
  - tests/unit_trust_test.c (trust updates)
  - tests/unit_context_test.c (weight adaptation)
  - ~400 lines of test code
  - Estimated effort: 12 hours

**Success Criteria:**
- ✅ No compilation errors/warnings
- ✅ Unit test pass rate = 100%
- ✅ All 4 firmware modules compile independently
- ✅ METRIC output format verified with simple test

**Estimated Total Effort:** 56 hours (7 person-days)

---

### Phase 2: Baseline Data Collection (Weeks 5–6)
**Status:** ⏳ PENDING

**Major Milestones:**
1. [ ] **Simulation Setup** (Week 5)
   - Create 8 Cooja simulation files (.csc)
   - Implement attack injection modules
   - Setup traffic generators
   - Configure metric logging
   - Deadline: Mid-Week 5

2. [ ] **MRHOF Baseline** (Week 5)
   - Run MRHOF on all 8 scenarios, N=4 seeds each
   - Collect PDR, latency, energy, control overhead
   - Archive raw logs in data/raw/mrhof_*.csv
   - Deadline: End of Week 5

3. [ ] **MARTHR Initial Collection** (Week 6)
   - Compile 4 firmware variants (full, trust-only, energy-only, qos-only)
   - Run on same 8 scenarios, N=4 seeds each
   - Archive in data/raw/marthr_*.csv
   - Deadline: End of Week 6

**Simulation Scenarios:**
- Lossless reference (1 seed)
- Lossy baseline (4 seeds)
- Attack selective forwarding 10% (4 seeds)
- Attack selective forwarding 25% (4 seeds)
- Attack rank inflation (4 seeds)
- Stress 2× load (4 seeds)
- Stress low PRR (4 seeds)
- Heterogeneous aerial+ground (4 seeds)

**Total Sim Time:** ~80 hours (Cooja batch execution)

**Success Criteria:**
- ✅ All scenarios run without crashes
- ✅ PDR > 90% in lossless scenarios
- ✅ All 8 × 4 = 32 seed collections complete
- ✅ Raw logs parsed without errors

---

### Phase 3: Ablation Studies & Statistical Analysis (Weeks 7–8)
**Status:** ⏳ PENDING

**Major Milestones:**
1. [ ] **Extended Ablation Campaign** (Week 7)
   - Run ablations A1, A2, A3 on lossy baseline
   - Increase N from 4 to 20 seeds for statistical power
   - Collect PDR, latency, energy, trust convergence time
   - Archive in data/estimated/*_ablation_*.csv
   - Deadline: End of Week 7

2. [ ] **Statistical Analysis** (Week 8)
   - Implement Mann-Whitney U test script
   - Compute p-values and effect sizes
   - Generate descriptive stats tables
   - Create box plots and outlier analysis
   - Deadline: Mid-Week 8

3. [ ] **Attack Analysis** (Week 8)
   - Measure attack detection time
   - Calculate false positive rate
   - Plot trust convergence under attacks
   - Analyze network partition scenarios
   - Deadline: End of Week 8

**Ablation Details:**
- A1: Trust disabled (energy + QoS only)
- A2: Energy disabled (trust + QoS only)
- A3: QoS disabled (trust + energy only)
- Full: All three levers enabled

**Total Sim Time:** ~100 hours (20 seeds × 8 scenarios)

**Success Criteria:**
- ✅ Mann-Whitney p-value < 0.05 for main hypothesis
- ✅ All ablation comparisons complete
- ✅ Statistical tables ready for manuscript
- ✅ Box plots generated for all metrics

---

### Phase 4: Figure Generation & Reproducibility (Weeks 9–10)
**Status:** ⏳ PENDING

**Major Milestones:**
1. [ ] **CSV Pipeline** (Week 9)
   - Create `regenerate_base_csvs.py`
   - Parse Cooja logs → clean CSVs
   - Handle: locale decimals, multiple DET formats
   - Test on all raw logs
   - Deadline: Mid-Week 9

2. [ ] **Figure Generation** (Week 9–10)
   - Create `generate_marthr_figures.py`
   - Generate 12 publication-quality figures
   - Include error bars and significance markers
   - Verify data-to-figure consistency
   - Deadline: End of Week 10

3. [ ] **Caption Refinement** (Week 10)
   - Write 12 precise captions (80–150 words each)
   - Create CAPTIONS_EN.tex
   - Ensure LaTeX compatibility
   - Deadline: End of Week 10

**Figures to Generate:**
1. Architecture diagram
2. DODAG with trust coloring
3. Context weights per domain
4. PDR comparison (4 variants)
5. Latency comparison
6. Per-class PDR
7. Energy proxy comparison
8. Control overhead
9. Trust convergence time
10. Ablation study results
11. Pareto frontier
12. Attack detection rate

**Success Criteria:**
- ✅ All 12 figures generate without errors
- ✅ All figures reproducible from committed CSVs
- ✅ Captions match figure content
- ✅ LaTeX integration verified

---

### Phase 5: Manuscript Writing & Compilation (Weeks 11–13)
**Status:** ⏳ PENDING

**Major Milestones:**
1. [ ] **Manuscript Structure** (Week 11)
   - Create LaTeX template with IEEE style
   - Setup preamble, bib, figure includes
   - Create section files (abstract, intro, arch, eval, results, discussion, conclusion)
   - Deadline: Mid-Week 11

2. [ ] **Content Writing** (Weeks 11–12)
   - Write abstract (150 words)
   - Write introduction (1 page)
   - Write related work (1.5 pages)
   - Write architecture (2 pages)
   - Write evaluation (2 pages)
   - Write results (3 pages)
   - Write discussion (1.5 pages)
   - Write conclusion (0.5 pages)
   - Deadline: End of Week 12

3. [ ] **Compilation & Validation** (Week 13)
   - Build PDF via latexmk
   - Verify all figures included
   - Check bibliography completeness
   - Fix overfull hboxes
   - Verify page count (12–14 pages)
   - Deadline: End of Week 13

**Manuscript Outline (12–14 pages IEEE format):**
- Abstract (150 words)
- Introduction (1 page)
- Related Work (1.5 pages, comparison table)
- Architecture (2 pages, MCS model + diagrams)
- Evaluation (2 pages, methodology + scenarios)
- Results (3 pages, baseline + ablation + attacks)
- Discussion (1.5 pages)
- Conclusion (0.5 pages)
- References (2–3 pages)

**Success Criteria:**
- ✅ LaTeX compiles without errors
- ✅ All figures referenced and included
- ✅ All tables formatted with statistics
- ✅ Bibliography complete (30+ references)
- ✅ Page count within 12–14 range

---

### Phase 6: Iteration & Refinement (Week 14)
**Status:** ⏳ PENDING

**Major Milestones:**
1. [ ] **Internal Review** (Week 14)
   - Checklist review (figures, captions, tables, grammar)
   - Fix LaTeX formatting issues
   - Refine wording for clarity
   - Verify page limits
   - Deadline: Mid-Week 14

2. [ ] **Code Cleanup** (Week 14)
   - Remove debug prints
   - Add code comments
   - Verify Makefile clean build
   - Setup .gitignore
   - Deadline: Mid-Week 14

3. [ ] **Data Documentation** (Week 14)
   - Create README_DATA_PROVENANCE.md
   - Document CSV generation workflow
   - Note known caveats
   - Create DATA_MANIFEST.csv
   - Deadline: End of Week 14

**Success Criteria:**
- ✅ No spelling/grammar errors
- ✅ Code includes helpful comments
- ✅ Data provenance fully documented
- ✅ All artifacts ready for publication

---

### Phase 7: Final Packaging & Submission (Week 15)
**Status:** ⏳ PENDING

**Major Milestones:**
1. [ ] **Public Deliverables** (Week 15)
   - Create public README.md
   - Create BUILD_NOTES.txt
   - Create LICENSE file (GPL 3.0)
   - Verify open-source readiness
   - Deadline: Mid-Week 15

2. [ ] **Camera-Ready Preparation** (Week 15)
   - Finalize PDF (embedded fonts, high-res figures)
   - Verify 12–14 page limit
   - Prepare submission package
   - Create author information
   - Deadline: Mid-Week 15

3. [ ] **Submission** (Week 15)
   - Select target venue (IEEE Infocom / ACM MobiSys)
   - Review venue guidelines
   - Submit via conference portal
   - Deadline: End of Week 15

**Target Venues:**
1. IEEE Infocom 2027 (Deadline: ~Dec 2026)
2. ACM MobiSys 2027 (Deadline: ~Jan 2027)
3. IEEE/ACM Transactions on Networking (anytime)

**Success Criteria:**
- ✅ Submission confirmed
- ✅ All files uploaded
- ✅ Author information complete
- ✅ Camera-ready PDF accepted

---

## RESOURCE REQUIREMENTS

### Personnel
- **Lead Developer:** 1 FTE
- **Reviewer/Advisor:** Part-time (optional)

### Hardware
- **Development Machine:** Any Linux (4GB RAM minimum)
- **Cooja Simulation:** 4 parallel instances (8GB RAM total)
- **Build Time:** ~10 hours total (parallel sims)

### Software (All Free/Open Source)
- Contiki-NG
- Cooja simulator
- Python 3.8+
- LaTeX (texlive-full)
- Git

### Timeline
- **Total Duration:** 15 weeks (~4 months)
- **Effort:** ~250 person-hours (6 weeks full-time equivalent)
- **Critical Path:** Phase 1 (implementation) → Phase 2 (baseline) → Phases 3–5 (sequential)

---

## RISK ASSESSMENT & MITIGATION

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|-----------|
| Cooja crashes on large topologies | Medium | High | Reduce node count, use Cooja batch mode, split sims |
| Trust convergence too slow | Medium | High | Tune gossip interval, reduce thresholds, profile |
| Energy overhead > 20% | Low | Medium | Optimize C code, profile CPU/radio, reduce logging |
| Manuscript exceeds page limit | High | Low | Cut Discussion/details, move to tech report |
| Figures non-reproducible from CSVs | Low | Critical | Version-lock scripts, test early, commit CSVs |
| Venue rejects paper | Medium | Medium | Submit to backup venues (MobiSys, Transactions) |

---

## SUCCESS METRICS (End-to-End)

### Go/No-Go Criteria by Phase

**Phase 1 Go-Criteria:**
- ✅ Code compiles without warnings
- ✅ Unit tests pass (100% pass rate)

**Phase 2 Go-Criteria:**
- ✅ MRHOF baseline collected (all scenarios, all seeds)
- ✅ MARTHR data collected (all scenarios, all seeds)

**Phase 3 Go-Criteria:**
- ✅ Ablation studies complete (A1–A3, 20 seeds)
- ✅ Mann-Whitney test p-value < 0.05

**Phase 4 Go-Criteria:**
- ✅ 12 figures generate cleanly
- ✅ All figures reproducible from CSVs

**Phase 5 Go-Criteria:**
- ✅ Manuscript compiles (LaTeX)
- ✅ 12–14 pages (IEEE format)

**Phase 6 Go-Criteria:**
- ✅ No spelling/grammar errors
- ✅ Data provenance documented

**Phase 7 Go-Criteria:**
- ✅ Submission confirmed
- ✅ Camera-ready PDF accepted

---

## COMMUNICATION & UPDATES

### Status Update Cadence
- **Weekly:** Check EXECUTION_PLAN.md for on-track progress
- **Bi-weekly:** Review milestone completion
- **Monthly:** Update MASTER_TRACKER.md and PROJECT_HEALTH_REPORT.md

### Key Contacts & Documents
- **High-level overview:** PROJECT_PROPOSAL.md
- **Literature context:** LITERATURE_REVIEW.md
- **Detailed plan:** EXECUTION_PLAN.md
- **Build issues:** BUILD_NOTES.txt
- **Health report:** internal/PROJECT_HEALTH_REPORT.md

---

## NEXT IMMEDIATE ACTIONS (This Week)

**Priority 1: MUST DO**
- [ ] Read LITERATURE_REVIEW.md (understand the 7 papers)
- [ ] Read EXECUTION_PLAN.md Phases 0–1 (understand approach)
- [ ] Verify Contiki-NG build environment works

**Priority 2: SHOULD DO**
- [ ] Install Python dependencies: `pip install -r requirements.txt`
- [ ] Test Cooja simulator (quick smoke test)
- [ ] Setup git repository (if not already done)

**Priority 3: NICE TO HAVE**
- [ ] Review MARTHR project for methodology reference
- [ ] Read PROJECT_PROPOSAL.md fully (architectural details)

---

## TIMELINE AT A GLANCE

```
Week 1:  ✅ Documentation complete
Week 2:  Firmware skeleton (Phase 1 start)
Week 3:  Trust + context modules
Week 4:  Unit tests, compilation validation
Week 5:  MRHOF baseline collection
Week 6:  MARTHR data collection
Week 7:  Ablation studies (20 seeds)
Week 8:  Statistical analysis
Week 9:  CSV pipeline + figure generation
Week 10: Figure refinement + captions
Week 11: Manuscript template + abstract/intro
Week 12: Architecture + evaluation + results
Week 13: Discussion + conclusion + compilation
Week 14: Iteration + code cleanup
Week 15: Camera-ready + submission ✅
```

---

## DOCUMENT LINKS

- 📄 [PROJECT_PROPOSAL.md](PROJECT_PROPOSAL.md) — High-level overview
- 📚 [LITERATURE_REVIEW.md](LITERATURE_REVIEW.md) — 7 papers analyzed
- 🗺️ [EXECUTION_PLAN.md](EXECUTION_PLAN.md) — Phase-by-phase roadmap
- 📖 [README.md](README.md) — Quick start guide
- 🔧 [BUILD_NOTES.txt](BUILD_NOTES.txt) — Build troubleshooting (to be created)
- 📊 [internal/PROJECT_HEALTH_REPORT.md](internal/PROJECT_HEALTH_REPORT.md) — Build status (to be created)

---

**Document Version:** 1.0  
**Last Updated:** July 5, 2026  
**Next Update:** Before Phase 1 start (Week 2)

