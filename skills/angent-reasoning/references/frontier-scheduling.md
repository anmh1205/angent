# Frontier scheduling

ANGENT should not let one pending external operation monopolize the cognitive loop.

This is a reasoning semantic, not a runtime scheduler. The harness may execute only one tool call at a time; ANGENT can still choose useful work from another independent branch between observations.

## Branch states

For non-trivial work with several possible next actions, Reasoning may view the active frontier as branches:

- **RUNNABLE** — all prerequisites for useful progress are currently satisfied;
- **WAITING_EXTERNAL** — progress depends on an external operation/event whose next informative observation condition is not yet satisfied;
- **BLOCKED** — progress cannot continue because a missing decision, authority, capability, prerequisite, or unresolved failure prevents a safe next action;
- **DONE** — the branch's required endpoint is verified.

These are semantic planning states. They do not require a queue service or scheduler database.

A whole task is BLOCKED only when no required branch is RUNNABLE and every unfinished path is blocked/waiting in a way that cannot currently produce useful progress.

## Work-conserving selection

After every observation that changes a branch to WAITING_EXTERNAL:

1. record the operation/dependency identity and its next informative observation condition;
2. recompute the active frontier before making another tool call;
3. exclude WAITING_EXTERNAL branches whose observation condition is not satisfied;
4. if any RUNNABLE branch can advance the Contract outcome, choose useful work from that set;
5. return to the waiting branch only after its informative-check condition becomes true or another branch now materially depends on the result;
6. if no RUNNABLE work exists and no waiting branch is yet informative to recheck, persist the frontier and stop issuing equivalent tool calls.

Do not choose the same pending branch merely because it was the most recent action.

## Useful independence

Independent work is work whose correctness does not depend on the pending result and that advances the requested endpoint.

Examples:
- inspect another file/module while a build runs;
- prepare a migration mapping while a provider job runs;
- audit another independent chapter while a long export runs;
- update task state or reconcile already-established evidence while CI runs;
- investigate a second hypothesis that does not depend on the pending operation.

Do not manufacture busywork. A branch is RUNNABLE only when it can create task-relevant progress.

Independence is a reasoning conclusion, not a permanent branch property. Preserve the dependency/shared-state assumptions that matter. After a material observation or effect changes shared state, recompute affected branch states before selecting from the old runnable set.

A branch can move RUNNABLE → BLOCKED/STALE when another branch changes a prerequisite, and a blocked/waiting branch can become RUNNABLE when a dependency is satisfied.

## Decision joins

Independent execution does not imply independent acceptance.

Several branches can run independently yet converge on one later decision. When unresolved branch output can materially reverse that decision, preserve the dependency instead of treating the first completed branch as sufficient by default.

A decision join is semantic, not a runtime barrier:
- identify which branch results remain decision-relevant;
- synthesize completed results by provenance/evidence strength, not arrival order;
- allow early decision when it is robust across credible outcomes of the unfinished branches;
- otherwise keep only the dependent decision/work blocked while unrelated RUNNABLE work continues.

Do not wait for every branch merely to satisfy a fan-out count.

## Recheck eligibility

A WAITING_EXTERNAL branch becomes eligible for another observation only when a stated condition is satisfied, such as:

- enough real time has passed relative to the operation's expected behavior;
- the provider emitted a completion/event signal;
- another branch has reached a point that requires this result;
- a deadline/timeout boundary is now decision-relevant;
- the user explicitly requests current status;
- a previously recorded observation trigger is now true.

“Status endpoint exists” and “the previous call returned pending” are not eligibility conditions.

## No-progress recurrence

Repeatedly observing the same pending state without a new trigger is evidence that scheduling failed.

Do not repair this by merely increasing a sleep interval or adding a larger polling threshold. Check whether:
- WAITING_EXTERNAL state was represented;
- the branch was excluded from runnable selection;
- independent branches were discovered;
- Root/Reasoning re-entered after the pending observation;
- Continuity preserved the wait condition across compaction/resume;
- a competing instruction incorrectly forced serial execution.

## Interruption boundary

If the host cannot keep working after the turn ends, ANGENT must not claim background progress.

Within an active turn, however, waiting on one branch does not justify idling when other independent work is runnable.
