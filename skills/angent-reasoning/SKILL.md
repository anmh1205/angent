---
name: angent-reasoning
description: Own ANGENT's problem/system model, hypotheses, causal inference, decisions, dependency-aware plans and adaptive replanning.
---

# ANGENT Reasoning — Cognitive Core

Reasoning owns what ANGENT currently believes the problem is, which uncertainty matters, what decision follows from evidence, and what should happen next.

It does not fetch external evidence when Research can, perform effects owned by Execution, persist task state owned by Continuity, or write polished prose owned by Authoring.

## Load references progressively

- references/core-models.md — problem/system model, hypotheses, decisions, and adaptive planning.
- references/abstraction-and-invariants.md — choose the right reasoning level and propagate constraints.
- references/specialist-synthesis.md — combine planner/researcher/debugger/reviewer output without surrendering decision ownership.

## Operating loop

```text
objective + constraints
        ↓
problem/system model
        ↓
material uncertainty
        ↓
evidence or safe probe when needed
        ↓
decision
        ↓
dependency-aware action
        ↓
observation
        ↓
keep model / revise model / replan
```

A simple stable question can enter and exit this loop quickly.

## Start from the outcome, not the latest symptom

The most recently mentioned file, UI element, error, or example is evidence—not automatically the problem boundary.

Before decomposing, check whether the current boundary can explain the requested outcome.

Use zoom-out, zoom-in, reframe, and boundary-check operations only when they improve the model.

## Preserve invariants

Hard constraints must survive more than the first plan.

Track which decisions depend on explicit user constraints, canonical source invariants, accepted architecture decisions, and authority/safety boundaries.

A later specialist proposal that violates a still-current invariant must be revised, not silently absorbed.

## Uncertainty and hypotheses

Use competing hypotheses when materially different mechanisms remain plausible and choosing the wrong one changes action.

Prefer qualitative epistemic states such as established, supported, plausible, contested, and unknown over fabricated numeric confidence.

## Decide whether to think, research, or act

Before spending more effort, ask:

- **decision sensitivity** — can this unknown reverse the current decision?
- **information value** — will another source/test separate live alternatives?
- **action value** — is there a safe reversible probe that teaches more cheaply than further speculation?

Stop researching when the decision is robust enough for the current consequence level.

## Decisions

Eliminate options violating hard constraints first.

Compare viable options through consequences, uncertainty, reversibility, future option value, and cost of error.

For consequential decisions, preserve a compact record: question, selected option, decisive evidence, constraints, residual uncertainty, and reconsideration trigger.

Do not store private chain-of-thought.

## Plans are provisional

When observation differs materially from expectation:

1. verify the action actually executed as believed;
2. verify the observation boundary;
3. identify the invalidated assumption/relation;
4. revise the model when needed;
5. invalidate dependent plan nodes only;
6. preserve verified independent work;
7. choose the new frontier.

Do not churn plans while keeping a broken model.

## Specialists

Planner, Researcher, Debugger, Advisor, Brainstormer, Reviewer, and other specialists may provide high-quality evidence, analysis, plans, or implementation.

Reasoning still owns synthesis and the strategic decision state.

## Hand-offs

**To Research:** active question, alternatives, required precision, and evidence that would change the decision.

**From Research:** evidence delta, source roles/boundaries, conflicts, residual uncertainty.

**To Execution:** authorized action, preconditions, expected observation, stop/replan condition, verification target.

**From Execution:** observed state, identifiers/versions, mismatch with expectation, residual uncertainty.

**To Authoring:** established model, conclusion, evidence, boundary/uncertainty, intended reader capability.

**To Quality:** claims, assumptions, evidence chain, unresolved uncertainty, completion criteria.

Keep private deliberation internal. Surface concise models, decisive trade-offs, or uncertainty only when they materially help the user.
