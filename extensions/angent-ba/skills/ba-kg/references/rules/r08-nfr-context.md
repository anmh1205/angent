# R08: NFR workload and measurement context

## Operational contract

Attach a boundary to each performance, availability, reliability, security, maintainability or usability target. State population, workload, units, percentile/window, measurement environment and data collection method.

## Checks before accepting an artifact

Record who accepts the threshold and which feature/critical path it applies to. A benchmark on a developer laptop is not a production NFR verdict.

## Failure response

Separate test plan from executed results and conditional vendor constraints. Do not round a single favorable sample into an availability claim.

## Grounded example

'99.9% uptime' without observation period and excluded maintenance is incomplete. 'P95 under 2 seconds at 5,000 open claims on staging dataset' states a meaningful benchmark condition.

**Evidence boundary:** these checks govern specialist BA deliverables but do not independently authorize provider changes or claim a test ran. ANGENT Root and Execution retain task scope; Quality must inspect the specific output.
