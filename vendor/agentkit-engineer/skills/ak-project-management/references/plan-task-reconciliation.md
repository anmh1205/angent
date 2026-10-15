# Plan ↔ task reconciliation

## Hydration

When an active plan has unfinished work and a **different** optional operational task surface exists:

1. read unfinished plan items/phases;
2. create or map operational tasks with enough identity to trace them back;
3. preserve dependency and ownership information;
4. avoid duplicating tasks already representing the same work.

Hydration is a projection, not a second plan authoring process. If the live issue/plan provider **already owns the authoritative work items**, there is nothing to hydrate from a second file plan: use that source directly.

## During work

Operational task state may be useful for collaboration, but active semantic state also belongs in Continuity.

A task marked “done” is not enough when acceptance evidence is missing.

## Sync-back

Before claiming a plan/project complete:

1. identify the authoritative plan/issue owner and its relevant phases/items;
2. match completed operational work with exact acceptance evidence and owning items;
3. reconcile predecessor and dependent items whose status has become stale;
4. derive aggregate completion only if the whole requested scope was inspected and reconciled;
5. report completed work with no trustworthy source mapping instead of inventing one.

## Resume

On a new session:
- recover Continuity;
- read the active plan;
- read current provider/task state;
- reconcile divergence;
- continue from the first valid unfinished item.

Provider state is evidence for coordination, while Continuity identifies what work was actively being pursued and why.
