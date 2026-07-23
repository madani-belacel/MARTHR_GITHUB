# LITERATURE REVIEW: Recent MANET Routing Innovations (2026)
## State-of-the-Art Analysis & Gap Identification

**Review Date:** July 5, 2026  
**Scope:** MANET/FANET routing, security, trust, energy awareness, machine learning  
**Search Sources:** arXiv, IEEE Xplore (sampling)

---

## TABLE OF CONTENTS
1. [Publication Summaries](#publication-summaries)
2. [Comparative Analysis](#comparative-analysis)
3. [Research Gaps](#research-gaps)
4. [Opportunities for Original Contribution](#opportunities)
5. [Recommended Next Steps](#recommended-next-steps)

---

## PUBLICATION SUMMARIES

### Publication 1: Enhancing FANET Routing Resilience
**Citation:** Yuan, X., Su, J., Xia, Y., Song, C. (June 2026). "Enhancing FANET Routing Resilience: A Fuzzy-Driven Bio-Inspired Approach and Its Quantitative Evaluation." arXiv:2606.26124.

**Summary:**
- Applies fuzzy logic combined with bio-inspired algorithms (swarm intelligence) to improve FANET routing robustness
- Tests on flying ad hoc networks with dynamic topology
- Metrics: delivery ratio, latency, network stability

**Strengths:**
- Novel combination of fuzzy + bio-inspired techniques
- Topology adaptation for aerial networks
- Quantitative evaluation framework

**Limitations:**
- No security/trust integration
- Limited to aerial scenarios; unclear applicability to ground networks
- No energy consumption analysis
- Scalability to > 100 nodes not tested

**Future Work Identified:**
- Real-world flight testing on physical UAV swarms
- 3D topology dynamics with altitude changes
- Heterogeneous aerial platforms (fixed-wing, quadcopter, airship)

**Gap for MARTHR:**
- MARTHR can complement this by adding trust-aware filtering for malicious/compromised UAVs
- Energy-aware adaptation when low-battery UAVs join

---

### Publication 2: Hierarchical Federated Learning in Tactical MANETs
**Citation:** Thornton, C.E., Jakubisin, D.J. (June 2026). "Hierarchical Federated Learning for Unsupervised Waveform Classification over Tactical MANETs." arXiv:2606.09504.

**Summary:**
- Distributed machine learning on contested radio networks
- Unsupervised waveform classification (signal detection/identification)
- Privacy-preserving federated learning without central aggregator
- Tested in tactical (military-grade contested) environments

**Strengths:**
- Novel federated approach without centralization
- Privacy-by-design (no raw signals transmitted)
- Real tactical constraints (jamming, interception risk)

**Limitations:**
- Focuses on signal processing, not routing
- No integration with routing protocol
- Compute overhead not quantified
- Requires synchronized local models (what if sync fails?)

**Future Work Identified:**
- Real-time deployment on resource-constrained devices
- Energy-efficient model training (edge AI)
- Dynamic topology adaptation during learning

**Gap for MARTHR:**
- MARTHR routing can provide stable multi-hop paths for federated learning aggregation
- Trust layer can identify which nodes are reliable for model aggregation
- Energy awareness can predict when nodes become unavailable

---

### Publication 3: Passive Reconnaissance of OLSR Defenses
**Citation:** Schweitzer, N., Danilchenko, K., Stulman, A. (June 2026). "Passive Reconnaissance of Routing-Layer Defenses in OLSR-Based MANETs using ML." arXiv:2606.00184.

**Summary:**
- Uses machine learning to detect OLSR routing protocol anomalies
- Passive detection (no active probing, avoids alerting attackers)
- Identifies rank inflation, sybil, and route hijacking attempts
- ML classifier trained on legitimate vs. anomalous OLSR messages

**Strengths:**
- First-of-its-kind passive ML-based detection
- No active probing (stealthy)
- Good empirical accuracy on simulated attacks

**Limitations:**
- Defensive analysis only; doesn't propose new protocol design
- OLSR-specific (limited generalizability)
- No mitigation mechanism; only detection
- False positive/negative trade-off not optimized for real networks

**Future Work Identified:**
- Multi-protocol security analysis (AODV, RPL, DSR)
- Real-time mitigation strategies (not just detection)
- Zero-trust frameworks for ad-hoc networks

**Gap for MARTHR:**
- MARTHR can integrate this ML detector into the trust layer
- Use detection signals to dynamically adjust trust weights for flagged nodes
- Combine detection with proactive rank filtering

---

### Publication 4: Hybrid Secure Routing in MANETs
**Citation:** Boufaida, S.O., Benmachiche, A., Maatallah, M., Chemam, C. (January 2026). "Hybrid Secure Routing in Mobile Ad-hoc Networks (MANETs)." arXiv:2602.13204.

**Summary:**
- Combines cryptographic security (encryption, digital signatures) with trust-based routing
- "Hybrid" = two-layer defense: protocol-level crypto + reputation-level trust
- Evaluated on AODV and DSR protocols

**Strengths:**
- Defense-in-depth: both crypto and trust
- Compatible with existing protocols
- Tested on two major routing protocols

**Limitations:**
- High computational overhead (crypto + trust computation)
- Energy impact not quantified
- No QoS metrics considered (latency, bandwidth)
- Scalability limited to small networks (10–50 nodes tested)
- Static trust weights; no adaptive context

**Future Work Identified:**
- Energy efficiency improvements
- Large-scale topology validation
- IoT integration (resource-constrained devices)
- Adaptive trust weight tuning

**Gap for MARTHR:**
- MARTHR provides energy + QoS awareness missing here
- Adaptive context (application-specific) trust weights
- Scalability via federated aggregation instead of global trust table

---

### Publication 5: SDN-Driven MANET Innovations
**Citation:** Piroddi, A., Fonti, R. (January 2026). "SDN-Driven Innovations in MANETs and IoT: A Path to Smarter Networks." arXiv:2601.10544.

**Summary:**
- Applies Software-Defined Networking (SDN) paradigm to MANETs
- Centralizes control plane (controller makes routing decisions)
- Decentralizes data plane (nodes forward per controller instructions)
- Tested on IoT scenarios with edge computing

**Strengths:**
- Centralized control enables global optimization
- Separation of control and data planes simplifies management
- Edge computing integration for low-latency decisions

**Limitations:**
- High control overhead (every decision sent to controller)
- Single point of failure (controller crash = network partition)
- Assumes reliable controller connectivity (not realistic in highly dynamic MANETs)
- Weak in scenarios with frequent node join/leave

**Future Work Identified:**
- Hybrid centralized/decentralized control
- Edge AI placement strategies
- 6G integration

**Gap for MARTHR:**
- MARTHR is **fully distributed** (no central controller dependency)
- Federated trust aggregation replaces SDN controller role
- Resilience to controller loss inherent in design

---

### Publication 6: Beaconless Geocast Protocols (Theoretical)
**Citation:** Gudmundsson, J., Kostitsyna, I., Löffler, M., Müller, T., Sacristán, V., Silveira, R.I. (December 2025). "Theoretical analysis of beaconless geocast protocols in 1D." arXiv:2512.02663.

**Summary:**
- Formal complexity analysis of location-aware routing without beacon messages
- Focuses on 1D topologies (linear network)
- Proves lower bounds on message complexity and delivery time
- Comparison with classical beacon-based geocasting

**Strengths:**
- Rigorous theoretical foundation
- Proves fundamental limits on protocol efficiency
- No empirical overhead; purely analytical

**Limitations:**
- Limited to 1D; real networks are 2D/3D
- No practical protocol implementation
- Energy/latency trade-offs not discussed
- No security or trust considerations

**Future Work Identified:**
- 2D/3D topology analysis
- Practical implementation on real hardware
- Topology-aware optimization strategies

**Gap for MARTHR:**
- MARTHR can implement practical geocast using 3D coordinates (UAVs + ground)
- Energy-aware beaconless operation
- Trust layer prevents false location claims (spoofing defense)

---

### Publication 7: DTN-Based Opportunistic Routing for Disaster Recovery
**Citation:** Hasan, M.M.U., Radenkovic, M. (November 2025). "Improving Resiliency of Vital Services in Flood-Affected Regions of Bangladesh Using Next-Generation Opportunistic DTN Edge Ad Hoc Networks." arXiv:2511.15710.

**Summary:**
- Delay-tolerant networks (DTNs) + opportunistic forwarding for emergency scenarios
- Tested in flood-disaster contexts where infrastructure is destroyed
- Edge caching strategies to buffer critical data
- Integration with 5G/satellite for backbone connectivity

**Strengths:**
- Real-world disaster scenario focus
- Opportunistic forwarding (forward when opportunity arises, not deterministic path)
- Edge caching for resilience

**Limitations:**
- Disaster/emergency-only context; limited generalizability
- No multi-criteria optimization (security, energy)
- Scalability to > 100 nodes unclear
- Trade-offs between SLA guarantees and delay tolerance not analyzed

**Future Work Identified:**
- Cross-layer optimization
- 5G/satellite gateway integration
- Real-time SLA guarantees with delay tolerance

**Gap for MARTHR:**
- MARTHR can apply DTN concepts to routine high-mobility scenarios (not just disasters)
- Trust layer identifies reliable "opportunistic hops" vs. flaky nodes
- Energy awareness predicts when nodes go offline (avoid using them)

---

## COMPARATIVE ANALYSIS

### Research Dimensions

| Dimension | FANET Fuzzy | Tactical FL | OLSR ML Defense | Hybrid Sec | SDN MANET | Beaconless 1D | DTN Disaster |
|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|
| **Trust/Reputation** | ❌ None | ❌ None | ✅ ML-based | ✅ Reputation | ❌ None | ❌ None | ❌ None |
| **Energy Awareness** | ❌ Not mentioned | ⚠️ Mentioned | ❌ No | ❌ No | ❌ No | ❌ No | ⚠️ Edge cache focus |
| **QoS/Latency** | ✅ Latency metric | ❌ No | ⚠️ Detection latency | ❌ No | ✅ Edge low-latency | ⚠️ Theoretical only | ✅ Delay-tolerant |
| **Scalability (N nodes)** | ~ 50 nodes | ~ 20 nodes | ~ 100 nodes | ~ 50 nodes | ~ 100 nodes | Theoretical | ~ 50 nodes |
| **Security Focus** | ❌ None | ✅ Privacy-preserving | ✅ Attack detection | ✅ Crypto+Trust | ❌ None | ❌ None | ⚠️ Implicit |
| **Heterogeneous Topologies** | ✅ Aerial-only | ❌ Tactical (ground) | ❌ Ground-only | ❌ Ground-only | ❌ IoT-only | ❌ Linear | ❌ Ground-only |
| **Context Adaptation** | ❌ Fixed | ❌ Fixed model | ❌ Fixed classifier | ❌ Fixed weights | ✅ Centralized | ❌ No | ❌ No |
| **Ablation Studies** | ❌ No | ❌ No | ❌ No | ❌ No | ❌ No | ❌ Theoretical | ❌ No |
| **Open-Source Available** | ⚠️ Code snippet | ❌ Likely closed | ❌ Likely closed | ❌ No | ❌ No | ✅ Theoretical | ❌ No |

### Key Observation
**No publication integrates all of:**
- Trust + Energy + QoS (3-objective optimization)
- Heterogeneous topology support (aerial + ground + sensor)
- Adaptive context-aware parameter tuning
- Ablation studies for reproducibility
- Open-source, reproducible pipeline

---

## RESEARCH GAPS

### Gap 1: Unified Multi-Objective Framework
**Problem:** Existing work treats security, energy, and QoS as separate concerns.
- FANET fuzzy ignores trust and energy
- Hybrid secure routing ignores QoS and energy
- SDN assumes global knowledge (not realistic)

**Opportunity:** Protocol that **simultaneously optimizes** trust, energy, and QoS with explicit trade-off analysis.

### Gap 2: Adaptive Context-Aware Routing
**Problem:** Most protocols use fixed parameters regardless of application domain.
- Disaster recovery differs from normal ops
- Safety-critical differs from best-effort
- Low-power nodes differ from high-power nodes

**Opportunity:** Protocol that **shifts weights dynamically** based on:
- Application safety level (safety-critical vs. best-effort)
- Network threat level (high attack rate vs. benign)
- Energy budget (low-power emergency vs. normal operation)

### Gap 3: Scalable Trust Management
**Problem:** Centralized trust tables don't scale (O(n²) memory).
- Hybrid secure routing stores global trust matrix
- SDN requires central controller

**Opportunity:** **Federated trust aggregation** where each node maintains only local trust views, gossips periodically.

### Gap 4: Heterogeneous Topology Support
**Problem:** Existing protocols assume single-tier networks.
- FANET focused on aerial only
- Tactical MANETs are ground-based
- No joint ground-aerial-sensor frameworks

**Opportunity:** Protocol that **natively supports mixed topologies** with different hop distances, power budgets, and threat models.

### Gap 5: Energy-Aware Trust Decay
**Problem:** Trust doesn't account for energy state.
- A trusted node can't forward if battery is 5%
- No model for "soft failures" due to energy rationing

**Opportunity:** **Dynamic trust decay** that correlates trust with residual energy:
```
trust_adjusted = base_trust × (residual_energy / max_energy)^k
```

### Gap 6: Reproducible Ablation Framework
**Problem:** Existing papers don't clearly show individual contribution of each metric.
- Can't answer: "Is the 5% improvement from trust, energy, or QoS?"
- No configurable "turn off" levers

**Opportunity:** Protocol with **pluggable levers** (A1: disable trust, A2: disable energy, A3: disable QoS) + statistical ablation framework.

---

## OPPORTUNITIES FOR ORIGINAL CONTRIBUTION

### Proposed Solution: MARTHR (MANET-Trust-Aware Hierarchical Routing)

**Core Idea:**
A **hierarchical, context-aware routing protocol** that:
1. **Unifies** trust, energy, and QoS into a single Multi-Criteria Score (MCS)
2. **Adapts** weights dynamically based on application context (safety_level, threat_level)
3. **Scales** via federated trust aggregation (no central authority)
4. **Supports** mixed topologies (aerial, ground, sensor nodes)
5. **Provides** transparent ablation mechanisms (plug-in modules)

**Differentiation vs. Publications 1–7:**

| vs. | How MARTHR Advances |
|-----|-----|
| FANET Fuzzy | Adds trust + energy + QoS (3-objective) + ablation studies |
| Tactical FL | Integrates ML-detected threats into trust layer |
| OLSR ML Defense | Proactive protocol redesign, not just detection |
| Hybrid Secure | Adds energy awareness + QoS + adaptive context |
| SDN MANET | Fully distributed federated design (no controller) |
| Beaconless 1D | Practical 3D protocol + energy-aware + trust-based |
| DTN Disaster | Generalizable beyond emergency (routine high-mobility) + multi-objective |

---

## RECOMMENDED NEXT STEPS

### Immediate (This Week)
1. ✅ Finalize PROJECT_PROPOSAL.md (in progress)
2. Create firmware skeleton: `marthr_ocp.c` with rank computation
3. Design federated trust aggregation protocol (TLV messages)
4. Outline Cooja simulation topology

### Short-term (Weeks 2–4)
1. Implement MARTHR in Contiki-NG rpl-lite
2. Create unit tests (rank computation, context fusion)
3. Setup Cooja reference scenarios (25-node grid + random)
4. Run baseline MRHOF comparison

### Medium-term (Weeks 5–8)
1. Conduct ablation studies (A1, A2, A3)
2. Attack injection (selective forwarding, rank inflation)
3. Stress tests (2× traffic, 50% link loss)
4. Statistical analysis (Mann–Whitney tests)

### Long-term (Weeks 9–12)
1. Figure generation and manuscript writing
2. Camera-ready PDF preparation
3. Submit to target venue (IEEE ComSoc, ACM SIGCOMM)

---

## REFERENCES (Detailed)

**[1]** Yuan, X., Su, J., Xia, Y., Song, C. (2026). "Enhancing FANET Routing Resilience: A Fuzzy-Driven Bio-Inspired Approach and Its Quantitative Evaluation," arXiv:2606.26124.

**[2]** Thornton, C.E., Jakubisin, D.J. (2026). "Hierarchical Federated Learning for Unsupervised Waveform Classification over Tactical MANETs," arXiv:2606.09504.

**[3]** Schweitzer, N., Danilchenko, K., Stulman, A. (2026). "Passive Reconnaissance of Routing-Layer Defenses in OLSR-Based MANETs using ML," arXiv:2606.00184.

**[4]** Boufaida, S.O., Benmachiche, A., Maatallah, M., Chemam, C. (2026). "Hybrid Secure Routing in Mobile Ad-hoc Networks (MANETs)," arXiv:2602.13204.

**[5]** Piroddi, A., Fonti, R. (2026). "SDN-Driven Innovations in MANETs and IoT: A Path to Smarter Networks," arXiv:2601.10544, DOI: 10.12720/jait.16.3.411-425.

**[6]** Gudmundsson, J., Kostitsyna, I., Löffler, M., Müller, T., Sacristán, V., Silveira, R.I. (2025). "Theoretical analysis of beaconless geocast protocols in 1D," arXiv:2512.02663.

**[7]** Hasan, M.M.U., Radenkovic, M. (2025). "Improving Resiliency of Vital Services in Flood-Affected Regions of Bangladesh Using Next-Generation Opportunistic DTN Edge Ad Hoc Networks," arXiv:2511.15710.

---

**Document Last Updated:** July 5, 2026  
**Next Review:** Before manuscript submission

