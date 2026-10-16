---
type: traceability
updated: {{date}}
links: []
---

# {{feature_or_project}} — requirement traceability review

## Source boundary

- Inspected URD / BRD / PRD / SRS / backlog / tests: {{actual_source_paths_and_revisions}}
- Excluded and unavailable evidence: {{uninspected_scope}}
- Structural graph revision: {{source_graph_or_review_record}}

## Declared relationship model

UN (user need) → BO (business objective) → CAP (product capability) → FR/NFR/BR (requirements) → AC/CHK/TC (acceptance or test evidence). UC and US explain actors and delivery slices; an ID association does not by itself establish semantic equivalence.

## Source-backed stage coverage

| Stage | Inspected population | Explicitly linked | Missing/unreviewed | Interpretation |
|---|---|---|---|---|
| User needs to objectives | {{total_UN}} | {{linked_UN}} | {{unlinked_UN}} | Declared business justification |
| Objectives to capabilities | {{total_BO}} | {{linked_BO}} | {{unlinked_BO}} | Explicit product coverage |
| Capabilities to FR | {{total_CAP}} | {{linked_CAP}} | {{unlinked_CAP}} | Design scope |
| FR to a TC artifact | {{total_FR}} | {{linked_FR}} | {{unlinked_FR}} | Test specification **only** |
| Executed passing tests | {{required_TC_or_unknown}} | {{executed_pass_TC_or_unknown}} | {{not_run_or_unknown}} | Requires actual runner evidence |

## Per-requirement proof and gaps

| FR ID | Exact upstream path | Explicit TC path | Execution evidence | Review/action |
|---|---|---|---|---|
| FR-{{feature}}-001 | {{UN_BO_CAP_FR_chain_or_missing}} | {{FR_AC_CHK_TC_chain_or_missing}} | {{run_link_or_not_executed}} | {{owner_and_next_action}} |

Use the existing ANGENT BA extractor with actual accepted Markdown input when compatible, then inspect lifecycle.per_requirement and unresolved_external_refs. Do not fill a missing stage with hypothetical IDs to improve coverage.

## Change and approval

| Changed ID | Downstream dependent IDs | Business approver / unresolved policy | Source revision |
|---|---|---|---|
| {{id}} | {{impacted}} | {{decision}} | {{source}} |

This is a **read-only report until authorized**. Source links are structural evidence, not proof of stakeholder validation, production deployment or test execution.
