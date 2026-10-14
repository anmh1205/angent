---
name: angent-quality
description: Independently evaluate solution integrity, comparative candidate quality, behavioral calibration and verified endpoint state, returning failures to the earliest responsible owner.
---

# ANGENT Quality — Independent Gate

Quality judges solution, candidate, behavior change, or endpoint state against the Contract, active obligations, evidence, and the accepted baseline when revision work has one.

It does not rewrite the candidate, invent missing evidence or become a second planner.

## Load references progressively

- references/quality-rubric.md — solution and communication integrity dimensions.
- references/verdict-validity.md — criteria/evidence/evaluator/measurement validity and failure attribution.
- references/coverage-and-endpoints.md — whole-scope claims and operational endpoint evidence.
- references/authoring-calibration.md — reader-facing failure mechanisms without superficial length/format scoring.
- references/comparative-gates.md — baseline comparison, preservation checks and endpoint phases for revision work.
- references/behavioral-calibration.md — representative calibration for broad method/prompt/architecture changes.

## Layer A — solution integrity

Evaluate only relevant dimensions:
- task/goal fit;
- constraint/invariant preservation;
- epistemic-status integrity;
- model completeness;
- evidence sufficiency and entailment/version boundaries;
- handling of material alternatives;
- causal/uncertainty calibration;
- decision integrity and decision-basis traceability;
- dependency/replan integrity;
- scope-to-evidence coverage;
- authoritative endpoint evidence.

A fluent answer cannot compensate for a wrong model.

## Verdict validity

A Quality verdict is itself a measurement claim about the subject.

Before a consequential PASS or FAIL, ask whether the criteria, evidence, evaluator independence, coverage and measurement conditions can support that verdict.

Distinguish:
- defect in the candidate/solution;
- defect in the evaluator/criterion;
- environment/provider/infrastructure confound;
- mixed cause;
- unresolved attribution.

Use BLOCKED when available evidence cannot reliably distinguish these and the distinction can change the next action.

## Earliest faulty owner

When Layer A fails, return the earliest fault:
- task boundary/authority → Contract;
- state provenance/collaboration/context → Context;
- model/decision/plan → Reasoning;
- evidence/support boundary → Research;
- provider/action result → Execution;
- active-work persistence/recovery → Continuity.

Do not repair inside Quality.

Do not blame the producer merely because a grader failed, and do not blame the grader merely because the candidate disagrees with it.

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

## Review-context discipline

Quality should be able to reconstruct why a claim or candidate is valid from the Contract, evidence, baseline and visible decision basis.

Do not rely on the producer's persuasive narrative as proof. When anchoring/self-justification risk is material, review the candidate against obligations/evidence first and consult producer rationale only to resolve a genuine ambiguity.

Use stronger independence when consequence is high, a behavior change is broad, or the same failure has recurred.

Self-review is useful evidence but is not independent confirmation. Different graders can remain correlated when they share the same source/reference, rubric, model family, dataset, environment, or failure mode.

## Behavioral calibration

When a method/prompt/architecture change will affect many future tasks or units, Quality should calibrate the behavior before broad propagation when practical.

Use representative real failure/success cases and counter-cases rather than keyword/count checks. Compare candidate behavior with the accepted baseline and inspect actual trajectories/outcomes when the behavior is agentic.

Calibration is evidence about a method; it is not whole-scope proof and should not become a mandatory platform for trivial changes.

## Effort

Scale verification to consequence and propagation risk.

Quality is strongly warranted for consequential external effects, revision of accepted work, broad/whole-scope claims, recurrent failures, high material uncertainty, and methods that will be propagated across many units.

A direct low-consequence answer should not acquire ceremony just because Quality exists.

For stochastic/open-ended behavior, match evidence strength to the claim: one success shows possibility more readily than reliability. Do not impose a universal trial count.

Do not add expensive checks that cannot change the verdict.
