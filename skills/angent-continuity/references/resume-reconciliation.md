# Resume and reconciliation

Resume is not “read an old summary and continue”.

## Recovery sequence

1. identify the active work item;
2. read the highest coherent continuity revision;
3. apply newest explicit instruction/current authority;
4. reconstruct the resume binding needed by unfinished dependent work;
5. compare it with live canonical/provider state;
6. classify the mapping as COMPATIBLE, REVALIDATE, AMBIGUOUS or INCOMPATIBLE;
7. inspect pending/ambiguous effects that require reconciliation before safe replay;
8. recover saved long-running process/job/workflow identities, branch states and next informative observation conditions;
9. validate artifact/source pointers;
10. refresh external state that may change the next decision;
11. revalidate stale or time-sensitive decisive premises in the saved decision basis;
12. return the reconciled frontier to Context/Reasoning;
13. let Reasoning recompute RUNNABLE, WAITING_EXTERNAL and BLOCKED branches;
14. continue only from an unfinished branch whose required binding is compatible or has completed revalidation.

A saved decision remains usable only while its decisive basis remains valid enough for the next dependent action.

## Compatibility before continuation

Load resume-binding.md when saved work depends on exact target/effect/baseline/capability identity.

- COMPATIBLE → continue after ordinary freshness/authority checks.
- REVALIDATE → mark affected work stale/recheck and rebuild the changed premise/dependency before continuation.
- AMBIGUOUS → fail closed for the dependent transition and inspect authoritative state.
- INCOMPATIBLE → do not continue the old dependent plan; establish a new baseline/action model or migration.

Do not classify the whole task from one changed timestamp or version. Judge the dependency closure that the saved work actually relies on.

## External change

A provider may have changed while ANGENT was interrupted: branch HEAD advanced, issue moved, page edited, deployment changed, process/job completed, capability semantics changed, or another session completed work.

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

Compare source versions and semantic overlap, preserve independently verified disjoint work, and classify only the overlapping dependency closure.

If overlap is partial and the provider/canonical state cannot establish whether saved work is still valid, treat that dependent path as AMBIGUOUS rather than guessing a winner.

## Ambiguous effects

If a prior session may have performed a write but response was lost, query by target/operation identity and determine actual state before retry.

This reconciliation requirement can override ordinary wait scheduling because replay safety depends on establishing the prior effect.

## Stale artifacts and evidence

A saved pointer is not proof an artifact still exists or matches the saved version.

A saved decision basis is not proof its evidence is still current.

Validate what can change the next action before using saved state as current context.
