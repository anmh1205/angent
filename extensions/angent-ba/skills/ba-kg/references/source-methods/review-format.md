# Evidence-first review findings and reconciliation

**Provenance:** Adapted from MIT Dev BA Kit / rules/review-format.md (Edward Ngo, 2026), https://github.com/nv-minh/dev-ba-kit. Reviewers are perspectives, not necessarily separate host agents.

## One finding, one falsifiable problem

A useful review finding records: affected artifact ID and section, observed issue, source witness, impact on business behavior, recommended change or missing evidence and severity rationale. Mark a source-backed contradiction differently from a style preference.

Use **blocking** when acceptance would be unsafe or materially incorrect without resolution: inconsistent authorization, wrong financial rule, leaking personal data, missing required behavior or an untestable consequential outcome. Use **warning** for material uncertainty that has a documented mitigation/waiver path. Use **suggestion** for improvements that need not block the user's current goal.

No fixed consensus rule promotes two weak warnings into a blocker. Severity follows consequences and evidence, not number of comments or identities of reviewers.

## Reviewer disagreement

Preserve conflicting evidence and assumptions. Check whether reviewers assessed the same source revision and scope. When there is no decisive witness, show alternatives and ask the responsible stakeholder to decide; do not auto-merge contradictory policies.

## Actionable output

A compact table can include: ID, severity, source/revision, observed vs expected, affected actors, next verification, owner and status. Include a sample corrected requirement or acceptance criterion only when the source permits it.

Do not fill a review with exhaustive generic categories. Prioritize issues that would materially change a decision, a user's outcome, an integration contract or a test.

## Approval and read-back

A reviewer's “approve” suggestion is not proof a stakeholder signed off or a provider changed. Track accepted resolutions against updated source files or real provider responses, and ensure unrelated content was preserved.

For independently executed code/diagram tests, include exact tool/runtime, command, source revision, outcome and the negative case where meaningful. If the test was not run, say so explicitly.
