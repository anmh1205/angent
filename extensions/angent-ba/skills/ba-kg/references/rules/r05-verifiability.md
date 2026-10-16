# R05: Requirements verifiability

## Operational contract

Every FR needs an actor or event trigger, a precondition where relevant, an observable state/result and an identified source. Each NFR needs metric, target, workload, environment and measurement method.

## Checks before accepting an artifact

Transform vague terms such as secure, fast, intuitive or reliable into explicit evidence requests; never invent a threshold to remove ambiguity. Different error causes require distinguishable observable results.

## Failure response

Derive at least one positive, negative and boundary check where the requirement demands them. Passing structural Markdown validation does not certify testability.

## Grounded example

'The API is fast' fails. 'The p95 response time is below the approved target for workload W, measured in environment E' is testable once target W/E are sourced.

**Evidence boundary:** these checks govern specialist BA deliverables but do not independently authorize provider changes or claim a test ran. ANGENT Root and Execution retain task scope; Quality must inspect the specific output.
