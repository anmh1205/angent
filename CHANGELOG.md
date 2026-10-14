# Changelog

## Unreleased — cognitive collaboration aligned, Engineer deferred

ANGENT 1.0.0 remains unreleased. Core hardening was integrated into main through PR #3 as squash commit 68f075b34c2b8948842d6bdf8aaaf14257db9733. Cognitive collaboration alignment was integrated through PR #5 as squash commit 8e94413d1460be5946e3d53083110c52a2817469.

### Cognitive collaboration alignment

- Added **Collaboration State** as task-relevant semantic state covering interaction mode, initiative/autonomy expectation, evidence/verification bar, explanation job, progress/checkpoint expectation and applicable working-method mechanisms.
- Kept collaboration state separate from authority, permanent user profile, project memory and Continuity.
- Added a **shared cognitive workspace** model so owner boundaries no longer imply a rigid one-way pipeline.
- Clarified that the workspace is conceptual semantics, not a new owner, database, event log, orchestrator or workflow engine.
- Restored Research's responsibility to return a **usable evidence-grounded subject-model delta** when a task requires relationships/mechanisms rather than flat citation inventory.
- Made Reasoning integrate TaskModel, collaboration state, evidence-grounded subject structure, hypotheses, decisions, observations and repair state into one coherent working model.
- Restored the long-lived distinction **full cognitive/subject model ≠ active teaching model ≠ presented model**.
- Made **information staging ≠ compression** and **point stated ≠ explanatory closure** explicit Authoring invariants.
- Extended Learning to promote conditional **working-method mechanisms** without turning collaboration history into preference rules.
- Updated cross-owner interface contracts so CollaborationState and subject-model deltas survive hand-offs when they matter.
- Preserved the existing owner set; no new top-level skill was introduced.

### Previously integrated core hardening

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

- Removed every file under root /tests as explicitly requested.
- Removed CI dependence on that suite; CI now performs committed-diff hygiene only.
- The removed suite mainly checked static structure, strings, counts, and internally frozen inventories and is not treated as behavioral acceptance evidence.

### Engineer boundary

Engineer implementation remains intentionally unchanged during cognitive-core alignment.

The next separate phase is to refresh native/fallback Engineer inventory/parity against current upstream while preserving canonical ANGENT cognitive semantics.

### Release boundary

1.0.0 is **not release-ready**.

Before any release:
1. complete the deferred Engineer inventory/parity refresh;
2. reconcile cross-harness behavior and the private ChatGPT package against the exact canonical source;
3. resolve the release/plugin identity/version strategy explicitly.

## Previous candidate history

Earlier PRs #1 and #2 established the pre-hardening 1.0.0 candidate and release-readiness documentation. Their “implementation/acceptance complete” status was superseded by the regression-focused core audit and PR #3.
