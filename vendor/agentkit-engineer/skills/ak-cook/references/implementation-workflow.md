# Implementation workflow

1. Inspect existing code, tests and project instructions.
2. Confirm the next work unit and its acceptance condition.
3. Implement the smallest coherent change.
4. Keep unrelated cleanup separate.
5. Add/update tests where behavior changed.
6. Run targeted verification.
7. Expand verification according to blast radius.
8. Ask Code Review for independent review when the change is material.
9. Update Continuity frontier for long work.
10. Continue to the next dependent work unit while authorized/runnable.

For parallel work, assign non-overlapping ownership and integrate before final verification.

## Finalize

Before claiming a plan-backed or multi-step task complete:

1. reconcile the active plan with what was actually implemented;
2. sync verified completion to the task/project surface when one is in use;
3. update Continuity so no stale unfinished frontier remains;
4. verify earlier phases/items were not left stale while later work finished;
5. check whether architecture/API/setup documentation became inaccurate and update only the authoritative affected docs when needed;
6. report any intentionally deferred test, unresolved mapping or known limitation.

Do not make journal creation mandatory for every successful task. Journal only when the work creates historical evidence worth retaining.

A generated patch, commit, task transition or specialist success message is progress, not the endpoint unless the task contract says so.
