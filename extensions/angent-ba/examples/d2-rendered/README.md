# D2 rendered visual examples (synthetic)

**Repository-only verification:** Any `tests/` command below requires the GitHub source checkout. Release ZIPs intentionally ship the supported `extensions/.../scripts/` executables, but not the development test suite. When using an installed package, run its bundled generator and verify actual output; check out the source only for the additional regression tests.


These are actual outputs from the original ANGENT build_d2.py using official D2 v0.9.0 on Windows, with source fixtures in extensions/angent-ba/examples/d2-*.json. Each source and SVG passed the renderer and XML/label read-back; the resulting PNGs were visually inspected at the test host.

- activity.d2 and activity.svg: guarded owner-permission flow, including swimlanes.
- erd.d2 and erd.svg: fleet/account/fault tables with PK/FK/unique and cardinality labels.
- architecture.d2 and architecture.svg: bounded vehicle-to-cloud logical integration.

This synthetic data is not an implemented IVTS schema, actual device traffic or product-authorized SRS. Regenerate after changing fixtures; do not replace images without re-running official D2 and inspecting visual content.

Run: python tests/integration/check_d2_cli.py --d2 PATH_TO_D2

The Activity source includes the latest model source_refs comments, checked against the synthetic BA graph. The comment proves **ID existence only**, not semantic correctness.
