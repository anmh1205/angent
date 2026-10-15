# Durable plan meaning and source ownership

A plan must survive runtime/tool changes and a fresh session **through its authoritative project source**. A file is a good source when the project uses files; an issue/spec/Notion plan can be the authority when the team already works there. Choose the canonical owner before creating artifacts. A portable Skill must not make a duplicate `plan.md` into a second competing source of truth.

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

An index/dashboard is not automatically the owner of plan meaning. If an issue or document system owns it, retain the decisive reasons and acceptance evidence there (or in stable linked documents), rather than assuming a parallel local file outranks it.

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
- authoritative artifact/provider pointer;
- acceptance criteria;
- open risks/blockers;
- authority granted for the next stage.
