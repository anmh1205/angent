---
name: ak-web-testing
description: Design and run repeatable web unit, component, integration, API/contract, E2E, visual, accessibility, performance/load and browser-compatibility tests with explicit environment/data boundaries.
license: Apache-2.0
metadata: {port: angent-fallback, mode: adapted, baseline: "AgentKit Engineer 2.19.0"}
---

# Web Testing — Portable Fallback

Use when the task needs a repeatable web-testing strategy or browser/runtime evidence, not merely one manual visual glance.

Prefer project-native Playwright/Vitest/Cypress/k6/axe or equivalents. No named tool is universally required.

## Load progressively

- `references/web-test-matrix.md` — choose the right layer.
- `references/browser-evidence.md` — runtime artifacts/authenticated flows.
- `references/flakiness.md` — diagnose instability instead of masking it.
- `references/performance-accessibility.md` — load/performance/a11y evidence.
- `references/environment-and-data.md` — endpoints/accounts/test data and mutation safety.

## Contract

Resolve:
- acceptance property;
- target environment/URL;
- test account/session/fixture;
- allowed remote mutations;
- browsers/devices/viewports;
- existing runner/CI conventions;
- artifact/trace needs;
- performance/accessibility threshold source when relevant.

Do not send tests to production or a real account merely because a URL is reachable.

## Workflow

1. Inspect current test stack and project commands.
2. Choose the cheapest reliable test layer(s) for the claim.
3. Prepare deterministic data/session state.
4. Implement/run focused tests.
5. Use browser evidence for properties that require rendering/interaction.
6. Diagnose failures/flakiness causally; do not add retries first.
7. Widen across browsers/devices/visual/performance/load only when risk/contract requires it.
8. Preserve traces/screenshots/logs only when useful for verdict/debugging.
9. Report exactly what was and was not covered.

## Layers

- pure logic → unit;
- component state/DOM behavior → component/integration;
- API/schema/service → API/integration/contract;
- critical user flow → E2E;
- layout/style regression → visual;
- semantics/keyboard → accessibility;
- latency/throughput/resource → performance/load;
- engine-specific behavior → cross-browser/device.

One suite does not prove every layer.

## Reliability

A green test must exercise the requested behavior.

A screenshot proves appearance at one state/viewport, not backend correctness. An HTTP 200 does not prove the UI handled the response.

For variable/flaky behavior, repeated evidence may be needed; do not infer a reliability rate from one run.

## Completion

Return commands/tools/environment, pass/fail evidence, covered claims, artifacts, and explicit gaps.

Do not claim whole-site/browser/accessibility coverage from a sampled page.
