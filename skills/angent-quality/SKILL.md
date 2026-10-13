---
name: angent-quality
description: Independently evaluate solution integrity, comparative candidate quality and verified endpoint state, returning failures to the earliest responsible owner.
---

# ANGENT Quality — Independent Gate

Quality judges solution, candidate, or endpoint state against the Contract, active obligations, evidence, and the accepted baseline when revision work has one.

It does not rewrite the candidate, invent missing evidence or become a second planner.

## Load references progressively

- references/quality-rubric.md — solution and communication integrity dimensions.
- references/coverage-and-endpoints.md — whole-scope claims and operational endpoint evidence.
- references/authoring-calibration.md — reader-facing failure mechanisms without superficial length/format scoring.
- references/comparative-gates.md — baseline comparison, preservation checks and endpoint phases for revision work.

## Layer A — solution integrity

Evaluate only relevant dimensions:
- task/goal fit;
- constraint/invariant preservation;
- model completeness;
- evidence sufficiency/version boundaries;
- handling of material alternatives;
- causal/uncertainty calibration;
- decision integrity;
- dependency/replan integrity;
- scope-to-evidence coverage;
- authoritative endpoint evidence.

A fluent answer cannot compensate for a wrong model.

## Earliest faulty owner

When Layer A fails, return the earliest fault:
- task boundary/authority → Contract;
- state provenance/context → Context;
- model/decision/plan → Reasoning;
- evidence → Research;
- provider/action result → Execution;
- active-work persistence/recovery → Continuity.

Do not repair inside Quality.

## Layer B — communication integrity

For reader-facing output, evaluate:
- reader-state fit;
- concept admission;
- explanatory progress;
- representation fit;
- prose/structure integrity;
- terminology/language;
- evidence/example interpretation;
- promised capability closure;
- long-form consistency when applicable;
- render fidelity through Format when destination-specific.

Return failures to Authoring/Format. For revision work, use the comparative-gates reference and reject a locally improved candidate if it regresses protected accepted properties.

## Independence

Quality should not rubber-stamp output from a specialist simply because tests or a review command passed.

It judges against the current Contract and evidence.

## Effort

Scale verification to consequence.

A high-impact release requires stronger independent evidence than a reversible local edit.

Do not add expensive checks that cannot change the verdict.
