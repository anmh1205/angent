# Comparative quality gates

Quality is one owner with several evaluation phases. The phases exist to prevent invalid solutions, communication regression and false endpoint claims without turning Quality into a second author.

## 1. Solution gate

Before expensive authoring or effects, evaluate the established solution model when consequence warrants it:

- task and authority fit;
- active constraints and invariants;
- model/evidence sufficiency;
- unresolved alternatives that could reverse the decision;
- plan/dependency integrity;
- verdict validity when the decision depends on an evaluator or measurement.

A failed solution gate returns to the earliest responsible owner.

## 2. Candidate gate

For a reader-facing artifact or revision, compare the candidate against:

- the current Contract;
- active obligations;
- the accepted baseline when one exists;
- the repair target;
- protected properties that the candidate could affect.

Do not ask only whether the candidate is good in isolation.

A valid repair must improve the target without silently dropping accepted strengths or active constraints.

## Capability evidence versus regression evidence

A change often requires two different questions:

- **capability/target evidence** — did the changed system actually gain or repair the intended property?
- **regression/preservation evidence** — did properties that were already accepted remain valid?

Evidence for one does not automatically establish the other.

For stochastic/open-ended behavior, one successful example can show the new behavior is possible while providing weak evidence that it is reliable. Likewise, a regression sample must actually cover the protected behavior it claims to preserve.

Do not impose a fixed trial count. Match evidence strength to variability, consequence and the claim being made.

## 3. Endpoint/render gate

After an external write or destination render, verify the state the user actually receives:

- intended artifact/version is present;
- semantic structure survived formatting;
- rendered content matches the accepted candidate;
- provider state satisfies the requested endpoint.

Transport success alone is insufficient.

## Findings set

Quality may return multiple related findings.

Each material finding should identify:

- phase;
- dimension;
- severity or consequence;
- evidence;
- affected scope;
- earliest responsible owner;
- required repair property;
- regression risk when relevant;
- evaluator/environment confounder when material.

Findings that share one causal mechanism should be grouped so repair targets the cause rather than a sequence of symptoms.

## Comparative verdict

For revisions, distinguish:

- **TARGET_FIXED** — the requested defect improved;
- **PRESERVATION_PASS** — protected properties remain valid under applicable baseline conditions;
- **DEPENDENCIES_RECONCILED** — invalidated dependent work was handled;
- **ENDPOINT_VERIFIED** — final user/provider state matches the accepted candidate.

A candidate does not pass merely because TARGET_FIXED is true.

## Baseline validity

Before using the accepted baseline as regression evidence, verify that its relevant validity conditions still match.

A changed model, provider, harness, environment, resource budget, rubric, source version or task distribution can make some baseline conclusions stale without making the baseline artifact itself wrong.

Invalidate only the conclusions that depended on the changed condition.

## Independence

Quality must preserve evaluative independence from production reasoning.

Independence can be strengthened through context separation, blind comparison, independent reviewers/models, deterministic outcome checks, provider read-back or human review. None is automatically independent if it shares the same source lineage, rubric, reference or environment failure mode.

Self-review is useful but is not independent confirmation.

## Oscillation signal

If successive candidates alternate failures across the same dimensions or the same defect reappears, return an oscillation/recurrence finding to Reasoning. Do not keep sending isolated wording fixes back to Authoring.
