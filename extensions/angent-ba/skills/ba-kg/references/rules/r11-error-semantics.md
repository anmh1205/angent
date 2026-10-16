# R11: Error semantics across user and integration boundaries

## Operational contract

Every error contract must identify triggering state, actor visibility, machine-facing identifier, mutation outcome, permitted retry, and telemetry/audit effects. API status alone rarely conveys the whole outcome.

## Checks before accepting an artifact

Review negative cases separately for unauthorized access, validation failure, business-policy conflict, duplicate request, rate limit and downstream unavailability. Require distinct user actions when remediation differs.

## Failure response

Do not expose whether an account or asset exists if the accepted disclosure policy forbids it. Require idempotency tests for mutating retry operations rather than assuming that a 5xx is safe to retry.

## Grounded example

A failed ECU-status fetch should not be converted into an 'invalid login' message. A duplicated diagnostic ACK requires verification that the operation has not created two records.

**Evidence boundary:** specialist advice does not establish completed provider writes or approve business requirements. The actual source and observed result remain decisive; ANGENT Root and Quality retain oversight.
