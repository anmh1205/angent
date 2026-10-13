---
name: ak-autoresearch
description: Run bounded goal-directed research/iteration by routing each cycle to the Skill that owns the measurable outcome.
metadata: {port: angent-fallback, mode: adapted}
---

# Autoresearch — Portable Fallback

Use when the work has a measurable objective and benefits from repeated evidence-driven iteration.

## Contract

Require:
- objective;
- metric/acceptance condition;
- allowed search/action space;
- maximum cost/time/iterations when relevant;
- stop conditions;
- artifact/source to preserve.

## Loop

1. Measure current state.
2. Form one changeable hypothesis.
3. Route the next step to the owning Skill.
4. Execute the smallest experiment.
5. Measure again.
6. Keep, revert or revise based on evidence.
7. Record the iteration in Continuity.
8. Stop when the target is met, progress saturates, the budget ends, or a new decision is required.

Do not run unbounded loops or optimize a proxy metric that no longer represents the user's objective.
