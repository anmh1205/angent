# Web test matrix

Choose by claim:

- pure logic → unit;
- component behavior → component/integration;
- API + DB/service → integration/contract;
- critical user flow → E2E;
- rendering/layout regression → visual;
- keyboard/semantics → accessibility checks;
- throughput/latency → load/performance;
- browser-specific behavior → cross-browser/device.

For every failure preserve trace/screenshot/log only when it helps diagnosis.
