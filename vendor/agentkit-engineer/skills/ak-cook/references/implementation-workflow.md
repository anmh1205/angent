# Implementation workflow

## Establish the work unit

1. Inspect existing code, tests, project instructions, and current accepted plan/task.
2. Confirm the next dependency-valid work unit and its observable acceptance condition.
3. Preserve unrelated work and shared-interface constraints.
4. When the selected mode requires a plan, ensure one coherent plan exists before implementation; fast mode may shorten planning but does not remove it.

## Implement

1. Make the smallest coherent change that advances the accepted outcome.
2. Keep unrelated cleanup separate unless it is a proven prerequisite.
3. Add or update tests when behavior changes unless no-test was explicitly selected.
4. For TDD mode, establish the failing behavioral test before the implementation when the behavior is testable that way.
5. For parallel mode, assign non-overlapping ownership and integrate dependency-valid outputs before final verification.
6. If evidence invalidates the plan/architecture, return to Reasoning instead of coding around the mismatch.

## Verify and review

1. Run targeted verification.
2. Expand verification according to blast radius and project/release gates.
3. Run Code Review in **every Cook mode**.
4. Treat blocking review findings as dependencies: return them to the correct implementation/debug owner and reverify affected behavior.
5. Do not let no-test, fast, auto, advice, YAGNI, or parallel modes weaken mandatory review or authority boundaries.

## Finalize

Before claiming a plan-backed or multi-step task complete:

1. reconcile the active plan with what was actually implemented;
2. sync verified completion to the task/project surface when one is in use;
3. update Continuity so no stale unfinished frontier remains;
4. verify earlier units were not left stale while later work finished;
5. check whether architecture/API/setup documentation became inaccurate and update only authoritative affected docs when in scope;
6. report deferred tests, unresolved mappings, evidence gaps, or known limitations explicitly.

Do not make journal creation mandatory for every successful task. Journal only when the work creates historical evidence worth retaining.

A generated patch, commit, task transition, worker report, or command success is progress evidence, not the endpoint unless the Contract says so.
