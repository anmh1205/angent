---
name: ak-cook
description: Implement an accepted task or plan through a bounded inspect-plan-change-verify-review workflow, with mode-specific effort but invariant authority and quality gates.
metadata: {port: angent-fallback, mode: adapted}
---

# Cook — Portable Fallback

Cook is the main implementation workflow for an existing project.

Use `ak-bootstrap` for a greenfield project, `ak-plan` when the endpoint is a plan only, and `ak-fix` when a proven defect needs the smallest bounded repair.

## Entry contract

Before implementation, establish enough of:
- accepted outcome/plan or a clear bounded task;
- applicable `AGENTS.md`;
- non-goals and authority/effect boundary;
- owned files/modules and shared interfaces;
- acceptance evidence;
- unresolved material decisions;
- stop/replan conditions.

Do not code through an unresolved architecture/product decision merely to maintain momentum.

## Modes and modifiers

Preserve current stable semantics:

- **normal/direct** — inspect/research as needed, produce an implementation plan proportional to the task, implement, test, and review;
- **fast** — reduce research/planning overhead, not verification;
- **parallel** — execute genuinely independent phases concurrently only with explicit dependencies and non-overlapping ownership;
- **auto** — remove routine pauses inside the accepted contract, not authority/verification gates;
- **no-test** — skip the test stage only when explicitly selected; mandatory review remains and missing test evidence is reported;
- **tdd** — add tests-first behavior for relevant phases while preserving the selected base mode;
- **advice** — add advisory checkpoints when the active runtime exposes the required adviser route; advice does not implement, approve, or widen scope;
- **yagni** — challenge unneeded implementation scope while preserving requirements the Contract actually accepted.

Do not invent unsupported flag combinations. When exact invocation syntax matters, inspect the current installed Skill/help.

## Workflow

1. Inspect current project state and the affected dependency closure.
2. Resolve only the research needed for the implementation decision.
3. Build or load a reviewed plan sized to the work; even fast mode needs a coherent plan before code.
4. Implement in dependency order and preserve established project conventions.
5. When a large diff warrants it, simplify/refactor only inside the accepted behavior boundary.
6. Run tests unless no-test was explicitly selected.
7. Run an independent code-review pass in **every mode**.
8. Blocking test/review findings return to the owning diagnosis/implementation step; do not waive them to call the work done.
9. Reconcile plan/artifact state, documentation impact, changed files, checks, unresolved risk, and requested endpoint evidence.

## Parallel/runtime boundary

Parallel mode requires:
- actual independent work;
- explicit dependency graph;
- non-overlapping writable ownership;
- runtime capability that can preserve the required delegation/isolation semantics.

If those conditions are absent, do not label sequential work as parallel.

## Failure protocol

Unexpected failed verification is evidence that can invalidate the current plan.

Preserve the failure, identify whether it is implementation defect, stale assumption, environment/provider issue, or test/evaluator defect, and replan when needed.

Repeated attempts with no new evidence are a stall signal.

## Authority

Cook authorizes only implementation effects already inside the accepted project/task scope.

Auto/fast/parallel/no-test/tdd/advice/yagni do not grant:
- credentials;
- external spend;
- commits/push/PR/merge;
- publication/deployment;
- destructive actions;
- live-account or production-data effects;
- acceptance of a regression.

Git delivery and deployment remain separately bounded effects unless the Contract explicitly includes them.

## Completion

Implementation is not complete because files changed or one command passed.

Report:
- implemented scope;
- tests/checks performed or explicitly deferred;
- mandatory review result;
- unresolved blockers/risks;
- docs/usage impact;
- endpoint state actually established.
