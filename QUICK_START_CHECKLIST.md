# MARTHR PROJECT: QUICK START CHECKLIST

**Welcome to the MARTHR Project!**

This is a high-quality research project proposal on **MANET-Trust-Aware Hierarchical Routing**.

---

## 📍 START HERE (First Time? Read This!)

### 1. **What is MARTHR?** (2 minutes)
MARTHR is a novel routing protocol that unifies:
- **Trust** (node reputation)
- **Energy awareness** (residual battery)
- **QoS** (latency, bandwidth)

through a single **Multi-Criteria Score (MCS)** with context-adaptive weights.

### 2. **Why is it Novel?** (2 minutes)
Recent papers (2026) show:
- FANET protocols optimize routing but ignore trust
- Secure routing protocols add trust but ignore energy/QoS
- No protocol unifies all three with transparent ablation studies

**MARTHR fills this gap.**

### 3. **What's Included?** (1 minute)
```
proposed_projet/
├── PROJECT_PROPOSAL.md       ← Start here (overview)
├── LITERATURE_REVIEW.md      ← Analysis of 7 recent papers
├── EXECUTION_PLAN.md         ← 15-week detailed roadmap
├── README.md                 ← Project guide
├── MASTER_TRACKER.md         ← Status dashboard
├── QUICK_START_CHECKLIST.md  ← This file
└── [folders for code, data, manuscript, etc.]
```

---

## ✅ QUICK CHECKLIST (Do These Now!)

### Phase 0: Setup (This Week and Beyond)

> This project is intended to span at least one full week of work for a first complete implementation cycle. A short one-hour pass is not enough to reach a meaningful milestone.
- [x] **Read PROJECT_PROPOSAL.md** (10 min) — High-level overview
- [x] **Skim LITERATURE_REVIEW.md** (15 min) — Why MARTHR is needed
- [x] **Review EXECUTION_PLAN.md** (20 min) — Understand the plan
- [x] **Read the reproduction and evaluation methodology** in [Temps/CHECKLIST_REPRODUCTION.md](Temps/CHECKLIST_REPRODUCTION.md) and [Temps/METHODOLOGIE_EVALUATION.md](Temps/METHODOLOGIE_EVALUATION.md)
- [x] **Install dependencies:** `pip install -r requirements.txt`
- [x] **Run the reproduction pipeline:** `python3 scripts/reproduce_project.py`
- [ ] **Inspect the data provenance** in [data/raw](data/raw) and [data/estimated](data/estimated)
- [ ] **Check for placeholders or inconsistencies** in the manuscript, scripts, and documentation

### Before Phase 1 (Week 2)
- [x] **Deep-read EXECUTION_PLAN.md** Phase 1 section (1 hour)
- [x] **Create ARCHITECTURE_SPEC.md** (formal protocol design)
- [x] **Setup coding environment** (IDE, git, build tools)
- [x] **Begin firmware implementation** (marthr_ocp.c)

---

## 📚 DOCUMENTS AT A GLANCE

| Document | Purpose | Read Time | Priority |
|----------|---------|-----------|----------|
| **PROJECT_PROPOSAL.md** | Vision, contributions, success criteria | 15 min | 🔴 Must |
| **LITERATURE_REVIEW.md** | Analysis of 7 papers (2026) + gaps | 30 min | 🔴 Must |
| **EXECUTION_PLAN.md** | Phase-by-phase roadmap (15 weeks) | 60 min | 🔴 Must |
| **README.md** | Quick start + project structure | 20 min | 🟡 Should |
| **MASTER_TRACKER.md** | Status dashboard + milestones | 20 min | 🟡 Should |
| **BUILD_NOTES.txt** | System setup + troubleshooting | 20 min | 🟢 Later |

---

## 🎯 THE 7 PAPERS (Why MARTHR Matters)

**Recent 2026 papers analyzed:**

1. **FANET Routing Resilience** (Yuan et al.) ← Good topology adapt, NO trust
2. **Federated Learning in Tactical MANETs** (Thornton & Jakubisin) ← Good privacy, NO routing
3. **OLSR Security via ML** (Schweitzer et al.) ← Good detection, NO mitigation
4. **Hybrid Secure Routing** (Boufaida et al.) ← Good trust, NO energy/QoS
5. **SDN MANET** (Piroddi & Fonti) ← Good optimization, needs central controller
6. **Beaconless Geocast 1D** (Gudmundsson et al.) ← Good theory, NO implementation
7. **DTN for Disaster Recovery** (Hasan & Radenkovic) ← Good emergency focus, NO generalization

**MARTHR's edge:**
- ✅ Unifies trust + energy + QoS (not in any paper)
- ✅ Adaptive context weights (not in any paper)
- ✅ Federated trust scaling (better than Papers 3–5)
- ✅ Ablation studies showing each lever's contribution (missing in all papers)

---

## 🚀 PROJECT AT A GLANCE

### Timeline
```
Week 1  ✅ Documentation (DONE)
Weeks 2-4: Firmware implementation
Weeks 5-6: Simulation baseline
Weeks 7-8: Ablation studies
Weeks 9-10: Figures + reproducibility
Weeks 11-13: Manuscript
Weeks 14-15: Polish + submit
```

