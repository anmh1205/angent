# Selecting an ANGENT BA specialist by deliverable and source

**Provenance:** Adapted from MIT Dev BA Kit / rules/doc-selection.md (Edward Ngo, 2026), https://github.com/nv-minh/dev-ba-kit. Specialist selection is performed by ANGENT Root/Hub; this is reference guidance, not a second router.

## Choose the work product, not a command keyword

| Actual question or required output | Suitable specialist family | Essential input or stop condition |
|---|---|---|
| Is an idea worth testing; who buys and what alternatives exist? | ba-discover, ba-prd, ba-roadmap | Customer/market claims must be researched and dated |
| What do users need and why does the organization invest? | ba-brainstorm, ba-urd, ba-brd, ba-prd-epic | Stakeholder evidence, scope, buyer and decision owner |
| What exact behavior, rule, interface or code-observed behavior exists? | ba-srs, ba-reverse-doc, ba-code-to-srs | Accepted decisions or pinned implementation sources |
| What does each actor achieve, and how can it be accepted? | ba-usecase, ba-userstory, ba-ac | Real FR/BR, actors and observable success/denial |
| Which screen, path or prototype must reviewers manipulate? | ba-user-flow, ba-wireframe-ascii, ba-wireframe-html, ba-prototype-html, ba-prototype-next, ba-figma | Approved screen model; real runtime only if available |
| What external API should be chosen, designed, mapped or tested? | ba-api-assess, ba-api-doc, ba-api-design, ba-api-map, ba-api-checklist, ba-api-test, ba-api-readiness | Actual source API specification and provider access for runtime claims |
| Which boundaries and failures must tests cover? | ba-test-checklist, ba-test-cases, ba-playwright-gen | Source FR/AC/CHK and executable environment where promised |
| What is inconsistent, changing, unverified or blocked? | ba-gap, ba-doc-drift, ba-ask, ba-cr, ba-dashboard, ba-kg | Current source revisions; no invented acceptance |
| What needs to be published, linked or handed over? | ba-jira, ba-confluence, ba-export, ba-preview, ba-reverse-preview, ba-userguide, ba-meet, ba-update-overview, ba-delegate | User authorization, actual provider/file capabilities and read-back |

For a visual diagram, use diagram-selection.md to choose process/activity, BPMN, sequence, state, ERD or D2. The best response may be prose and one source table, not a diagram.

## Cross-family handoff

A sensible conceptual lineage is needs and objectives → product capabilities → functional rules and quality constraints → actor behavior and interfaces → acceptance/test evidence → controlled release. This is a **traceability model**, not a compulsory pipeline of all documents. One small product decision may need only a BR and a negative test; a broad regulated workflow may require many artifacts.

Existing accepted project files take precedence over template paths. A skill does not create missing upstream decisions to satisfy its own input contract. Preserve uncertainty and use the present user/host permissions.

## Example

“Show an API error message on a login screen” requires the actual error contract, a source-linked screen model and a runnable mock or frontend test. The full commercial API assessment workflow is unnecessary if the integration provider and interface are already decided. Correct method selection minimizes irrelevant generated files.

## Verification

Check that the selected kit added specialist reasoning or execution beyond ANGENT Core, used actual source IDs, chose a runnable provider only when present, and returned an artifact appropriate to the user's stated medium. A citation, count or attractive file is not evidence that the next system actually consumed the work.
