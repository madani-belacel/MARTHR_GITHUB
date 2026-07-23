# MARTHR PROJECT: COMPLETE DOCUMENTATION INDEX

**Project:** MANET-Trust-Aware Hierarchical Routing Protocol  
**Created:** July 5, 2026  
**Status:** Phase 0 Complete – Ready for Phase 1 Implementation

---

## 📚 DOCUMENT HIERARCHY

### 🔴 MUST READ (Start With These)

**1. QUICK_START_CHECKLIST.md** (5 min)
   - What is MARTHR? (30-second version)
   - Why is it novel? (vs. 7 papers)
   - Which document to read next
   - Quick checklist before Phase 1

**2. PROJECT_PROPOSAL.md** (20 min)
   - High-level overview of the project
   - 4 core innovations
   - Scientific contributions
   - Success criteria
   - 15-week roadmap overview
   - **Key sections:**
     - Section 3: "Proposed Contributions"
     - Section 4: "Project Roadmap"
     - Section 7: "Success Criteria"

**3. LITERATURE_REVIEW.md** (30 min)
   - Deep analysis of 7 papers (2026)
   - Comparative analysis table
   - Research gaps identified
   - Why MARTHR is novel
   - **Key sections:**
     - Section 2: Publication summaries
     - Section 3: Comparative analysis
     - Section 4: Research gaps
     - Section 5: Opportunities for MARTHR

### 🟡 SHOULD READ (Essential for Implementation)

**4. EXECUTION_PLAN.md** (60 min)
   - Phase-by-phase detailed roadmap
   - Week-by-week breakdown
   - Specific deliverables per phase
   - Resource requirements
   - Risk assessment
   - Success metrics by phase
   - **Key sections:**
     - Phase 1: Protocol Design & Implementation
     - Phase 2: Baseline Collection
     - Phase 3: Ablation Studies
     - Phase 4: Figures & Reproducibility

**5. README.md** (20 min)
   - Project structure
   - Quick start guide
   - Architecture overview
   - Key differentiators vs. prior work
   - Building the project (step-by-step)
   - Documentation reading order

**6. MASTER_TRACKER.md** (20 min)
   - High-level status dashboard
   - Phase overview
   - Detailed milestone tracking
   - Resource requirements
   - Risk assessment & mitigation
   - Success metrics per phase
   - **For:** Tracking progress, identifying blockers

### 🟢 REFERENCE (Consult As Needed)

**7. BUILD_NOTES.txt** (to be created in Phase 1)
   - System dependencies
   - Build troubleshooting
   - Environment setup
   - Common errors & solutions

**8. internal/PROJECT_HEALTH_REPORT.md** (to be created)
   - Build status
   - Test results
   - Known issues
   - Performance metrics
   - Updated weekly

**9. internal/PHASE1_ROADMAP.md** (to be created in Phase 1)
   - Detailed firmware implementation steps
   - File-by-file breakdown
   - Function signatures
   - Test plan

**10. scripts/regenerate_base_csvs.py** (Phase 4)
   - CSV generation from Cooja logs
   - Locale handling
   - Data validation

**11. scripts/generate_marthr_figures.py** (Phase 4)
   - Figure generation from CSVs
   - Matplotlib configuration
   - Error bar computation

**12. data/README_DATA_PROVENANCE.md** (Phase 6)
   - Data flow: logs → CSVs → figures
   - Known caveats
   - Archive format

---

## 📖 READING PATHS BY ROLE

### For Project Manager / Decision Maker (30 min)
1. ✅ QUICK_START_CHECKLIST.md
2. ✅ PROJECT_PROPOSAL.md (Sections 1, 3, 7)
3. ✅ MASTER_TRACKER.md (Timeline + Go/No-Go criteria)

**Outcome:** Understand project scope, timeline, and risks.

