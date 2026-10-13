# Frontier lifecycle and semantic persistence

Continuity persists active work; it should not become a second copy of every owner's internal state.

## Lifecycle

A work item has one lifecycle state:

- **ACTIVE** — runnable work remains;
- **PAUSED** — intentionally stopped with a known continuation point;
- **BLOCKED** — cannot advance until an external dependency or decision changes;
- **COMPLETED** — requested endpoint was verified;
- **SUPERSEDED** — replaced by a newer work item or scope;
- **ABANDONED** — explicitly discontinued.

Only ACTIVE, PAUSED and BLOCKED items are candidates for normal resume.

## Persist semantics, not transcripts

A frontier should preserve:

- outcome and current phase;
- active obligations/invariants;
- verified completed units;
- current unfinished unit;
- consequential decisions;
- accepted baseline or artifact-state pointer/digest when revisions depend on it;
- stale/recheck units caused by changed dependencies;
- unresolved dependencies;
- pending or ambiguous external effects;
- source/provider versions needed for reconciliation;
- next safe action.

Large authoring/research models should remain with their owner artifact/store. Continuity persists a compact pointer, digest and the subset needed to resume safely.

## Discovery must match recovery

The mechanism used to list active work must discover the same highest coherent revisions that per-work-item recovery would load.

Do not rely only on a convenience pointer that may lag an already-written immutable revision after interruption.

## Advance boundaries

Create a new frontier revision when meaning changes:

- a coherent work unit completes;
- scope/obligation changes;
- an accepted baseline changes;
- a dependency invalidates completed work;
- a consequential decision changes downstream work;
- an external effect is reconciled;
- lifecycle changes;
- handoff/compaction occurs.

Do not persist every read or every wording edit.

## Completion

Mark COMPLETED only when the Contract endpoint is verified.

A summary, commit, page write or tool success is not a lifecycle completion event unless it is itself the requested endpoint.
