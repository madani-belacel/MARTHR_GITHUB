# NS-3 MARTHR integration notes

This directory contains a minimal NS-3-compatible scaffold for MARTHR:
- marthr-routing-protocol.{h,cc}: main routing protocol skeleton
- marthr-routing-helper.{h,cc}: helper to install the protocol
- marthr-routing-example.cc: minimal example with four nodes and UDP echo traffic

To compile in a real NS-3 workspace, add these files to the `src/marthr-routing` module and register them in the module's `CMakeLists.txt` / `wscript`.