### For Firmware Developer (2 hours)
1. ✅ QUICK_START_CHECKLIST.md
2. ✅ PROJECT_PROPOSAL.md (All sections)
3. ✅ LITERATURE_REVIEW.md (Gap sections 4–5)
4. ✅ EXECUTION_PLAN.md (Phase 1)
5. ✅ README.md (Building section)
6. 🔄 internal/PHASE1_ROADMAP.md (when available, Phase 1)

**Outcome:** Ready to implement marthr_ocp.c, marthr_trust.c, etc.

### For Data Analyst / Statistician (1.5 hours)
1. ✅ QUICK_START_CHECKLIST.md
2. ✅ PROJECT_PROPOSAL.md (Section 4, ablation studies)
3. ✅ LITERATURE_REVIEW.md (All)
4. ✅ EXECUTION_PLAN.md (Phases 3–4)
5. 🔄 scripts/statistics/compute_ablation_stats.py (when available, Phase 3)

**Outcome:** Ready to analyze simulation results and generate figures.

### For PhD/Researcher (Full understanding, 4 hours)
1. ✅ Read all documents in order (Sections 🔴 + 🟡 + relevant 🟢)
2. ✅ Understand complete methodology
3. 🔄 Implement end-to-end (all phases)

**Outcome:** Full ownership of project and publications.

---

## 🗺️ DOCUMENT-TO-PHASE MAPPING

| Phase | Duration | Key Documents | Primary Owner |
|-------|----------|---|---|
| **Phase 0: Documentation** | Week 1 | All 🔴 + 🟡 docs | Everyone |
| **Phase 1: Design & Impl** | Weeks 2–4 | EXECUTION_PLAN.md (Sec 1), PHASE1_ROADMAP.md | Firmware Dev |
| **Phase 2: Baseline** | Weeks 5–6 | EXECUTION_PLAN.md (Sec 2), simulation specs | DevOps |
| **Phase 3: Ablation** | Weeks 7–8 | EXECUTION_PLAN.md (Sec 3), stats scripts | Data Analyst |
| **Phase 4: Figures** | Weeks 9–10 | EXECUTION_PLAN.md (Sec 4), Python scripts | Data Analyst |
| **Phase 5: Manuscript** | Weeks 11–13 | EXECUTION_PLAN.md (Sec 5), LaTeX | Writer/Researcher |
| **Phase 6: Iteration** | Week 14 | PROJECT_HEALTH_REPORT.md | Everyone |
| **Phase 7: Submission** | Week 15 | README.md, LICENSE | PM |

---

## 🔄 DOCUMENT CROSS-REFERENCES

### "I want to understand the MCS model"
1. PROJECT_PROPOSAL.md → Section 3 (Proposed Contributions)
2. LITERATURE_REVIEW.md → Section 5 (Opportunities for MARTHR)
3. EXECUTION_PLAN.md → Phase 1, Task 1.1 (Protocol Specification)
4. Later: internal/ARCHITECTURE_SPEC.md (Phase 1 output)

### "I want to understand the ablation studies"
1. PROJECT_PROPOSAL.md → Section 3.3 (Ablation Studies)
2. EXECUTION_PLAN.md → Phase 3 (Ablation Studies & Analysis)
3. Later: scripts/statistics/compute_ablation_stats.py

### "I want to see the timeline"
1. PROJECT_PROPOSAL.md → Section 4 (Project Roadmap)
2. EXECUTION_PLAN.md → Full document (phases 0–7)
3. MASTER_TRACKER.md → Timeline section
4. README.md → Next Steps

### "I want to reproduce the figures"
1. README.md → Building the project (Phase 4 section)
2. EXECUTION_PLAN.md → Phase 4 (Figure Generation)
3. scripts/regenerate_base_csvs.py (implementation)
4. scripts/generate_marthr_figures.py (implementation)
5. data/README_DATA_PROVENANCE.md (documentation)

### "I want to submit the paper"
1. PROJECT_PROPOSAL.md → Success Criteria (Section 7)
2. EXECUTION_PLAN.md → Phase 7 (Final Packaging & Submission)
3. README.md → License & Citation
4. manuscript/main.pdf (output)

---

## 📊 CONTENT SUMMARY

