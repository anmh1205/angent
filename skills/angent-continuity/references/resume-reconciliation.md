# Resume and reconciliation

Resume is not “read an old summary and continue”.

## Recovery sequence

1. identify the active work item;
2. read the highest coherent continuity revision;
3. establish whether the persisted state comes from a trusted/verified storage boundary; if integrity or ownership is uncertain, downgrade it to historical evidence and verify dependent facts before use;
4. apply newest explicit instruction/current authority;
5. reconstruct the resume binding needed by unfinished dependent work;
6. compare it with live canonical/provider state;
7. classify the mapping as COMPATIBLE, REVALIDATE, AMBIGUOUS or INCOMPATIBLE;
8. inspect pending/ambiguous effects that require reconciliation before safe replay;
9. recover saved long-running process/job/workflow identities, branch states and next informative observation conditions;
10. validate artifact/source pointers;
11. refresh external state that may change the next decision;
12. revalidate stale or time-sensitive decisive premises in the saved decision basis;
13. return the reconciled frontier to Context/Reasoning;
14. let Reasoning recompute RUNNABLE, WAITING_EXTERNAL and BLOCKED branches;
15. continue only from an unfinished branch whose required binding is compatible or has completed revalidation.

A saved decision remains usable only while its decisive basis remains valid enough for the next dependent action.

## Resolve the correct active workstream before using a checkpoint

A valid but stale checkpoint can describe an earlier phase or a sibling audit. Neither the last assistant summary nor the latest timestamp is sufficient to select the continuation branch.

1. Identify the exact workstream and expected outcome named by the user's current instruction.
2. Discover candidate frontiers from revisioned Continuity records, current worktrees/branches and HEADs, recent commits, provider change history, open PRs/issues and the most recent meaningful tool actions.
3. Distinguish the **canonical base** (often `main`) from the **active working branch**. A checkpoint with `source_of_truth.branch: main` does not imply all unfinished work is on main.
4. Compare candidates by stable task identity, scope, verified work units and dependency/effect evidence. Select the task-matching live frontier, not an adjacent audit with a newer narrative.
5. Reconcile saved coverage with actual committed changes and operations. Verified commits after the checkpoint advance that frontier; they do not erase applicable invariants or independently verified work.
6. A source file read for the next batch is evidence of exploration, not proof that the batch was ported or accepted. Restore the first **unfinished** unit, not the last touched file.
7. If several plausible workstreams remain, preserve each separately; mark only overlapping dependencies ambiguous. Validate the selected exact branch/HEAD and unfinished scope before a dependent write.

When the chosen branch and checkpoint disagree, report the discrepancy and correct the active frontier record at a meaningful checkpoint rather than silently continuing the stale phase.

## Recovered-state trust

Coherent revision order establishes storage consistency, not snapshot authenticity.

A checkpoint copied from an untrusted file, client, issue/document, arbitrary project artifact, or other externally writable source must not silently become active Continuity state merely because it matches the schema.

Current explicit authority is always re-established from the live interaction/Contract. Saved effect intent, verification claims, decision basis and artifact pointers are used only to the strength justified by their provenance and current read-back.

When state trust is uncertain but its information may still help, preserve it as a hypothesis/historical hint and verify the load-bearing fields rather than discarding all progress or trusting all of it.

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
