# R03: Stable artifact identities

## Operational contract

Retain existing accepted UN/BO/CAP/FR/BR/AC/CHK/TC IDs when editing or moving rows. IDs are a durable referent for conversation, Jira, tests and change impact; a document section number is not an identity.

## Checks before accepting an artifact

Reject duplicate IDs within and across the relevant artifact type and feature boundary. Resolve renaming and supersession explicitly; do not silently reuse retired IDs for a different requirement.

## Failure response

Require references to name real source artifacts. Graph traversal may find an ID but still cannot establish the semantic meaning of its edge.

## Grounded example

Moving FR-007 to the beginning of a document must not rename it FR-001; a retired FR keeps its history and gets a superseded-by reference.

**Evidence boundary:** these checks govern specialist BA deliverables but do not independently authorize provider changes or claim a test ran. ANGENT Root and Execution retain task scope; Quality must inspect the specific output.
