# Context assembly

Context should maximize decision signal, not token occupancy.

## Candidate inputs

- newest explicit user instruction;
- current conversation facts;
- active-work frontier from Continuity;
- active obligations from Contract/task state;
- collaboration state relevant to the current task;
- accepted baseline or artifact-state pointer when revision work depends on it;
- accepted positive/calibration baseline when a recurring quality complaint compares current behavior to prior good behavior;
- applicable AGENTS.md scope;
- project knowledge;
- user/global memory;
- project memory;
- promoted Learning mechanisms;
- retrieved historical/session evidence;
- live provider/source state when freshness matters.

## Start from the current decision

Ask what the next owner needs to decide or do.

Retrieve only context that can change task interpretation, constraints, collaboration method, available options, execution method, or communication/quality requirements. Active obligations that can constrain the next decision are mandatory context, not optional retrieval candidates.

## Correction reconstruction

For a one-off local defect, ordinary baseline/context may be enough.

For repeated, oscillating, method-level, or “you are doing this wrong again” feedback, retrieve enough prior evidence to answer:

- Has the same failure mechanism appeared before?
- What previous repair was attempted?
- What accepted/positive output did the user identify as better?
- Which working-method Learning mechanisms should already have applied?
- Is the latest example only one manifestation of a broader owner/interface/state-model failure?

Do not load the full chat history by default. Retrieve the smallest set that can distinguish a local defect from a recurring/systemic one.

## Collaboration reconstruction

When collaboration method matters, recover the smallest state that answers questions such as:

- Is this answer-only, research-first, audit-only, explanation-first, autonomous execution, verify-and-fix, or another task-specific mode?
- How much initiative is expected before a genuine decision boundary?
- What evidence or verification standard is expected?
- How should progress/checkpoints be surfaced?
- Which promoted working-method mechanisms actually apply to this decision class?

Prefer explicit current instructions over historical inference. Do not treat collaboration state as effect authorization.

## AGENTS.md scope

Apply project instructions relevant to the files/subtree being operated on while preserving applicable root instructions.

Do not copy AGENTS.md into memory merely because it was loaded.

## Provenance

Know whether material context is current instruction, prior preference, project instruction, canonical provider state, active task state, collaboration state, inferred memory, Learning guidance, recurrence evidence, or positive baseline.

## Freshness

Refresh when another session/process may have changed the state, a pointer/version is stale, or the next action depends on exact current state.

## Progressive disclosure

Prefer maps/pointers over large preloads.

Retrieve deeper source text when exact wording matters, compact memory lacks detail, recurrence/systemic interpretation needs historical evidence, conflict exists, or verification needs source evidence.

Return a compact state package with unresolved conflict explicitly preserved.
