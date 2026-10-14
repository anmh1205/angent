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
- live provider/source state when freshness matters;
- canonical role→provider/source identity mapping when stale aliases or superseded objects can change the decision.

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

## Reader-state reconstruction for continuing documents

When continuing or revising a multi-unit teaching artifact, recover the accepted artifact/curriculum pointer: which concepts were previewed versus made usable, the reader capability already supported, unresolved prerequisite debt, protected successful explanations, and downstream dependencies. Do not reconstruct reader mastery from chapter titles, keyword matches, content length, or a self-reported VERIFIED label. Refresh the affected canonical units when their content or revision changed; retrieve only the units needed to establish the next capability boundary.

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

## Canonical target resolution

A remembered provider ID, old URL, prior release, archived object, or historical checkpoint is not automatically the current target.

When the user's target is a semantic role such as current/canonical/production/private/latest-for-this-project and provider identity can drift:
- resolve the role from current user/project/provider source-of-truth;
- preserve the resolved identity/version and mapping provenance;
- carry any material conflict instead of guessing from recency or familiarity.

When the user names one exact provider identity or historical object, keep that exact identity unless current authority changes the task.

Load `canonical-identity.md` for detailed boundaries.

## Freshness

Refresh when another session/process may have changed the state, a pointer/version is stale, or the next action depends on exact current state.

## Decision-point sufficiency

Before a consequential decision or effect, ask whether omitted context could plausibly change:
- current authority or exclusions;
- resolved target/scope and canonical role→identity binding when relevant;
- a decisive premise;
- a protected property;
- a dependency that makes the selected branch unsafe or stale.

Retrieve only the missing state that can change that decision. This is a sufficiency check, not permission to reload the entire history.

A context package that was sufficient when a plan was formed can become insufficient after a new user instruction, another branch effect, provider drift, resume, or argument transformation.

## Progressive disclosure

Prefer maps/pointers over large preloads.

Retrieve deeper source text when exact wording matters, compact memory lacks detail, recurrence/systemic interpretation needs historical evidence, conflict exists, or verification needs source evidence.

Return a compact state package with unresolved conflict explicitly preserved.