### Documentation Volume
| Category | Documents | Total Pages (est.) |
|----------|-----------|----------|
| Planning | 6 documents | ~40 pages |
| Implementation | Phase 1 code specs | ~20 pages |
| Analysis | Statistics + figures | ~15 pages |
| Manuscript | LaTeX source | ~30 pages |
| **Total** | | **~100+ pages** |

### Key Concepts Covered
- ✅ Trust-aware routing protocols
- ✅ Multi-objective optimization (trust + energy + QoS)
- ✅ Federated trust aggregation
- ✅ Context-adaptive parameter tuning
- ✅ Ablation study methodology
- ✅ Reproducible research workflows
- ✅ Statistical significance testing
- ✅ Publication-quality figure generation

### Alignment with Prior Work
- 📍 MARTHR methodology: simulation → CSV → figures → manuscript
- 📍 AER-MQoS methodology: ablation studies, caption refinement
- 📍 MARTHR: unified framework combining both approaches

---

## 🎯 READING STRATEGY

### Option 1: Skim & Execute (Busy Person)
1. QUICK_START_CHECKLIST.md (5 min)
2. PROJECT_PROPOSAL.md Section 3 (10 min)
3. EXECUTION_PLAN.md Phase 1 (20 min)
4. Start coding
**Total:** 35 min

### Option 2: Understand the Context (Researcher)
1. QUICK_START_CHECKLIST.md (5 min)
2. PROJECT_PROPOSAL.md (20 min)
3. LITERATURE_REVIEW.md (30 min)
4. EXECUTION_PLAN.md (60 min)
5. Start coding with full context
**Total:** 115 min

### Option 3: Master the Entire Project (PhD/Advisor)
1. All documentation in order (150 min)
2. Review MARTHR project for methodology (60 min)
3. Review AER-MQoS project for methodology (60 min)
4. Deep review of EXECUTION_PLAN.md all phases (120 min)
5. Ready to oversee all 15 weeks
**Total:** 390 min (6.5 hours)

---

## ✅ VERIFICATION CHECKLIST

### Before Phase 1
- [ ] Read PROJECT_PROPOSAL.md ✅
- [ ] Read LITERATURE_REVIEW.md ✅
- [ ] Read EXECUTION_PLAN.md Phase 1 ✅
- [ ] Understand MCS model ✅
- [ ] Understand ablation study plan ✅
- [ ] Contiki-NG environment ready ✅

### Before Phase 2
- [ ] Phase 1 firmware complete ✅
- [ ] Unit tests pass ✅
- [ ] Simulation scenarios setup ✅
- [ ] MRHOF baseline ready ✅

### Before Phase 5
- [ ] Phases 2–4 complete ✅
- [ ] All figures generated ✅
- [ ] Data provenance documented ✅
- [ ] LaTeX environment ready ✅

### Before Submission
- [ ] Manuscript camera-ready ✅
- [ ] All references verified ✅
- [ ] Figures reproducible ✅
- [ ] Code open-source ready ✅
- [ ] Venue requirements met ✅

---

## 📞 QUICK REFERENCE

### Most Important Documents (in order)
1. **QUICK_START_CHECKLIST.md** ← Read first
2. **PROJECT_PROPOSAL.md** ← Understand vision
3. **LITERATURE_REVIEW.md** ← Understand novelty
4. **EXECUTION_PLAN.md** ← Understand plan
5. **README.md** ← Understand structure

### For Specific Tasks
- "How do I build this?" → README.md
- "What are the phases?" → MASTER_TRACKER.md
- "What do I do Week 2?" → EXECUTION_PLAN.md Phase 1
- "How do I make figures?" → scripts/generate_marthr_figures.py
- "How do I run stats?" → scripts/statistics/compute_ablation_stats.py

### Troubleshooting
- Build errors → BUILD_NOTES.txt (Phase 1)
- Cooja crashes → PROJECT_HEALTH_REPORT.md (Phase 2)
- CSV parsing issues → scripts/regenerate_base_csvs.py comments
- Figure generation → scripts/generate_marthr_figures.py comments

