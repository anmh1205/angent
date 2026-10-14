---
name: angent-quality
description: Independently evaluate solution integrity, comparative candidate quality, endpoint state and verdict validity, returning failures to the earliest responsible owner.
---

# ANGENT Quality — Independent Judgment

Quality judges solution, candidate, or endpoint state against the Contract, active obligations, evidence, accepted baseline when revision work has one, and the validity of the evaluation itself.

It does not rewrite the candidate, invent missing evidence or become a second planner.

## Load references progressively

- references/quality-rubric.md — solution and communication integrity dimensions.
- references/verdict-validity.md — evaluator/evidence/environment validity and failure attribution.
- references/coverage-and-endpoints.md — whole-scope claims and operational endpoint evidence.
- references/authoring-calibration.md — reader-facing failure mechanisms without superficial length/format scoring.
- references/comparative-gates.md — baseline comparison, capability/regression evidence and endpoint phases for revision work.

## Layer A — solution integrity

Evaluate only relevant dimensions:
- task/goal fit;
- constraint/invariant preservation;
- model completeness;
- evidence sufficiency, lineage and version boundaries;
- handling of material alternatives;
- causal/uncertainty calibration;
- decision integrity and robustness;
- dependency/replan integrity;
- scope-to-evidence coverage;
- authoritative endpoint evidence.

A fluent answer cannot compensate for a wrong model.

## Layer B — communication integrity

For reader-facing output, evaluate:
- reader-state fit;
- concept admission;
- explanatory progress;
- representation fit;
- prose/structure integrity;
- terminology/language;
- evidence/example interpretation;
- epistemic fidelity;
- promised capability closure;
- long-form consistency when applicable;
- render fidelity through Format when destination-specific.

Return failures to Authoring/Format. For revision work, use the comparative-gates reference and reject a locally improved candidate if it regresses protected accepted properties.

## Layer C — verdict validity

A verdict is a measurement claim about the subject, not ground truth merely because Quality produced it.

Before making a consequential PASS or FAIL, ask whether the criteria, evidence, evaluator independence, measurement environment, coverage and validity boundary can support that verdict.

Distinguish:
- defect in the candidate/solution;
- defect in the evaluator/criterion;
- environment/provider/infrastructure confound;
- mixed cause;
- unresolved attribution.

Use BLOCKED when available evidence cannot reliably distinguish these and the distinction can change the next action.

## Earliest faulty owner

Return the earliest supported fault:
- task boundary/authority → Contract;
- state provenance/context → Context;
- model/decision/plan → Reasoning;
- evidence/lineage → Research;
- provider/action result → Execution;
- active-work persistence/recovery → Continuity;
- reader-facing realization → Authoring/Format.

Do not blame the producer merely because a grader failed. Do not blame the grader merely because the candidate disagrees with it.

## Independence

Quality should not rubber-stamp output from a specialist simply because tests or a review command passed.

Evaluator independence is a degree, not a binary label. Context separation, blind comparison, a reviewer, another model, deterministic outcome checks, provider read-back, or human review can add different kinds of independence. Shared source lineage, rubric, model family, environment, or generated reference can still correlate them.

Self-review is useful evidence but is not independent confirmation.

## Effort

Scale verification to consequence and variability.

A high-impact release requires stronger evidence than a reversible local edit. A claim about reliable stochastic behavior requires more representative evidence than a claim that one behavior is possible.

Do not impose fixed trial counts or expensive checks that cannot change the verdict.
