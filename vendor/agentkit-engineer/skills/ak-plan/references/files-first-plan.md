# Files-first plan

A durable plan should survive runtime/tool changes and a fresh session.

## Minimum semantic structure

Record:
- objective;
- requested scope and non-goals;
- constraints/invariants;
- current-state summary with evidence pointers;
- accepted decisions;
- load-bearing assumptions and refresh/replan triggers;
- architecture/solution shape;
- phase/work-unit list;
- dependency graph/order;
- files/modules/interfaces/state involved;
- migration/rollback/compatibility state when material;
- acceptance/verification per phase;
- risks and mitigations;
- unresolved decisions;
- progress state when the plan is used for active execution.

A database/dashboard may index the plan but must not be the only place where the plan meaning exists.

## Phase quality

Each phase should answer:

- what capability/state becomes true;
- why this phase exists now;
- what it depends on;
- what it owns/touches;
- what must not change;
- how to implement the change;
- what evidence proves completion;
- what observation invalidates the phase/plan.

Avoid phase files that are merely filenames or TODO inventories.

## Handoff

A successor should be able to execute the plan without replaying the planning conversation.

Carry a compact handoff:
- goal;
- approved scope/non-goals;
- decisive evidence/decisions;
- artifact path;
- acceptance criteria;
- open risks/blockers;
- authority granted for the next stage.
