# Changelog

## Unreleased — core hardened, Engineer deferred

ANGENT 1.0.0 remains unreleased. Core hardening was integrated into `main` through PR #3 as squash commit `68f075b34c2b8948842d6bdf8aaaf14257db9733`.

### Cognitive core

- Added cumulative constraint evolution so a newer correction does not silently discard still-active requirements.
- Added accepted-baseline repair semantics, protected-property preservation, affected-scope reasoning, dependency invalidation, and oscillation escalation.
- Added sticky REPAIRING/UNSTABLE state across terse continuation/resume turns.
- Added long-lived artifact state for reader capability, concept dependencies, terminology, depth, examples, prerequisite debt, coverage, and accepted revision state.
- Changed Quality from a single-position gate into solution, comparative-candidate, and endpoint/render phases.
- Added trust classes separating factual/source authority from task/effect authority.
- Added Learning activation, recurrence, reopen/retire semantics, and dedicated user/project Learning persistence scopes.
- Added Continuity lifecycle, baseline pointers, stale/recheck state, repair state, and coherent immutable-revision discovery.
- Fixed Continuity discovery so listing active work and per-item recovery use the same durable revision source.
- Strengthened Execution around whole-scope enumeration evidence and retry churn.
- Separated Format representation ownership from Execution external-effect ownership.
- Strengthened broad-audit coverage semantics for pagination, truncation, filters, stale units, and unseen scope.
- Suppressed repetitive continuation chatter when no meaningful state delta exists.

### Repository cleanup

- Removed every file under root `/tests` as explicitly requested.
- Removed CI dependence on that suite; CI now performs committed-diff hygiene only.
- The removed suite mainly checked static structure, strings, counts, and internally frozen inventories and is not treated as behavioral acceptance evidence.

### Engineer boundary

Engineer implementation was intentionally not changed during core hardening.

The next phase is to refresh native/fallback Engineer inventory/parity against the current upstream while preserving the now-canonical ANGENT core semantics.

### Release boundary

Core hardening is complete and canonical, but 1.0.0 is **not release-ready**.

Before any release:
1. complete the deferred Engineer inventory/parity refresh;
2. reconcile cross-harness behavior and the private ChatGPT package against the exact canonical source;
3. resolve the release/plugin identity/version strategy explicitly.

## Previous candidate history

Earlier PRs #1 and #2 established the pre-hardening 1.0.0 candidate and release-readiness documentation. Their “implementation/acceptance complete” status was superseded by the regression-focused core audit and PR #3.
