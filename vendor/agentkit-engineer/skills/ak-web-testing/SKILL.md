---
name: ak-web-testing
description: Design and run web unit, integration, E2E, visual, accessibility, load and browser-compatibility tests using project-native or harness-available tools.
license: Apache-2.0
metadata: {port: angent-fallback, mode: portable}
---

# Web Testing — Portable Fallback

Use Playwright/Vitest/k6 or the project's established equivalents when available.

## Load progressively

- `references/web-test-matrix.md` — choose the right test layer.
- `references/browser-evidence.md` — browser/runtime artifacts and authenticated flows.
- `references/flakiness.md` — diagnose unreliable tests instead of adding retries blindly.
- `references/performance-accessibility.md` — load/performance/a11y validation.

## Workflow

1. Start from the acceptance claim.
2. Inspect current test stack and CI conventions.
3. Choose the cheapest reliable test layer.
4. Create stable data/session setup.
5. Run targeted tests first.
6. Widen across browsers/devices/performance only when the change/risk requires it.
7. Preserve traces/screenshots/logs only when they help explain a result.
8. Report scope and untested surfaces explicitly.

## Quality gates

- no green test that fails to exercise the requested behavior;
- no blind retry masking a race;
- no UI pass inferred from compile/build alone;
- no whole-site claim from one sampled page.
