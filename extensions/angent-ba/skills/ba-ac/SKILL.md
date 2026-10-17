---
name: ba-ac
description: Evidence-driven business analysis for ac with approved source identity, testable outcomes and non-destructive handoff.
---

# Acceptance criteria: observable obligations, boundaries and error outcomes

**Source methodology:** Adapted independently from the MIT Dev BA Kit AC method, Edward Ngo (2026): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/ac/SKILL.md. ANGENT Root retains source authority; the BA method supplies precise behavioral conditions, not new business policy.

## Establish what must be proven

1. Read the approved feature/story/use-case behavior, FR/BR and error matrix, actual actor/permission model, linked existing ACs and relevant tests. Do not insist on a specific \`us-NNN.md\` file: an accepted spec section, issue or provider document can own the criterion.
2. For each meaningful user scenario, identify **Given** observable preconditions, **When** an actor/system event occurs, **Then** the externally visible system outcome. Avoid unverifiable "is easy", vague "secure" or implementation-only details unless the contract explicitly exposes them.
3. Enumerate positive path, denial/authorization, invalid input, boundary values, timeout/offline, duplicate action, cancellation and recovery where relevant. Do not pad each story with a fixed number of criteria; coverage is based on risk and acceptance obligations.
4. Express business thresholds exactly as accepted, including units, time zone, inclusive/exclusive comparisons and owner. Test below/at/above a boundary when it changes permitted behavior. If the threshold is unknown, leave an explicit blocked decision rather than filling an example number.
5. State the expected errors or failure semantics: code/status when contractually specified, message class, no-data disclosure, state/storage side effects, allowed retry or recovery. An API HTTP response and a UI message may have separate ACs when their audiences differ.
6. Assign stable AC IDs consistent across project files, Jira, test case exports and documentation. A locally scoped \`AC-001\` is valid only if a namespace/path is always carried with it; do not create two unrelated global \`AC-001\` records and later claim one-to-one traceability.
7. Compare new ACs with existing ones to remove duplicates and contradictions without silently weakening agreed policy. Mark which source ID(s) each AC covers; an invented source link cannot establish traceability.

## Practical testable examples

- **Authorization:** Given an authenticated account lacking permission for vehicle V, when it requests V's live status, then the system denies the operation and does not disclose the location or vehicle state.
- **Telemetry degradation:** Given an offline tracker, when an authorized operator opens vehicle status, then the interface clearly distinguishes stale last-known data from a current reading, subject to the *accepted* freshness policy.
- **Boundary:** Given a rule with an approved upper limit L, when the measured value equals L, then the outcome follows the approved inclusive/exclusive definition; follow with L−δ and L+δ using a meaningful unit.

These are **candidate criteria**, not verified rules for any deployed system.

## Handoff, checks and limitations

Create a coverage matrix connecting AC → FR/BR/error/story → test case or checklist, with correct direction and explicit references. \`extensions/angent-ba/scripts/extract_markdown_graph.py\` supports an optional accepted AC table with \`ID\` and \`Criterion\` columns; a graph link check proves identity only, never execution.

The result should let a tester produce a reproducible fixture and a stakeholder decide whether observed behavior passes. Run actual automated tests only when the target environment and authorized tools exist; separate specification acceptance, test execution, release and customer validation. Revisions require a source-scoped diff and current permissions rather than a fictional fixed Claude L2 stage.
