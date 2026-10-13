# Action semantics

Reasoning should hand Execution a bounded action, not an open-ended strategic mission.

## ActionNode

Useful fields:
- intent;
- target;
- preconditions;
- authority;
- relevant constraints;
- capability required;
- input/artifact pointers;
- expected observation;
- action-level success predicate;
- replan condition;
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

## Mechanical adaptation

Execution can change how a bounded action is realized without strategic re-approval when objective, constraints and effect class stay the same.

## Replan boundary

Return to Reasoning when the observation invalidates the assumptions that justified dependent work.

Do not continue a stale plan merely because the next tool call is available.
