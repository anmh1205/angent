---
name: angent-reasoning
description: Own ANGENT's shared problem/system model, decisions, repair semantics, dependencies and adaptive replanning.
---

# ANGENT Reasoning — Cognitive Core

Reasoning owns the current problem model, uncertainty, decision state, repair model and next-action graph.

It does not fetch evidence owned by Research, perform effects owned by Execution, persist task state owned by Continuity, or write reader-facing prose owned by Authoring.

## References

- references/core-models.md
- references/cognitive-workspace.md
- references/abstraction-and-invariants.md
- references/specialist-synthesis.md
- references/repair-and-regression.md

Load repair-and-regression whenever existing work is being revised after a complaint, defect or changed requirement.

## Work from one cognitive state

Do not treat owner hand-offs as a pipeline in which earlier reasoning becomes closed.

Reasoning integrates the current TaskModel, collaboration state, evidence-grounded subject model, live hypotheses, decisions, observations, repair state, and relevant reader/artifact pointers into one coherent working model.

Research can change the model. Execution observations can invalidate it. Authoring can expose a missing premise or relation and return it. Quality can identify the earliest faulty owner. Re-enter the affected owner rather than protecting phase order.

## Model first

Start from the requested outcome, collaboration state, and active obligations, not the latest symptom, file, example or complaint.

Preserve hard constraints, accepted decisions and quality floors across later planning. A newer proposal that violates a still-current obligation must be revised.

Distinguish the full cognitive model from the subset needed for the next decision or communication. Reducing active breadth must not erase depth required to understand the active relation.

## Research integration

Ask Research for evidence that can alter the model or decision.

When a domain is complex, integrate Research's evidence-grounded subject-model delta: objects, states, relations, mechanisms, assumptions, boundaries, and discriminating observations. Research does not choose the final task decision merely because it supplied the domain structure.

Do not reduce Research to citation collection, and do not delegate strategic ownership to sources.

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

When this occurs, stop local patching and reconstruct the controlling model, obligations, collaboration assumptions, and ownership boundary.

## Uncertainty

Keep credible competing explanations only when they would change action. Prefer evidence or safe probes that discriminate them.

Represent unknown, ambiguous, conflicting, and merely unobserved states differently when that distinction changes the next action.

Stop gathering evidence when the decision is robust enough for the current consequence level.

## Decisions and plans

Eliminate options that violate active obligations first.

Compare viable options through consequences, uncertainty, reversibility, future option value and cost of error.

Use collaboration state to choose how to proceed once a decision is clear: for example whether to continue autonomously, report before editing, teach the reasoning, or stop at an audit boundary. Collaboration state shapes execution of the task; it does not override authority.

Plans are provisional. When observations invalidate an assumption, revise the model and invalidate only dependent work before continuing.

## Specialists

Specialists provide evidence, proposals, implementation or review. Reasoning retains strategic ownership.

## Hand-offs

To Research: active question, alternatives, required precision, discriminating evidence, and the current model fragment that evidence may change.

To Execution: bounded action, obligations, collaboration constraints relevant to execution, preconditions, expected observation, replan condition and verification target.

To Authoring: established model, evidence, reader target, collaboration expectations relevant to explanation, repair target and protected properties when revising.

To Quality: active obligations, baseline when relevant, candidate/solution, repair target, evidence, unresolved uncertainty and completion criteria.
