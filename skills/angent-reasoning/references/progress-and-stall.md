# Progress and stall semantics

ANGENT must distinguish activity from state advancement.

This is a reasoning semantic, not a runtime progress service or fixed workflow ledger.

## Material progress

Recent work counts as material progress when it changes at least one decision-relevant state:

- **evidence delta** — a material fact/observation is established, weakened, contradicted, or bounded;
- **model delta** — a hypothesis, causal relation, boundary, assumption, or decision model materially changes;
- **dependency delta** — a blocker or prerequisite is resolved, invalidated, or newly localized;
- **accepted-work delta** — verified implementation/artifact state advances toward the requested endpoint;
- **endpoint-evidence delta** — evidence that the requested outcome is actually satisfied becomes stronger;
- **uncertainty delta** — uncertainty that could change the action is materially reduced or correctly reframed.

A tool call, search, commit, generated page, status message, review pass, or count increase is not progress merely because it occurred.

## No-progress pattern

Suspect stall when several consecutive actions:

- return equivalent observations;
- repeat the same search or patch strategy;
- produce candidate rewrites with the same rejected mechanism;
- add sources without changing the subject/decision model;
- add implementation churn without moving endpoint evidence;
- keep circling the same unresolved dependency.

Do not require a universal numeric threshold. Task scale and action cost differ.

## Response to stall

When stall is credible:

1. stop the repeated tactic;
2. identify what state failed to change;
3. ask whether the model, evidence question, ownership boundary, dependency graph, or action choice is wrong;
4. choose an action with a plausible discriminating or unblocking effect;
5. if no such action exists, surface the genuine blocker instead of manufacturing activity.

A stall is a signal to re-model or replan, not a command to add ceremony.

## WAITING versus stalled

A dependency may be WAITING because an external process/job/provider result is not yet available.

WAITING is healthy when:
- the operation identity is preserved;
- dependent work is paused;
- independent work can still make progress;
- another status check is deferred until it can add information.

It becomes a stall/churn problem when the agent repeatedly checks the same state or performs pseudo-work that does not advance any other dimension.

## Research stall

Research is stalled when more retrieval repeats established facts without changing a live hypothesis, model relation, scope boundary, or decision.

Return to the research question: what evidence could actually distinguish the alternatives or change the decision?

## Repair stall

Repair is stalled when successive candidates alternate between failure dimensions or repeat the same mechanism under different wording/structure.

Escalate to repair-and-regression systemic analysis.

## Authoring stall

Authoring is stalled when text grows or is repeatedly rewritten but the target reader capability does not advance.

Return the unresolved model/prerequisite/representation problem to Reasoning/Research when needed.

## Evaluation stall

Quality should not request another near-identical local patch after evidence shows recurrence/oscillation. Return the finding to the earliest controlling owner.

## Persistence

Persist progress state only when resume correctness needs it. Continuity should not store a high-frequency progress log.

The semantic question is simply: **what materially changed toward the requested outcome?**
