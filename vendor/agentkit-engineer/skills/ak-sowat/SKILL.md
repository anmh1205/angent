---
name: ak-sowat
description: Make a product-outcome priority call from recent implementation, verification, delivery, issue, and dependency evidence, with at most three evidence-backed next steps.
metadata: {port: angent-fallback, mode: portable}
---

# Sowat — Portable Fallback

Use after implementation or when the user wants a direct judgment about what matters next.

This Skill is product/outcome analysis, not implementation.

## Build the evidence view

Reconstruct:
- intended user/business outcome;
- what is actually implemented;
- what is verified;
- what is shipped/live versus only present in source;
- related regressions, dependencies, adoption blockers, and open issues;
- current priorities and delivery constraints.

Do not infer customer demand, revenue impact, shipment, or provider state without evidence.

## Make the priority call

1. Connect completed work to the intended outcome.
2. Challenge polish or busywork that does not materially advance the outcome.
3. Identify the highest-impact unresolved risks/opportunities.
4. Compare impact, effort, dependency, reversibility, and evidence quality.
5. Recommend no more than three next actions.
6. Give each action an observable success signal and state the evidence that would change the ranking.

Keep recommendations conditional when product evidence is weak.

## Boundary

Do not edit code, mutate issues, assign work, publish, deploy, or perform external effects from this Skill.

Use `ak-sumup` for a factual implementation recap and `ak-watzup` for live repository/work status.
