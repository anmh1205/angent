# Shared cognitive workspace

The cognitive workspace is ANGENT's semantic integration model. It prevents owner boundaries from turning into a rigid workflow.

It is not a storage engine, runtime object, database, event log, orchestrator, or new top-level skill.

## Purpose

At any moment, ANGENT should be able to reason from one coherent view of the work rather than from disconnected packets produced by earlier owners.

The workspace may contain, only when relevant:

- TaskModel and active obligations;
- collaboration state;
- current problem/system model;
- evidence-grounded subject model;
- live hypotheses and residual uncertainty;
- current decision and reconsideration trigger;
- adaptive plan;
- RepairModel and protected properties;
- relevant reader/artifact-state pointers;
- stale/dependent work markers;
- latest observations that can change the model.

The complete internal state of each owner does not belong here.

## Owner updates

Each owner changes only the semantics it owns:

- Contract changes task boundary, obligation and authority semantics.
- Context changes reconstructed working/collaboration state and provenance.
- Research changes evidence and evidence-grounded subject structure.
- Reasoning changes problem/system/hypothesis/decision/plan/repair state.
- Execution changes observed external state.
- Authoring changes reader-facing candidate and artifact semantics.
- Quality changes verdicts, not producer state.
- Continuity persists the compact resume-critical subset.
- Learning changes reusable future mechanisms after promotion.

## Not a pipeline

No owner is “finished forever” because another owner ran.

Examples:

- Research finds evidence that changes the problem boundary → return to Contract/Reasoning as needed.
- Authoring cannot explain a relation because the underlying model is underspecified → return to Reasoning/Research.
- Execution observes a false precondition → Reasoning replans.
- Quality finds a factual/model defect → return to the earliest responsible owner, not to a prose patch.
- A current instruction changes interaction mode → Context updates collaboration state without discarding unrelated verified work.

## Model breadth

Keep the full cognitive model rich enough for correct reasoning, but activate only the subset needed for the current decision.

This distinction is critical:

full cognitive model ≠ active working model ≠ presented model.

Narrowing the active model reduces competing concepts. It does not justify compressing away the mechanism needed to understand the active relation.

## Harness boundary

ANGENT defines these semantics. The harness may represent them in prompt context, structured state, files, memory, or another mechanism.

Do not build runtime infrastructure merely to mirror this conceptual workspace.
