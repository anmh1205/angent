# R06: Failure and recovery paths

## Operational contract

Trace the complete actor goal, including denial, invalid data, concurrency, upstream outage, retries, cancellation, lost connectivity, stale state, repeated actions and accessibility of recovery when pertinent.

## Checks before accepting an artifact

Do not treat all faults as one generic 'error' branch. Distinguish business denial from service unavailability and user cancellation; record expected state side effects and information disclosure.

## Failure response

Every terminal must identify what the user sees and what is persisted or rolled back. A diagram is incomplete when a nonterminal task has no next step or decision guards do not cover meaningful alternatives.

## Grounded example

A 403 vehicle access denial must not show cached telemetry; a 503 provider outage may have a last-known-state contract only if it is actually approved.

**Evidence boundary:** these checks govern specialist BA deliverables but do not independently authorize provider changes or claim a test ran. ANGENT Root and Execution retain task scope; Quality must inspect the specific output.
