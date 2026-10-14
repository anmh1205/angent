---
name: ak-test
description: Run and interpret unit, integration, end-to-end, UI, build, coverage and regression checks using project-native or harness-available testing capabilities.
license: MIT
metadata:
  author: agentkit
  port: angent-fallback
  baseline: "AgentKit Engineer 2.19.0"
---

# Test — Portable Fallback

Testing exists to produce evidence about the requested behavior, not merely to run commands.

This fallback does not require AgentKit browser/test Skills. Prefer project-native test tooling and whatever browser/runtime capability the active harness actually exposes.

Read:
- `references/test-execution-workflow.md`;
- `references/ui-testing-workflow.md`;
- `references/report-format.md`.

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
