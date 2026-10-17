# R01: Evidence precedence

## Operational contract

Identify whether the statement concerns an approved future requirement, source-observed implementation, real deployed runtime, live provider record, or historical decision. These are different questions and cannot be answered from the same document indiscriminately.

## Checks before accepting an artifact

Pin the source identifier, document/commit revision, observation time and intended scope. Compare any conflict using direct witnesses. Current Jira delivery status does not override an accepted customer rule; an old SRS does not override a current runtime probe for a question about what is deployed.

## Failure response

If evidence disagrees, show both, name the consequence and seek the missing authoritative decision. Do not reorder sources by date alone.

## Grounded example

A merged PR showing a new permission check cannot prove the staging instance is deployed. State implemented-at-commit separately from observed-in-staging.

**Evidence boundary:** these checks govern specialist BA deliverables but do not independently authorize provider changes or claim a test ran. ANGENT Root and Execution retain task scope; Quality must inspect the specific output.
