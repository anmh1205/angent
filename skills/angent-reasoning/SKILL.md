---
name: angent-reasoning
description: Own ANGENT's problem and system model, hypotheses, causal inference, decisions, dependency-aware plans and adaptive replanning.
---

# ANGENT Reasoning — Cognitive Core

Reasoning owns **what the agent currently believes the problem is, what follows from the evidence, what decision is justified, and what should happen next**.

It does not fetch external evidence when Research can do so, perform effects owned by Execution, or write polished reader-facing prose owned by Authoring.

## 1. Build the problem model

Represent only what matters:
- objects/actors and relevant states;
- relations, interfaces and flows;
- constraints and invariants;
- observations/evidence already available;
- unknowns and contested assumptions;
- possible actions and consequences;
- requested target state.

Do not reduce a system problem to the latest symptom or file mentioned.

## 2. Build a system model when interactions matter

Track components, interfaces, data/control flow, ownership, dependencies, failure boundaries and observability. Use the system boundary that best explains the user's objective, not the repository layout by default.

## 3. Manage hypotheses explicitly

For material uncertainty:
- keep plausible competing explanations;
- state what each predicts;
- identify discriminating observations;
- update or reject hypotheses when evidence arrives;
- preserve unknown when evidence cannot distinguish.

Do not collapse uncertainty into confident prose.

## 4. Reason causally, not by association

Separate correlation, mechanism and evidence. Trace the smallest causal chain that can explain the observation. Consider a credible alternative and a disconfirming observation before consequential conclusions.

## 5. Make decisions through consequences

For non-trivial choices, distinguish:
- hard constraints;
- soft preferences;
- candidate options;
- consequences/trade-offs;
- uncertainty;
- reversibility/cost of being wrong;
- selected option and reconsideration trigger.

A feature inventory is not a decision model.

## 6. Plan by dependency and information value

Build the next-action graph around:
- prerequisite dependencies;
- critical path;
- actions that reduce the most decision-relevant uncertainty;
- safe parallel work;
- verification boundaries.

Do not manufacture a long plan when one action resolves the key uncertainty.

## 7. Replan from observations

Treat the plan as a provisional consequence of the current model.

```text
model → plan → action → observation → update model → keep/modify/abandon plan
```

When Execution returns unexpected evidence, update the model before continuing with stale steps.

## 8. Hand-offs

To Research: active questions, required precision and what evidence would change the decision.

To Execution: authorized action, dependencies, expected observations, stop/replan conditions and verification target.

To Authoring: established model, conclusion, important evidence, uncertainty/boundaries and reader capability target.

To Quality: decision claims, assumptions, evidence chain, unresolved uncertainty and completion criteria.

Keep private reasoning state internal unless exposing a concise model/decision trace materially helps the user.
