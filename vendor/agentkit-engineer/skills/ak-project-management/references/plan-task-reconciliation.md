# Plan ↔ task reconciliation

## Hydration

When an active plan has unfinished work and a live task surface exists:

1. read unfinished plan items/phases;
2. create or map operational tasks with enough identity to trace them back;
3. preserve dependency and ownership information;
4. avoid duplicating tasks already representing the same work.

Hydration is a projection, not a second plan authoring process.

## During work

Operational task state may be useful for collaboration, but active semantic state also belongs in Continuity.

A task marked “done” is not enough when acceptance evidence is missing.

## Sync-back

Before claiming a plan/project complete:

1. sweep every relevant plan phase/item;
2. map verified operational completions back to their source plan items;
3. backfill stale earlier items;
4. update aggregate plan progress from reconciled evidence;
5. report completed work that cannot be mapped instead of silently dropping it.

## Resume

On a new session:
- recover Continuity;
- read the active plan;
- read current provider/task state;
- reconcile divergence;
- continue from the first valid unfinished item.

Provider state is evidence for coordination, while Continuity identifies what work was actively being pursued and why.
