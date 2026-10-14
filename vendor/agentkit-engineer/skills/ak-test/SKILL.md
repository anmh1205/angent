---
name: ak-test
description: Run validation, create or optimize test suites, audit weak tests, and return structured evidence about code, build, coverage, browser/UI, and regression behavior.
license: MIT
metadata: {port: angent-fallback, mode: adapted}
---

# Test — Portable Fallback

Testing exists to establish a behavioral/quality claim, not merely to run commands or maximize a metric.

Use project-native tooling and the browser/runtime capabilities the active harness actually exposes.

## Choose the test job

Distinguish the requested outcome:

- **validate** — run focused or broad unit/integration/E2E/build/type/lint/coverage/UI checks;
- **create** — add a test suite or missing tests for an accepted behavior;
- **optimize** — reduce runtime/flakiness/CI cost without weakening the protected behavioral signal;
- **audit** — identify weak, misleading, flaky, redundant, or missing tests and repair them only when edits are authorized.

Do not mutate tests merely because Test can detect a gap.

## Start from the acceptance question

Identify:
- claim to establish;
- affected surface;
- relevant environment/configuration;
- project-native commands;
- expected evidence;
- whether test-source edits are authorized;
- coverage/whole-scope promise, if any.

Coverage percentage is evidence about exercised code, not proof of behavioral completeness.

## Discover and execute proportionally

Read applicable `AGENTS.md`, build/package config, CI, test directories, and known-good commands.

Run the smallest set that can establish the claim, then widen when:
- failures imply broader impact;
- an interface has downstream consumers;
- release/merge policy requires it;
- the Contract promises broad coverage.

For test creation/optimization, preserve the behavior the suite is intended to detect; do not optimize CI by deleting the signal.

## UI/browser validation

Use actual available capability:
- project-native Playwright/Cypress/browser suites;
- connected browser/computer-use;
- installed browser workflow.

When visual/responsive/accessibility/form/console behavior matters, collect the evidence needed for that claim.

If browser capability or authenticated setup is unavailable, report the exact verification gap instead of inferring visual success from build success.

## Failure handling

A failing test is an observation, not automatically a diagnosis.

Separate:
- product/code defect;
- test defect;
- environment/provider/configuration failure;
- flaky/noisy measurement;
- unresolved attribution.

Return non-obvious causes to debugging/Reasoning before patching blindly.

## Report

Return:
- operation and test scope;
- commands/tools/environments used;
- fresh outcomes;
- created/changed tests when authorized;
- failures and attribution confidence;
- coverage/visual limitations;
- whether the requested acceptance claim is established.

A green command that did not exercise the promised behavior is not a task PASS.
