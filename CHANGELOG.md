# Changelog

## Unreleased — core hardening

The previous ANGENT 1.0.0 “implementation/acceptance complete” state is superseded. Core implementation is active again and 1.0.0 remains unreleased.

### Cognitive core

- Added cumulative constraint evolution so a newer complaint does not silently discard still-active requirements.
- Added accepted-baseline repair semantics, protected-property preservation, affected-scope reasoning, dependency invalidation, and oscillation escalation.
- Added long-lived artifact state for reader capability, concept dependencies, terminology, depth, examples, prerequisite debt, coverage, and accepted revision state.
- Changed Quality from a single-position gate into solution, comparative-candidate, and endpoint/render phases.
- Added trust classes so retrieved external content cannot become instruction authority by imperative wording alone.
- Added Learning activation and recurrence semantics so stored lessons can be reopened when they fail to transfer.
- Added Continuity lifecycle and baseline/stale-work semantics.
- Fixed Continuity discovery so listing active work scans the same coherent immutable revisions used by per-work-item recovery.
- Separated Format representation ownership from Execution external-effect ownership.
- Strengthened whole-scope coverage semantics around pagination, truncation, filters, stale units, and unseen scope.

### Repository cleanup

- Removed every file under root `/tests`.
- Removed CI dependence on that suite; CI now performs committed-diff hygiene only.
- The removed suite was not considered behavioral evidence because it primarily checked static structure, strings, counts, and internally frozen inventories.

### Engineer boundary

Engineer fallback implementation is intentionally unchanged in this phase. Upstream inventory/parity refresh is deferred until the cognitive core is stabilized.

---

## 1.0.0 — previous candidate history

The notes below describe the earlier candidate state before core hardening reopened implementation. They are historical context, not current release-readiness evidence.


The candidate is under active core hardening and is not release-ready.

### Core hardening

- Added explicit constraint evolution so newer corrections do not silently erase still-active requirements.
- Added active-obligation preservation in Context.
- Added baseline-preserving repair semantics, protected properties, dependency invalidation and oscillation escalation in Reasoning.
- Added semantic artifact state for long-form and iterative Authoring.
- Reworked Quality around solution, comparative-candidate and endpoint concerns, including overcorrection/regression detection.
- Added trust boundaries between retrieved external content and task authority.
- Strengthened broad-audit coverage semantics for pagination, truncation and stale/recheck units.
- Added Continuity lifecycle, accepted-baseline pointers and recovery/discovery coherence.
- Added Learning activation and recurrence semantics.
- Clarified that Format defines destination representation while Execution owns external writes.
- Removed the root `tests/` suite that mainly asserted static structure, keywords and counts.
- Reduced the GitHub workflow to diff hygiene only; it is not behavioral acceptance evidence.

### Engineer

Engineer integration remains native-first / fallback-second.

Fallback inventory/parity is intentionally deferred until after the core-hardening phase. Historical completeness counts are not considered current upstream-parity evidence.

### Release boundary

Previous statements that implementation/acceptance were complete are superseded by this hardening work.

Do not publish, tag or describe 1.0.0 as released or implementation-complete until:

1. the core-hardening branch is reconciled into the intended canonical source;
2. the core architecture is read back for internal consistency;
3. the deferred Engineer inventory/parity phase is resolved;
4. the intended release surface/version strategy is explicitly approved.
