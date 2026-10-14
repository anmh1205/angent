---
name: angent-quality
description: Independently evaluate solution integrity, correction scope, comparative candidate quality, behavioral calibration and verified endpoint state, returning failures to the earliest responsible owner.
---

# ANGENT Quality — Independent Gate

Quality judges solution, candidate, behavior change, correction scope, or endpoint state against the Contract, active obligations, evidence, and the accepted baseline when revision work has one.

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
- correction interpreted at the right abstraction level;
- epistemic-status integrity;
- model completeness;
- evidence sufficiency and entailment/version boundaries;
- handling of material alternatives;
- causal/uncertainty calibration;
- decision integrity and decision-basis traceability;
- dependency/replan integrity, including revalidation of branch independence after shared-state changes;
- resume-compatibility integrity when saved work is resumed: dependent continuation/replay is supported by a compatible or completed-revalidation binding;
- effect-boundary integrity: current authority matches the resolved consequential target/material arguments;
- observation-admission integrity: model/decision changes are supported by the actual observed identity/scope/version/completeness;
- failure-domain integrity: tool/harness/transport/access failures are not laundered into negative domain facts, and authoritative negative observations are not weakened to generic UNKNOWN;
- mutation-freshness integrity: consequential existing-state writes are based on a compatible live target version/basis and preserve unrelated concurrent changes;
- canonical-target integrity: semantic-role targets resolve to the current authoritative object while explicit exact/historical targets remain bound to the identity actually requested;
- delegation-context integrity when specialists are used: bounded work context/effect authority is preserved, material trust/epistemic boundaries survive handoff, and specialist self-report is re-admitted rather than promoted automatically;
- scope-to-evidence coverage;
- authoritative endpoint evidence.

A fluent answer cannot compensate for a wrong model, and fixing the user's quoted example cannot compensate for leaving the same generating failure intact.

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

## Verdict consumption

Quality does not grant effect authority, but a Quality phase that the current Contract/revision/risk model has made **required** is a dependency of the transition it protects.

For that dependent transition:
- **PASS** satisfies the Quality dependency only within its verdict-validity boundary;
- **FAIL** rejects the current candidate/solution for that dependency and routes repair to the earliest faulty owner;
- **BLOCKED** leaves the dependency unsatisfied until evidence/evaluator/environment uncertainty is resolved or the requirement is legitimately changed.

Do not advance an accepted baseline, publish/write a candidate as accepted, or perform another consequential dependent effect merely by ignoring a required FAIL/BLOCKED.

Do not globally stop unrelated RUNNABLE work. The verdict blocks only transitions that rely on that gate.

A direct low-consequence task with no required Quality phase remains direct.

## Earliest faulty owner

When Layer A fails, return the earliest fault:
- task boundary/authority → Contract;
- state provenance/collaboration/context/recurrence retrieval → Context;
- correction interpretation/model/decision/plan → Reasoning;
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
- cross-surface prose continuity;
- paragraph cohesion;
- representation fit;
- prose/structure integrity;
- terminology/language;
- evidence/example interpretation;
- promised capability closure;
- long-form consistency when applicable;
- render fidelity through Format when destination-specific.

A document does not pass merely because it is more formal or more structured than the equivalent response. If moving to document form introduces stock teaching narration, detached sentences, generic AI prose, or weaker cohesion, return the failure to Authoring even when the facts remain correct.

For revision work, use the comparative-gates reference and reject a locally improved candidate if it regresses protected accepted properties.

## Review-context discipline

Quality should be able to reconstruct why a claim or candidate is valid from the Contract, evidence, baseline and visible decision basis.

Do not rely on the producer's persuasive narrative as proof. When anchoring/self-justification risk is material, review the candidate against obligations/evidence first and consult producer rationale only to resolve a genuine ambiguity.

Use stronger independence when consequence is high, a behavior change is broad, or the same failure has recurred.

Self-review is useful evidence but is not independent confirmation. Different graders can remain correlated when they share the same source/reference, rubric, model family, dataset, environment, or failure mode.

## Behavioral calibration

When a method/prompt/architecture change will affect many future tasks or units, Quality should calibrate the behavior before broad propagation when practical.

Use representative real failure/success cases and counter-cases rather than keyword/count checks. Compare candidate behavior with the accepted baseline and inspect actual trajectories/outcomes when the behavior is agentic.

For recurring corrections, include at least one analogous case not literally named by the latest complaint when practical. This checks whether the generating mechanism was repaired rather than the example memorized.

Calibration is evidence about a method; it is not whole-scope proof and should not become a mandatory platform for trivial changes.

When a material behavioral acceptance claim will be reused later, keep a reproducible evidence pointer/record linking the case, baseline, candidate, observable trajectory/artifacts, outcome, criteria and verdict validity boundary. Do not rely on “passed before” as an ungrounded memory.

## Effort

Scale verification to consequence and propagation risk.

Quality is strongly warranted for consequential external effects, revision of accepted work, broad/whole-scope claims, recurrent failures, high material uncertainty, and methods that will be propagated across many units.

A direct low-consequence answer should not acquire ceremony just because Quality exists.

For stochastic/open-ended behavior, match evidence strength to the claim: one success shows possibility more readily than reliability. Do not impose a universal trial count.

Do not add expensive checks that cannot change the verdict.
