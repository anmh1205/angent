---
name: ak-test
description: Validate software behavior, create missing test protection, audit deceptive or ineffective tests, and optimize suite/CI cost without weakening evidence or project-defined gates.
license: MIT
metadata:
  author: agentkit
  port: angent-fallback
  mode: adapted
  baseline: "AgentKit Engineer 2.19.0"
---

# Test — Portable Fallback

Testing exists to produce evidence about the requested behavior, not merely to run commands.

This fallback does not require AgentKit browser/test Skills. Prefer project-native test tooling and whatever browser/runtime capability the active harness actually exposes.

Read:
- `references/test-execution-workflow.md`;
- `references/ui-testing-workflow.md`;
- `references/report-format.md`;
- `references/test-suite-judgement.md` when creating, auditing or optimizing tests.

## Choose the actual testing outcome

- **Validate code or UI (default):** establish whether an existing change satisfies its acceptance claim, including required project checks. Treat the operation as evidence gathering; do not silently fix product code.
- **Create or extend tests:** inspect current code/specifications and existing tests, map important behaviors and failure mechanisms to the right test layers, then add missing protection with authorized edits. A useful test must fail for the defect it is supposed to catch, not merely exercise a line.
- **Audit tests:** find assertions that can pass while the requirement fails, disabled/skipped/xfail cases, flawed fixtures or mocks, nondeterminism, duplication and outdated expectations. Start read-only; change tests/CI only if the requested scope authorizes repair.
- **Optimize suite or CI:** locate measured cost and test-selection overlap, then improve scheduling, fixture isolation or impact selection while preserving required checks and the ability to catch material regressions. Never claim improved speed without comparable measurements.

Use `references/test-suite-judgement.md` for the distinct analysis/verification methods. CLI-shaped words such as `create`, `audit` or `optimize` identify the user's intended result, not a requirement to invoke any `ak test` command. Do not force suite creation or optimization when a simple test run is sufficient.

## Start from the acceptance question

Before running tests, identify what needs to be established:
- regression safety;
- specific bug reproduction/fix;
- build/type/lint integrity;
- API/contract behavior;
- end-to-end user flow;
- UI/render/accessibility state;
- performance/security property.

Do not run every available suite by default.

## Reason from behavior to proof

For a nontrivial behavior change, trace the acceptance claim through the actual producer, transformation, transport/storage boundary and consumers. At each boundary identify a failure that **would still pass** the nearest unit test, then choose the least expensive additional observation capable of detecting it. A mocked integration test proves behavior under the mock contract, not wire compatibility with the real peer; a build proves buildability, not runtime correctness. This reasoning selects tests from the system's failure mechanisms rather than a fixed suite count.

Explicitly separate **source-level**, **simulated**, **integrated**, **deployed** and **physical-device** evidence when they imply materially different claims. If the required environment is missing, preserve the strongest verified subset and state the unavailable endpoint; do not infer physical hardware behavior from a simulator or live production health from local tests.

## Discover project-native tests

Read applicable `AGENTS.md`, package/build config, CI workflow, test directories, and known-good commands.

Prefer the repository's established tooling, fixtures, thresholds and environment requirements over generic defaults.

## Execute proportionally

Run the smallest set that can establish the current claim, then widen when:
- failures imply broader impact;
- the task promises whole-scope coverage;
- release/merge gates require it;
- a changed interface has downstream consumers.

For reliability claims, repeated evidence may be required when behavior is flaky/stochastic. One green run establishes occurrence more strongly than reliability.

## UI/browser testing

Use the browser/UI capability actually available in the harness:
- project-native Playwright/Cypress/Vitest/browser tests;
- connected browser/computer-use tools;
- other installed browser Skills when present.

Do not hard-require a named AgentKit browser Skill.

If no browser capability exists, report UI verification as unavailable instead of claiming visual pass from build success.

## Failure handling

Never hide a failing test by weakening the assertion, disabling the test, or changing acceptance semantics unless evidence establishes that the test itself is wrong and the authorized task includes correcting it.

A failing test is evidence, not automatically a diagnosis. When failure cause is non-obvious, return the evidence to Debug/Reasoning rather than patching blindly inside Test.

## Report

Return:
- commands/tools and relevant environment;
- scope covered;
- pass/fail outcomes;
- failures with exact evidence;
- coverage/verification limitations;
- whether the requested acceptance claim is established.

A green command that did not exercise the requested behavior is not a pass for the task.
