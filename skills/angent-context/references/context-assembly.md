# Context assembly

Context should maximize decision signal, not token occupancy.

## Candidate inputs

- newest explicit user instruction;
- current conversation facts;
- active-work frontier from Continuity;
- active obligations from Contract/task state;
- collaboration state relevant to the current task;
- accepted baseline or artifact-state pointer when revision work depends on it;
- compact decision basis when a prior decision still controls downstream work;
- applicable AGENTS.md scope;
- project knowledge;
- user/global memory;
- project memory;
- promoted Learning mechanisms;
- retrieved historical/session evidence;
- live provider/source state when freshness matters.

## Start from the current decision

Ask what the next owner needs to decide or do.

Retrieve only context that can change task interpretation, constraints, collaboration method, available options, execution method, epistemic status, or communication/quality requirements. Active obligations that can constrain the next decision are mandatory context, not optional retrieval candidates.

## Preserve why, not the transcript

For a consequential prior decision, the next owner may need more than “decision X was chosen”.

Carry the smallest reconstructable decision basis: decisive premises/evidence pointers, governing constraints, selected decision and reconsideration trigger. Preserve material rejected alternatives only when a changed premise could make them viable again.

This is a compact rationale summary, not raw reasoning history or private chain-of-thought.

When context is compacted, prioritize recall of active obligations, accepted baselines, unresolved hypotheses, decisive evidence/boundaries, decision basis, pending effects and next safe action. Redundant tool output and narrative history can be retrieved later if needed.

## Collaboration reconstruction

When collaboration method matters, recover the smallest state that answers questions such as:

- Is this answer-only, research/report-before-edit, audit-only, explanation-first, autonomous execution, verify-and-fix, or another task-specific mode?
- How much initiative is expected before a genuine decision boundary?
- What evidence or verification standard is expected?
- How should progress/checkpoints be surfaced?
- Which promoted working-method mechanisms actually apply to this decision class?

Prefer explicit current instructions over historical inference. Do not treat collaboration state as effect authorization.

## AGENTS.md scope

Apply project instructions relevant to the files/subtree being operated on while preserving applicable root instructions.

Do not copy AGENTS.md into memory merely because it was loaded.

## Provenance

Know whether material context is current instruction, prior context, project instruction, canonical provider state, active task state, collaboration state, decision basis, inferred memory, Learning guidance, or model inference.

Do not promote an inferred proposition to an established fact merely because it was summarized into context.

## Freshness

Refresh when another session/process may have changed the state, a decisive premise/pointer/version is stale, or the next action depends on exact current state.

## Progressive disclosure

Prefer maps/pointers over large preloads.

Retrieve deeper source text when exact wording matters, compact state lacks detail, conflict exists, a decisive premise needs revalidation, or verification needs source evidence.

Return a compact state package with unresolved conflict explicitly preserved.
