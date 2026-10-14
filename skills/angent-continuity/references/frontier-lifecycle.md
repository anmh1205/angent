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

Track repair state separately from lifecycle:

- **NONE** — no active repair loop;
- **REPAIRING** — a candidate is being revised against an accepted baseline;
- **UNSTABLE** — recurrence/oscillation shows that local patching is not reliable and Reasoning must re-establish the controlling model before ordinary production resumes.

A terse continuation does not clear REPAIRING/UNSTABLE state.

Repair-state transitions:

~~~text
NONE → REPAIRING        when revision against an accepted baseline begins
REPAIRING → NONE        when comparative Quality accepts the new baseline
REPAIRING → UNSTABLE    when recurrence/oscillation invalidates local repair confidence
UNSTABLE → REPAIRING    after Reasoning re-establishes the controlling model and bounded repair
UNSTABLE → NONE         only when the repair task is explicitly superseded/abandoned or a stable accepted baseline is established
~~~

## Persist semantics, not transcripts

A frontier should preserve:

- outcome and current phase;
- active obligations/invariants;
- verified completed units;
- current unfinished unit;
- consequential decisions;
- compact decision basis/pointer when later work depends on why a decision remains valid;
- accepted baseline or artifact-state pointer/digest when revisions depend on it;
- collaboration-state pointer/subset only when losing it would materially change resume behavior;
- stale/recheck units caused by changed dependencies or decisive evidence;
- unresolved dependencies;
- pending or ambiguous external effects;
- source/provider versions needed for reconciliation;
- next safe action.

Large authoring/research models and complete collaboration/history models should remain with their owning context/artifact/store. Continuity persists a compact pointer, digest and the subset needed to resume safely.

Do not persist raw private reasoning. A recovered decision basis or collaboration-state pointer does not override newer authority or live evidence.

## Discovery must match recovery

The mechanism used to list active work must discover the same highest coherent revisions that per-work-item recovery would load.

Do not rely only on a convenience pointer that may lag an already-written immutable revision after interruption.

## Advance boundaries

Create a new frontier revision when meaning changes:

- a coherent work unit completes;
- scope/obligation changes;
- accepted baseline changes;
- collaboration mode materially changes ongoing work;
- a decisive premise/evidence boundary changes;
- a dependency invalidates completed work;
- a consequential decision changes downstream work;
- an external effect is reconciled;
- lifecycle changes;
- handoff/compaction occurs.

Do not persist every read or every wording edit.

## Completion

Mark COMPLETED only when the Contract endpoint is verified.

A summary, commit, page write or tool success is not a lifecycle completion event unless it is itself the requested endpoint.
