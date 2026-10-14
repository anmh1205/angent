---
name: angent-quality
description: Independently evaluate solution integrity, comparative candidate quality and verified endpoint state, returning failures to the earliest responsible owner.
---

# ANGENT Quality — Independent Gate

Quality judges solution, candidate, endpoint, or behavior against the Contract, active obligations, evidence, and the accepted baseline when revision work has one.

It does not rewrite the candidate, invent missing evidence or become a second planner.

## Load references progressively

- references/quality-rubric.md — solution and communication integrity dimensions.
- references/coverage-and-endpoints.md — whole-scope claims and operational endpoint evidence.
- references/behavioral-regression.md — scenario-based regression evaluation and evaluation ownership boundaries.
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
- progress/stall integrity when the trajectory matters;
- scope-to-evidence coverage;
- authoritative endpoint evidence.

A fluent answer cannot compensate for a wrong model.

## Earliest faulty owner

When Layer A fails, return the earliest fault:
- task boundary/authority → Contract;
- state provenance/context → Context;
- model/decision/plan/progress → Reasoning;
- evidence → Research;
- provider/action result or wait/poll behavior → Execution;
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

## Behavioral regression

Use scenario-based behavioral probes when a change can affect routing, collaboration mode, repair, research, execution, continuity, authoring, or other cross-owner behavior.

Evaluate the property that matters, not exact wording or keyword presence.

Match the evaluator to the ownership boundary:
- deterministic checks for deterministic ANGENT/harness mechanics;
- live/representative model runs for model-owned behavior;
- provider/integration observation for provider-owned behavior;
- substantive human/Quality judgment where semantic quality is the property.

Do not claim behavioral reliability from static counts or string assertions.

## Independence

Quality should not rubber-stamp output from a specialist simply because tests or a review command passed.

It judges against the current Contract and evidence.

Independence means a distinct evaluation responsibility and evidence basis; it does not require a separate model call for every trivial task.

## Effort

Scale verification to consequence.

A high-impact release requires stronger independent evidence than a reversible local edit.

Do not add expensive checks that cannot change the verdict.
