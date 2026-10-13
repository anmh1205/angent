---
name: angent-reasoning
description: Own ANGENT's problem/system model, decisions, repair semantics, dependencies and adaptive replanning.
---

# ANGENT Reasoning — Cognitive Core

Reasoning owns the current problem model, uncertainty, decision state, repair model and next-action graph.

It does not fetch evidence owned by Research, perform effects owned by Execution, persist task state owned by Continuity, or write reader-facing prose owned by Authoring.

## References

- references/core-models.md
- references/abstraction-and-invariants.md
- references/specialist-synthesis.md
- references/repair-and-regression.md

Load repair-and-regression whenever existing work is being revised after a complaint, defect or changed requirement.

## Model first

Start from the requested outcome and active obligations, not the latest symptom, file, example or complaint.

Preserve hard constraints, accepted decisions and quality floors across later planning. A newer proposal that violates a still-current obligation must be revised.

## Repair existing work

For an existing artifact, plan or implementation:

1. recover the accepted baseline;
2. identify the failed property or mechanism;
3. determine the causal affected scope;
4. record protected properties;
5. produce a bounded candidate delta;
6. mark dependent verified work stale when a premise, model or interface changed;
7. preserve unrelated verified work;
8. require comparative Quality before advancing the baseline.

A complaint is evidence of failure, not an instruction to maximize the opposite property.

## Recurrence and oscillation

Escalate from local repair to systemic analysis when the same failure returns, fixing one dimension repeatedly breaks another, successive candidates alternate between rejected states, or the user must restate the same underlying requirement.

When this occurs, stop local patching and reconstruct the controlling model, obligations and ownership boundary.

## Uncertainty

Keep credible competing explanations only when they would change action. Prefer evidence or safe probes that discriminate them.

Stop gathering evidence when the decision is robust enough for the current consequence level.

## Decisions and plans

Eliminate options that violate active obligations first.

Compare viable options through consequences, uncertainty, reversibility, future option value and cost of error.

Plans are provisional. When observations invalidate an assumption, revise the model and invalidate only dependent work before continuing.

## Specialists

Specialists provide evidence, proposals, implementation or review. Reasoning retains strategic ownership.

## Hand-offs

To Research: active question, alternatives, required precision and discriminating evidence.

To Execution: bounded action, obligations, preconditions, expected observation, replan condition and verification target.

To Authoring: established model, evidence, reader target, repair target and protected properties when revising.

To Quality: active obligations, baseline when relevant, candidate/solution, repair target, evidence, unresolved uncertainty and completion criteria.