### Outputs
- ✅ Contiki-NG firmware (open-source)
- ✅ 20-seed simulation campaign
- ✅ 12 publication-quality figures
- ✅ Camera-ready IEEE manuscript (~14 pages)
- ✅ Reproducible CSV-to-PDF pipeline

### Target Venue
- IEEE Infocom 2027 (top-tier)
- ACM MobiSys 2027 (top-tier backup)

---

## 💡 HOW MARTHR WORKS (30-Second Version)

```
┌────────────────────────────────────────────────────┐
│ Application: "This packet is safety-critical"     │
├────────────────────────────────────────────────────┤
│ MARTHR Rank Computation:                           │
│   MCS = 0.6·trust + 0.2·energy + 0.2·qos          │
│                                                    │
│   (weights adapt by application domain)           │
├────────────────────────────────────────────────────┤
│ Federated Trust: "Node A succeeded 95% of time"   │
│ Energy Aware: "Node B has 10% battery left"       │
│ QoS Metric: "Path via C has 50ms latency"        │
├────────────────────────────────────────────────────┤
│ RPL Integration: Use MCS as rank score            │
│ Result: Node D becomes parent (best MCS score)    │
└────────────────────────────────────────────────────┘
```

---

## ❓ COMMON QUESTIONS

### Q: How is this different from AER-MQoS?
**A:** MARTHR focuses on **trust** (security/reputation) in addition to energy+QoS. AER-MQoS was energy+QoS only.

### Q: How is this different from MARTHR?
**A:** MARTHR is a **proactive routing protocol**, while MARTHR was an **intrusion detection system**. Different problems, similar methodology.

### Q: Can I start Phase 1 now?
**A:** Yes! But first read EXECUTION_PLAN.md Phase 1 section to understand the implementation tasks.

### Q: What if I get stuck?
**A:** 
1. Check BUILD_NOTES.txt for common issues
2. Review PROJECT_HEALTH_REPORT.md (to be created)
3. See internal/PHASE1_ROADMAP.md for detailed implementation steps

### Q: How reproducible is this?
**A:** All figures regenerable from committed CSVs (no re-running 20 seeds of simulations). Firmware deterministically builds. Figures are bit-identical.

---

## 📞 NEXT STEP

**Pick Your Path:**

### Path A: Quick Overview (15 min)
1. ✅ Read this file (you're here!)
2. Read PROJECT_PROPOSAL.md
3. Skim LITERATURE_REVIEW.md
→ You now understand the project

### Path B: Ready to Code (60 min)
1. ✅ Complete Path A
2. Read EXECUTION_PLAN.md Phase 1
3. Read CODE_STRUCTURE.md (Phase 1 start)
→ You're ready to write firmware

### Path C: Want to Help (2 hours)
1. ✅ Complete Path B
2. Understand the data flow (CSV pipeline)
3. Review figure generation approach
→ You can contribute to any phase

---

## 🔗 DOCUMENT NAVIGATION

```
START HERE
    ↓
PROJECT_PROPOSAL.md (overview)
    ↓
LITERATURE_REVIEW.md (why it's novel)
    ↓
EXECUTION_PLAN.md (how to build it)
    ↓
Phase 1: ARCHITECTURE_SPEC.md + code_source/
    ↓
Phase 2–3: data/ + scripts/
    ↓
Phase 4–5: manuscript/ + Figures/
    ↓
Phase 6–7: camera-ready submission
```

---

## 📊 SUCCESS CRITERIA

By end of 15 weeks:
- ✅ Firmware compiles, unit tests pass
- ✅ 20-seed ablation studies complete
- ✅ All figures reproducible from CSVs
- ✅ 14-page manuscript camera-ready
- ✅ Submitted to IEEE/ACM venue

---

## 🎓 LEARNING OUTCOMES

By completing this project, you will understand:
- ✅ How to design multi-objective routing protocols
- ✅ Federated trust management in MANETs
- ✅ Contiki-NG firmware development
- ✅ Reproducible research workflows
- ✅ Publication-quality figure generation
- ✅ Statistical ablation study design

---

## 📝 FINAL CHECKLIST

Before you say "I'm ready to start Phase 1":

- [ ] Read PROJECT_PROPOSAL.md fully
- [ ] Read LITERATURE_REVIEW.md fully
- [ ] Understand the MCS model (trust + energy + QoS)
- [ ] Know what ablation studies are (A1, A2, A3)
- [ ] Understand federated trust concept
- [ ] Have Contiki-NG environment ready
- [ ] Have Python 3.8+ installed
- [ ] Have LaTeX ready (optional for Phase 5)

**If all boxes checked ✅ → You're ready for Phase 1!**

---

## 💬 QUESTIONS?

- **"What is MARTHR?"** → See PROJECT_PROPOSAL.md (Section 1)
- **"Why is it novel?"** → See LITERATURE_REVIEW.md (Research Gaps section)
- **"How do I start coding?"** → See EXECUTION_PLAN.md (Phase 1 section)
- **"How do I reproduce figures?"** → See scripts/regenerate_base_csvs.py
- **"Where's the firmware?"** → See code_source/ folder

---

**Last Updated:** July 5, 2026  
**Version:** 1.0  
**Next:** Read PROJECT_PROPOSAL.md (10 minutes)

