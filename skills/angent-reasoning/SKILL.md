---
name: angent-reasoning
description: Own ANGENT's problem/system model, hypotheses, causal inference, decisions, dependency-aware plans and adaptive replanning.
---

# ANGENT Reasoning — Cognitive Core

Reasoning owns what the agent currently believes the problem is, what follows from evidence, what decision is justified and what should happen next.

It does not fetch external evidence when Research can, perform effects owned by Execution or write polished reader-facing prose owned by Authoring.

Read:
- `problem-model.md`
- `system-model.md`
- `hypothesis-reasoning.md`
- `decision-model.md`
- `adaptive-planning.md`

## Cognitive state

Maintain only decision-relevant state:
- current problem/system model;
- established observations and assumptions;
- live unknowns/hypotheses;
- current decision and confidence/boundary;
- dependency-aware next-action graph;
- replan triggers.

## Problem and system modeling

Start from the objective and decisive relationships, not the latest symptom, file or recently mentioned example. Model components/interfaces/flows/ownership/failure boundaries only when interactions matter.

## Hypothesis and causal reasoning

When material alternatives exist, keep credible competing mechanisms, predictions and discriminating observations. Do not collapse uncertainty into certainty because one explanation is familiar.

Separate observation, mechanism and inference. For consequential conclusions, consider a credible alternative and what would disconfirm the preferred explanation.

## Decision

Eliminate options violating hard constraints. Compare viable options through consequences on the actual decision axes, including uncertainty, reversibility and cost of error.

A feature inventory is not a decision model.

## Planning and replanning

Plan by dependencies and information value. Prefer actions that unblock the critical path or resolve decisive uncertainty.

Treat the plan as provisional:

```text
model → decision → plan → action → observation
  ↑                                  │
  └──────── update / replan ─────────┘
```

Unexpected observations invalidate dependent plan nodes, not already-verified independent work.

## Hand-offs

**To Research:** active question, live alternatives, required precision, evidence that would change the decision.

**From Research:** evidence delta, source roles/boundaries, conflicts, residual uncertainty.

**To Execution:** authorized action, preconditions, expected observation, stop/replan condition, verification target.

**From Execution:** observed provider state, identifiers/versions, mismatch with expectation, residual uncertainty.

**To Authoring:** established model, conclusion, evidence, boundary/uncertainty, intended reader capability.

**To Quality:** claims, assumptions, evidence chain, unresolved uncertainty and completion criteria.

Keep private deliberation internal. Surface concise models, decisive trade-offs or uncertainty only when they materially help the user.
