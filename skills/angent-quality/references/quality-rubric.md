# Quality rubric

Quality is one owner with several evaluation phases. Use only the phases relevant to the task.

## Criteria grounding

Before judging, establish where the relevant criteria come from:

- current Contract and success state;
- active obligations/invariants;
- accepted baseline/protected properties for revision;
- authoritative domain requirements/evidence;
- reader capability or destination requirements where applicable.

Do not substitute an easy-to-measure proxy for the actual requested property.

## Phase A — solution integrity

Before expensive authoring or effects when consequence warrants it, PASS requires the relevant items:

1. task fit and current authority;
2. active obligations/invariants preserved;
3. important model relations/states present;
4. material conclusions supported at required precision;
5. evidence lineage/independence sufficient for the claim;
6. alternatives handled when they can change the decision;
7. causal claims justified;
8. unresolved uncertainty calibrated;
9. decision follows from constraints/consequences and is robust to remaining uncertainty;
10. dependency/replan structure coherent;
11. whole-scope claims have whole-scope evidence;
12. evaluator/measurement conditions are valid enough for the verdict.

Return failure to the earliest responsible owner. Use BLOCKED instead of inventing a producer defect when evaluator/environment attribution is unresolved.

## Phase B — candidate integrity

For reader-facing work evaluate:

1. reader-state fit;
2. concept admission;
3. explanatory progress and semantic economy;
4. representation fit;
5. paragraph/structure integrity;
6. terminology/language;
7. evidence/example interpretation;
8. epistemic fidelity between claim strength and support;
9. promised capability closure;
10. long-form consistency.

For a revision, do not judge the candidate only in isolation. Compare it with:

- the accepted baseline;
- the stated repair target;
- active obligations;
- protected properties and accepted quality floors;
- relevant artifact state;
- the baseline's still-valid measurement conditions.

A repair passes only when the target improves without silently losing accepted strengths.

## Phase C — endpoint/render integrity

After a destination write or external effect, verify the actual user/provider state:

- intended artifact/version exists;
- semantic structure survived formatting;
- rendered/visible result matches the accepted candidate;
- requested endpoint is satisfied.

Transport success is not endpoint proof.

## Verdict validity

A material PASS/FAIL is a claim that must itself be supported.

Check criteria validity, evidence validity, evaluator independence, environment/configuration, confounders and validity boundary. If these cannot support a justified PASS or FAIL, return BLOCKED.

For stochastic behavior, distinguish possibility, observed failure mode, repeatability and reliability. One trial does not establish all four.

## Findings

Return every material finding needed for the verdict. A finding identifies its phase, dimension, evidence, affected scope, earliest responsible owner and required repair property.

When several symptoms share one mechanism, group them so repair addresses the cause instead of one symptom at a time.

## Recurrence and oscillation

If the same failure returns after repair, or successive candidates alternate failures across the same dimensions, return a systemic recurrence/oscillation finding to Reasoning.

Do not keep requesting another local patch when the controlling model is failing.

## Comparative acceptance

For revision work distinguish:

- target repaired;
- protected properties preserved;
- invalidated dependencies reconciled;
- endpoint/render verified when required;
- verdict valid within the evidence/measurement boundary.

All required conditions must hold before the accepted baseline advances.
