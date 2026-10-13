# Action semantics

Reasoning should hand Execution a bounded action, not an open-ended strategic mission.

## ActionNode

Useful fields:
- intent;
- target;
- authority;
- active obligations relevant to the action;
- preconditions/dependencies;
- capability required;
- input/artifact pointers;
- expected observation;
- action-level success predicate;
- replan condition;
- verification target;
- effect class.

Do not serialize every trivial action into a formal object; preserve these semantics.

## ObservationDelta

Return:
- action attempted;
- actual provider/local state;
- changed identifiers/versions;
- artifacts/checks;
- whether expectation matched;
- uncertainty;
- evidence pointers.

## Whole-scope reads

When an action contributes to a whole-scope claim, preserve whether enumeration was actually complete.

Relevant evidence can include:
- pagination/cursor exhaustion;
- top-N or result limits;
- truncation indicators;
- scope filters;
- expected/observed counts when known.

A first page or partial result cannot establish full coverage.

## Retry and progress

Retry only when another attempt can plausibly change the result.

If repeated equivalent actions produce no new observation, return to Reasoning rather than churning tools.

## Mechanical adaptation

Execution can change how a bounded action is realized without strategic re-approval when objective, active obligations and effect class stay the same.

## Replan boundary

Return to Reasoning when a precondition fails, the observation invalidates the model, expected state differs materially, or a new obligation changes the action.

Do not continue a stale dependent plan merely because the next tool call is available.
