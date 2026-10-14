# Research stopping rule

Research should end when additional evidence has low decision/model value.

## Continue when

- a material hypothesis remains undistinguished;
- an exact current/versioned fact is required;
- a decisive premise is only assumed, conflicted, or stale;
- source conflict can reverse the recommendation;
- apparent corroboration is highly correlated and genuinely independent evidence could change the decision;
- evaluator/environment attribution remains unresolved and can change the next action;
- a missing relation/mechanism prevents a usable subject model;
- the next action has high cost/blast radius and critical assumptions are weak;
- scope coverage is insufficient for the claim being made.

## Stop when

- the current decision is robust to remaining uncertainty;
- decisive claims are supported at the required boundary/precision;
- the subject-model relations needed for the decision are adequately grounded;
- new sources repeat already-established non-decisive facts or the same evidence lineage;
- the unknown is outside requested scope;
- a cheap reversible action can teach more than further reading;
- the user asked for a bounded quick answer and existing evidence is sufficient.

## Negative-claim stopping

When the claim is absence/nonexistence/non-support, stop with the strongest bounded proposition the retrieval evidence actually supports.

Continue or change retrieval strategy when:
- a search miss is the only support for a consequential global absence claim;
- index freshness, non-default scope, access exclusions, top-k/truncation, or query formulation can plausibly hide a result;
- an exact authoritative lookup or complete-enough enumeration is cheaply available and would materially strengthen the claim.

Stop rather than search indefinitely when:
- the decision is robust even if the missing item exists outside the searched boundary;
- available sources cannot provide stronger coverage and the residual uncertainty is stated;
- an authoritative negative lookup or sufficient enumeration already closes the relevant scope.

Do not require arbitrary numbers of failed searches.

## Detect research stall

More searches are not progress when they only produce repetitions, low-authority variants of the same claim, or evidence that cannot discriminate live alternatives.

If repeated retrieval does not change epistemic state, subject-model structure, coverage, or the decision, return the residual uncertainty to Reasoning or change the research strategy.

## Do not chase certainty

Residual uncertainty is acceptable when it is explicit and does not change the justified action.

Do not search toward an arbitrary source-count, independence-count, or trial-count target.

The goal is robust understanding/decision quality, not evidence volume.
