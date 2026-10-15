# Implementation workflow

## 1. Inspect and bind the work unit

Read:
- applicable `AGENTS.md`;
- accepted plan/spec/requirements;
- existing code and adjacent conventions;
- relevant tests;
- current branch/worktree/provider state.

Confirm the next coherent work unit and its acceptance evidence.

For multi-step work, keep durable progress in the active plan/Continuity. Runtime task trackers are optional working views.

## 2. Scout before guessing

Before forming implementation assumptions:
- trace ownership/data/control flow when unclear;
- inspect existing helpers/utilities;
- inspect public interfaces/contracts touched;
- identify downstream consumers and migration state.

A "fast" mode may reduce breadth but does not allow blind editing.

## 3. Implement

Make the smallest coherent change.

For each phase/work unit:
- preserve accepted scope/non-goals;
- respect project patterns unless evidence justifies a change;
- keep generated/shared contracts consistent;
- avoid unrelated cleanup;
- run cheap compile/type/static checks at useful boundaries.

### TDD path

Where selected:
1. establish current/regression behavior in tests;
2. implement/refactor;
3. verify regression tests remain green;
4. add/adjust tests for new behavior;
5. run the phase gate.

### Parallel path

Delegate only branches with explicit non-overlapping/safely composable ownership and established prerequisites.

Record:
- worker scope;
- files/state owned;
- dependencies;
- expected evidence.

Integrate all accepted results before final verification. Worker completion messages are not endpoint evidence.

## 4. Review gate

In interactive mode, pause only at a meaningful decision/review boundary—not after every file.

In auto mode, continue when:
- scope/authority are still valid;
- no material decision is user-owned;
- verification/review gates are satisfiable.

New architecture, broadened scope, destructive/external effect, or unresolved safety trade-off returns to Reasoning/user decision as appropriate.

## 5. Test

Testing is required by default.

Use project-native checks and `ak-test` semantics:
- changed happy path;
- error/edge paths material to the change;
- regression protection;
- build/type/lint/integration/UI checks as applicable.

For a cross-layer change, reconcile the producer's contract with every affected consumer before calling it complete: data shape, error semantics, initialization/order, version compatibility, ownership and recovery may differ even when individual modules compile. Select tests based on the actual boundary where the accepted behavior must hold; consult Test's evidence-layer method rather than assuming a local green suite proves the end-to-end result.

A failing test is evidence, not a license to weaken the assertion. Diagnose non-obvious failures before changing code.

If tests are explicitly deferred, mark the result implemented-but-untested.

## 6. Independent code review

For material changes, use `ak-code-review` semantics after implementation/testing.

Review must check:
- acceptance/spec compliance;
- blast radius and indirect consumers;
- public contract breakage;
- security/reliability concerns;
- project-pattern consistency;
- verification sufficiency.

Repair accepted findings, retest, and re-review when needed. Repeated cycles without convergence trigger re-model/escalation rather than infinite patching.

## 7. Finalize

Before claiming a plan-backed or multi-step task complete:

1. reconcile the active plan with what was actually implemented;
2. sync verified completion to the task/project surface when one is in use;
3. update Continuity so no stale unfinished frontier remains;
4. verify earlier phases/items were not left stale while later work finished;
5. update only authoritative affected documentation when behavior/setup/contracts/architecture changed;
6. report intentionally deferred tests, unresolved mappings or known limitations;
7. verify the requested endpoint itself.

Journal/history capture is optional and evidence-driven, not mandatory ceremony.
