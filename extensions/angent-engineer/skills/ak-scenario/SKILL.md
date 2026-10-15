---
name: ak-scenario
description: Generate evidence-grounded edge cases and test targets across the stable twelve dimensions, with one-shot or bounded novelty/saturation exploration.
metadata: {port: angent-fallback, mode: adapted}
---

# Scenario — Portable Fallback

Use to expand stateful features, APIs and high-risk changes into concrete, prioritized QA scenarios before implementation, during test design or for release audit. Stable Engineer 2.19.0 offers two **distinct modes**, not merely a large list of imagined failures:

- **One-shot (default)**: one pass over relevant dimensions, usually a small set of concrete scenarios per dimension.
- **Iterative (--iterations N or --saturation)**: one high-value situation per round with deduplication, variant expansion, coverage tracking and a bounded/saturation stop gate.

## Twelve relevant dimensions

1. User/actor types — admin, guest, blocked, bot, first-time users.
2. Input extremes — missing, null, empty, Unicode, oversized or injection-like values.
3. Timing — races, concurrent requests, retries, timeouts, slow networks.
4. Scale — empty/single/large collections, pagination/cursor boundaries.
5. State transitions — abort/restart/resume, intermediate and partial states.
6. Environment — platform/device, accessibility, locale/timezone and dependency limits.
7. Failure cascades — database/service/disk/network outage and partial write.
8. Authorization — identity, roles, tenants, token expiry, session or privilege boundary.
9. Data integrity — duplicate keys, orphan state, encoding, concurrent migrations.
10. Integration — third-party retries, webhook replay, version/contract drift.
11. Compliance/privacy — retention, deletion, audit and personal-data exposure where applicable.
12. Business logic — price, tier, limits, refund, cancellation, entitlement edge cases.

Select and **explain** relevant dimensions and important skips; a skip based on a fragile assumption becomes a scenario to test. Add domain-specific dimensions only when needed. Do not mechanically enumerate all twelve for every trivial task.

## One-shot mode

Read actual feature definition/source and state machine when available. For each relevant dimension, derive specific trigger/precondition/actor, expected behavior/invariant, adverse consequence and test oracle; prioritize by plausible severity and impact. Critical implies credible data-loss, security or silent-corruption risks; High impacts core functionality for affected users. Return scenarios with IDs and an honest dimensional coverage summary.

## Iterative and saturation mode

For --iterations N, honor the requested maximum bounded iterations and retain a trace of work; for --saturation, stop when **two consecutive iterations** introduce no genuinely new situations (plus an explicit safety iteration cap if the runtime demands one).

For each iteration:
1. Select the highest-value unexplored dimension/combination or deliberately shift actor, time, negation or scale after repeated same-dimension work.
2. Generate a concrete scenario with trigger, state/preconditions, flow, expected outcome and reason the outcome matters.
3. Classify against accepted scenarios as **new**, **variant**, **duplicate** or **out-of-scope/low-value**. Distinct actor/state/outcome can justify a variant; cosmetic rewording cannot.
4. Keep genuinely new/important variants; expand meaningful boundary/failure cases, classify severity, and log discards with cause.
5. Update coverage dimensions, repeated non-novel counts and remaining high-impact gaps. Periodically report meaningful progress rather than repeating large tables.

If the host supports durable project logs, store an authorized scenario-results.tsv or equivalent; do not imply a TSV was written when the work exists only in chat. Do not use a fabricated composite score as proof of test coverage: distinct scenario count and tested requirement matrix matter more.

## Output and handoff

Include selected/skipped dimensions with rationale, kept scenarios (ID, dimension, actor/precondition, trigger, expected behavior/test oracle, severity), duplicates filtered, residual coverage gaps and one-shot/iteration/saturation stop reason. Distinguish **generated test targets** from **implemented or executed tests**.

Pass high-risk scenarios to Plan/Predict and behavior expectations to Test when authorized; do not automatically mutate a test suite or project board under a scenario-only request.
