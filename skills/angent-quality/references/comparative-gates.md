# Comparative quality gates

Quality is one owner with several evaluation phases. The phases exist to prevent invalid solutions, behavioral regression, communication regression and false endpoint claims without turning Quality into a second author.

## 1. Solution gate

Before expensive authoring or effects, evaluate the established solution model when consequence warrants it:

- task and authority fit;
- active constraints and invariants;
- epistemic status and evidence/entailment sufficiency;
- unresolved alternatives that could reverse the decision;
- decision basis when traceability matters;
- plan/dependency integrity.

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

Target/capability evidence and preservation/regression evidence answer different questions.

A successful new behavior can show the repair is possible while providing weak evidence that it is reliable. Likewise, a preservation check only supports properties it actually exercises.

For stochastic/open-ended behavior, use representative repeated evidence when the claim and consequence warrant it. Do not impose a fixed trial quota.

## 3. Behavioral calibration gate

For a change with propagation risk—such as a shared method, root prompt, routing rule, owner interface or bulk transformation strategy—compare candidate behavior with the accepted baseline on a small representative set before scaling when practical.

Include:
- real failure cases the change intends to repair;
- accepted-success cases that must stay good;
- counter-cases where the new behavior should not trigger;
- difficult/boundary cases when they can change the decision.

Inspect trajectories/outcomes when a pass/fail score could hide the wrong mechanism. Use ablation or narrower comparison when one prompt/rule change may be responsible.

Do not mistake this calibration for proof that uninspected scope is clean.

## 4. Endpoint/render gate

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
- regression risk when relevant.

Findings that share one causal mechanism should be grouped so repair targets the cause rather than a sequence of symptoms.

## Comparative verdict

For revisions, distinguish:

- **TARGET_FIXED** — the requested defect improved;
- **PRESERVATION_PASS** — protected properties remain valid;
- **DEPENDENCIES_RECONCILED** — invalidated dependent work was handled;
- **ENDPOINT_VERIFIED** — final user/provider state matches the accepted candidate.

A candidate does not pass merely because TARGET_FIXED is true.

## Baseline validity

Before using an accepted baseline or old test result as regression evidence, verify that the relevant validity conditions still match.

Material conditions can include model/provider/version, harness/tool behavior, environment/resources/configuration, rubric/criterion, source/artifact version, and task/input distribution.

A changed condition makes only dependent conclusions stale/recheck. It does not automatically invalidate the baseline artifact or unrelated accepted properties.

## Independence and anchoring

Quality must preserve evaluative independence from production reasoning.

Independence can be achieved through context separation, a reviewer/specialist, a separate model when available, or a deliberate blind comparison against the Contract/baseline.

When anchoring risk is material, evaluate the candidate and evidence before reading the producer's persuasive rationale. The compact decision basis may be consulted for traceability; it is not itself evidence that the decision is correct.

Different reviewers, graders, or repeated checks are not automatically independent if they share the same reference, source lineage, rubric, model family, dataset, environment, or failure mode.

Use stronger independence when consequence is high or the same failure has recurred.

## Oscillation signal

If successive candidates alternate failures across the same dimensions or the same defect reappears, return an oscillation/recurrence finding to Reasoning. Do not keep sending isolated wording fixes back to Authoring.
