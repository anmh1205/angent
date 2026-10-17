# R10: Privacy, security and non-disclosure

## Operational contract

Identify data classification and tenant/actor access before copying source documents to external tools, logging user input or exporting stakeholder packages. Treat code, contracts, customer data and account identifiers as potentially sensitive.

## Checks before accepting an artifact

Default to local diagram and test rendering when feasible. Sending schema or process source to hosted PlantUML/dbdiagram services or SaaS tools is an external disclosure requiring authorization.

## Failure response

Use placeholders and synthetic fixtures for examples. Never record real access tokens in Bruno `.bru`, password test data, changelogs or artifact metadata.

## Grounded example

A diagram generator passing unit tests with a fleet vehicle ID does not authorize publishing actual vehicle locations. Check delivery scope and redact identifiers.

**Evidence boundary:** these checks govern specialist BA deliverables but do not independently authorize provider changes or claim a test ran. ANGENT Root and Execution retain task scope; Quality must inspect the specific output.
