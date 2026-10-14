# Resume and reconciliation

Resume is not “read an old summary and continue”.

## Recovery sequence

1. identify the active work item;
2. read the highest coherent continuity revision;
3. apply newest explicit instruction/current authority;
4. inspect pending/ambiguous effects that require reconciliation before safe replay;
5. recover saved long-running process/job/workflow identities, branch states and next informative observation conditions;
6. validate artifact/source pointers;
7. refresh external state that may change the next decision;
8. revalidate stale or time-sensitive decisive premises in the saved decision basis;
9. resolve conflicts/divergence;
10. return the reconciled frontier to Context/Reasoning;
11. let Reasoning recompute RUNNABLE, WAITING_EXTERNAL and BLOCKED branches;
12. continue from the highest-value unfinished valid RUNNABLE branch.

A saved decision remains usable only while its decisive basis remains valid enough for the next dependent action.

## External change

A provider may have changed while ANGENT was interrupted: branch HEAD advanced, issue moved, page edited, deployment changed, process/job completed, or another session completed work.

Do not discard the stored frontier. Reconcile it so completed/remaining work still has meaning.

If the external change invalidates a decisive premise, return to Reasoning rather than mechanically continuing the old plan.

## Running operations

If a saved operation was WAITING_EXTERNAL, preserve its operation identity and informative-observation condition.

Do not automatically poll every saved handle merely because the session resumed.

First determine whether:
- authoritative reconciliation is required before any safe action;
- the saved informative-observation condition is now satisfied;
- another runnable branch now depends on the result.

Execution performs the observation when Reasoning selects the branch. Reasoning decides whether independent work should proceed first.

If the operation no longer exists, distinguish provider retention/expiration from failure before deciding to relaunch.

## Concurrent sessions

A later timestamp does not automatically win.

Compare source versions, identify overlap, preserve independently verified disjoint work, and reconcile conflicting frontier/decision state before dependent action.

## Ambiguous effects

If a prior session may have performed a write but response was lost, query by target/operation identity and determine actual state before retry.

This reconciliation requirement can override ordinary wait scheduling because replay safety depends on establishing the prior effect.

## Stale artifacts and evidence

A saved pointer is not proof an artifact still exists or matches the saved version.

A saved decision basis is not proof its evidence is still current.

Validate what can change the next action before using saved state as current context.
