# NS-3 MARTHR Routing Module Structure

## Module Layout
```
ns-3-dev/src/marthr-routing/
├── model/
│   ├── marthr-routing-header.h          # IPv6 routing header format
│   ├── marthr-routing-header.cc
│   ├── marthr-context.h                 # Context-aware weight adaptation (ported from C)
│   ├── marthr-context.cc
│   ├── marthr-trust-table.h             # Trust management (ported from C)
│   ├── marthr-trust-table.cc
│   ├── marthr-score.h                   # Multi-criteria scoring (ported from C)
│   ├── marthr-score.cc
│   ├── marthr-rank.h                    # Rank computation (ported from C)
│   ├── marthr-rank.cc
│   ├── marthr-routing-protocol.h        # Main protocol class (NS-3 specific)
│   └── marthr-routing-protocol.cc
├── helper/
│   ├── marthr-routing-helper.h          # Installation helper
│   └── marthr-routing-helper.cc
├── examples/
│   ├── marthr-example.cc                # Minimal working example
│   └── marthr-grid-example.cc           # Grid topology scenario
├── test/
│   ├── marthr-routing-test-suite.cc
│   └── marthr-trust-update-test.cc
├── CMakeLists.txt                       # Build configuration
└── wscript                              # Waf build script (NS-3 uses Waf)

## Integration Steps
1. Create wscript with source files and dependencies
2. Port C code (context, trust, score, rank) to NS3::Object hierarchy
3. Implement MarthrRoutingProtocol : public ns3::Ipv6RoutingProtocol
4. Add trace sources for metrics collection (NodeId, ParentId, Rank, Trust, Energy, QoS, MCS)
5. Integrate with NS-3 simulator callbacks and packet tagging
6. Create installation helper for easy topology setup

## Key NS-3 Concepts
- Trace sources: Export metrics per-node at each routing decision
- Packet tagging: Attach metric metadata to packets for statistics collection
- IP layer routing: Handle IPv6 routing with custom metric
- Helper pattern: Simplify installation on NodeContainers
- Test suite: Use NS3_TEST for unit testing of protocol functions
