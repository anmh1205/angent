# Changelog

## Unreleased — cognitive collaboration aligned, reliability hardening active

ANGENT 1.0.0 remains unreleased as a project release. Core hardening was integrated through PR #3. Cognitive collaboration alignment was integrated through PR #5. Long-running wait/poll discipline was restored through PR #6 after a live regression exposed behavior lost from Cogent Chat Work.

### Reliability hardening

- Restored **no-tight-poll** behavior for long-running processes/jobs/workflows.
- Added explicit WAITING versus RUNNABLE semantics so an external dependency does not monopolize the work loop while independent useful work remains.
- Added long-running operation identity/handle state to Continuity for safe resume and reconciliation.
- Defined unchanged RUNNING/PENDING observations as no-progress rather than completed work.
- Added general **progress/stall semantics** to Reasoning: evidence/model/dependency/accepted-work/endpoint/uncertainty deltas count as progress; repeated activity without such a delta triggers re-model/replan.
- Added scenario-based **behavioral regression evaluation** under Quality, grounded in real failures, corrections, positive calibration and accepted behavior.
- Evaluation now follows ownership boundaries: deterministic mechanics can use deterministic tests; model behavior requires representative model/session evidence; provider behavior requires provider/integration evidence.
- Restored calibration-before-scale as a method-quality principle without reviving static/count test gates.
- Kept these changes semantic: no progress service, polling daemon, trace backend, event ledger, or new top-level owner was added.

### Cognitive collaboration alignment

- Added **Collaboration State** as task-relevant semantic state covering interaction mode, initiative/autonomy expectation, evidence/verification bar, explanation job, progress/checkpoint expectation and applicable working-method mechanisms.
- Kept collaboration state separate from authority, permanent user profile, project memory and Continuity.
- Added a **shared cognitive workspace** model so owner boundaries no longer imply a rigid one-way pipeline.
- Restored Research's responsibility to return a **usable evidence-grounded subject-model delta** when a task requires relationships/mechanisms rather than flat citation inventory.
- Made Reasoning integrate TaskModel, collaboration state, evidence-grounded subject structure, hypotheses, decisions, observations and repair state into one coherent working model.
- Restored the long-lived distinction **full cognitive/subject model ≠ active teaching model ≠ presented model**.
- Made **information staging ≠ compression** and **point stated ≠ explanatory closure** explicit Authoring invariants.
- Extended Learning to promote conditional **working-method mechanisms** without turning collaboration history into preference rules.
- Preserved the existing owner set; no new top-level skill was introduced.

### Previously integrated core hardening

- Added cumulative constraint evolution so a newer correction does not silently discard still-active requirements.
- Added accepted-baseline repair semantics, protected-property preservation, affected-scope reasoning, dependency invalidation, and oscillation escalation.
- Added sticky REPAIRING/UNSTABLE state across terse continuation/resume turns.
- Added long-lived artifact state for reader capability, concept dependencies, terminology, depth, examples, prerequisite debt, coverage, and accepted revision state.
- Changed Quality from a single-position gate into solution, comparative-candidate, and endpoint/render phases.
- Added trust classes separating factual/source authority from task/effect authority.
- Added Learning activation, recurrence, reopen/retire semantics, and dedicated user/project Learning persistence scopes.
- Added Continuity lifecycle, baseline pointers, stale-dependency state and coherent immutable-revision discovery.
- Strengthened Execution around whole-scope enumeration evidence and retry churn.
- Separated Format representation ownership from Execution external-effect ownership.
- Strengthened broad-audit coverage semantics for pagination, truncation, filters, stale units, and unseen scope.

### Repository validation policy

- Root /tests remains removed.
- CI remains hygiene-only.
- Static string/count/self-consistency checks are not treated as behavioral acceptance evidence.
- Behavioral reliability is evaluated with scenario properties, representative live runs/session evidence and provider state appropriate to the ownership boundary.

### Engineer boundary

Engineer implementation remains intentionally separate from cognitive/reliability hardening.

The next Engineer phase must refresh native/fallback inventory/parity against current upstream without weakening the integrated cognitive semantics.

### Private plugin boundary

The private ChatGPT plugin may be updated under explicit user authorization as an evaluation surface and can carry a patch version higher than the unreleased project version.

Private plugin update/read-back does not mean the project is public-release-ready.

## Previous candidate history

Earlier PRs #1 and #2 established the pre-hardening 1.0.0 candidate and release-readiness documentation. Their “implementation/acceptance complete” status was superseded by later regression-focused audits.