---

## 🔗 EXTERNAL REFERENCES

### Papers Analyzed (7 Recent 2026 Publications)
1. arXiv:2606.26124 — FANET Routing Resilience (Fuzzy + Bio-inspired)
2. arXiv:2606.09504 — Hierarchical Federated Learning in Tactical MANETs
3. arXiv:2606.00184 — Passive Reconnaissance of OLSR Defenses (ML)
4. arXiv:2602.13204 — Hybrid Secure Routing in MANETs
5. arXiv:2601.10544 — SDN-Driven Innovations in MANETs and IoT
6. arXiv:2512.02663 — Theoretical Analysis of Beaconless Geocast Protocols
7. arXiv:2511.15710 — DTN-Based Opportunistic Routing for Disaster Recovery

**All summarized in:** LITERATURE_REVIEW.md

### Contiki-NG Resources
- Official: https://github.com/contiki-ng/contiki-ng
- RPL Spec: RFC 6550 (IETF)
- MRHOF: RFC 6719 (IETF)

### Simulation Environment
- Cooja: Contiki-NG's built-in network simulator
- Hardware: Any Linux machine (4GB RAM minimum)
- Python: 3.8+ with pandas, numpy, scipy, matplotlib

---

## 🎓 LEARNING JOURNEY

**Week 1–2:** Foundation
- [ ] Understand the problem (trust + energy + QoS)
- [ ] Know the 7 papers and their limitations
- [ ] Grasp the MCS model concept

**Week 3–4:** Design
- [ ] Learn federated trust aggregation
- [ ] Understand RPL/MRHOF integration
- [ ] Study ablation study methodology

**Week 5–6:** Implementation
- [ ] Write firmware modules
- [ ] Run simulations
- [ ] Collect baseline data

**Week 7–8:** Analysis
- [ ] Compute statistics
- [ ] Perform ablation studies
- [ ] Interpret results

**Week 9–10:** Presentation
- [ ] Generate figures
- [ ] Write captions
- [ ] Ensure reproducibility

**Week 11–15:** Documentation
- [ ] Write manuscript
- [ ] Refine wording
- [ ] Submit to venue

---

## 📄 DOCUMENT METADATA

| Document | Lines | Topics | Owner | Phase |
|----------|-------|--------|-------|-------|
| PROJECT_PROPOSAL.md | ~400 | Proposal, roadmap | PM | 0 |
| LITERATURE_REVIEW.md | ~500 | 7 papers, gaps | Researcher | 0 |
| EXECUTION_PLAN.md | ~700 | Phases 0–7 | PM | 0 |
| README.md | ~300 | Quick start | Everyone | 0 |
| MASTER_TRACKER.md | ~400 | Milestones | PM | 0 |
| QUICK_START_CHECKLIST.md | ~200 | Checklists | Everyone | 0 |
| This index | ~400 | Navigation | Everyone | 0 |
| **Phase 1 specs** | ~300 | ARCHITECTURE_SPEC.md | Dev | 1 |
| **Firmware code** | ~1000 | *.c / *.h files | Dev | 1 |
| **Analysis scripts** | ~500 | Python scripts | Data | 3–4 |
| **Manuscript** | ~3000 | LaTeX source | Writer | 5 |

---

## 🎯 FINAL GUIDANCE

**Read these in order, don't skip:**
1. QUICK_START_CHECKLIST.md (5 min) ← You are here
2. PROJECT_PROPOSAL.md (20 min)
3. LITERATURE_REVIEW.md (30 min)
4. EXECUTION_PLAN.md Phase 1 (20 min)
5. Start coding Phase 1

**Then reference as needed:**
6. README.md (when implementing)
7. MASTER_TRACKER.md (when tracking progress)
8. BUILD_NOTES.txt (when troubleshooting)
9. Phase-specific docs (as phases begin)

---

**Document Version:** 1.0  
**Last Updated:** July 5, 2026  
**Next:** Read PROJECT_PROPOSAL.md (20 minutes)

