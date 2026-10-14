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
- evidence pointers;
- wait state and next informative observation condition when the action remains pending.

## Whole-scope reads

When an action contributes to a whole-scope claim, preserve whether enumeration was actually complete.

Relevant evidence can include:
- pagination/cursor exhaustion;
- top-N or result limits;
- truncation indicators;
- scope filters;
- expected/observed counts when known.

A first page or partial result cannot establish full coverage.

## Wait state

A long-running operation may leave its branch in WAITING_EXTERNAL while unrelated work remains RUNNABLE.

Preserve the operation identity/handle, last observed state, dependent work and next informative observation condition when the wait may survive interruption.

When an action becomes WAITING_EXTERNAL, return control to Reasoning before any equivalent status observation is selected again.

Execution does not decide whether the whole task should keep waiting or switch branches; that requires the full active frontier.

Do not convert WAITING_EXTERNAL into repeated equivalent polling. Another check must be made eligible by new timing, event, dependency or explicit-status information.

## Retry and progress

Retry only when another attempt can plausibly change the result.

If repeated equivalent actions produce no new observation, return to Reasoning rather than churning tools.

A pending/running response with no state change is not substantive progress.

## Mechanical adaptation

Execution can change how a bounded action is realized without strategic re-approval when objective, active obligations and effect class stay the same.

## Replan boundary

Return to Reasoning when a precondition fails, the observation invalidates the model, expected state differs materially, an operation becomes RUNNING/PENDING, or a new obligation changes the action.

Do not continue a stale dependent plan merely because the next tool call is available.
