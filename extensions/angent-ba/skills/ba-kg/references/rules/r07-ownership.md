# R07: Data and decision ownership

## Operational contract

Separate policy owner, business approver, engineering implementer, data controller, integration source of truth and workflow actor. These responsibilities can belong to different groups.

## Checks before accepting an artifact

Every mapped API field needs an explicit owning side and transformation rules. When two systems can change the same value, define conflict resolution and a freshness/reconciliation guarantee.

## Failure response

Never grant an agent or external kit more write authority because a specialist method recommends it; ANGENT Execution follows the actual user-permitted target and provider rights.

## Grounded example

The payment processor may own settlement status while the rental platform owns reservation eligibility. A 'sync all' instruction without field ownership risks false updates.

**Evidence boundary:** these checks govern specialist BA deliverables but do not independently authorize provider changes or claim a test ran. ANGENT Root and Execution retain task scope; Quality must inspect the specific output.
