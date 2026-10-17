---
type: roadmap
status: draft
updated: {{date}}
links: []
---

# {{product_name}} — decision-based roadmap

## Evidence and time horizon

- Accepted product outcomes: {{real_PRD_or_decision_source}}
- Planning horizon: {{period_and_team_capacity_if_known}}
- Evidence snapshot: {{revision_or_date}}
- Open allocation decisions: {{unresolved_owners_and_constraints}}

## Prioritization (only score with measured or explicitly assumed inputs)

| Capability ID | Buyer/user value | Impact evidence | Confidence basis | Effort basis | Dependencies | Proposed order |
|---|---|---|---|---|---|---|
| CAP-{{feature}}-01 | {{problem_and_value}} | {{actual_source_or_unknown}} | {{confidence_basis}} | {{estimate_and_owner_or_unknown}} | {{dependencies}} | {{proposed_or_approved}} |

If RICE or another scoring rule is used, state its exact inputs, scales, weights and population. Missing reach or effort is **unknown**, not zero. A formula does not turn an unsupported estimate into fact.

## Delivery horizon

| Horizon | Capability / outcome | Business approval | Dependency or exit condition |
|---|---|---|---|
| Now | {{capability}} | {{accepted_decision_or_uncommitted}} | {{completion_evidence}} |
| Next | {{capability}} | {{decision_state}} | {{required_validation}} |
| Later | {{capability_hypothesis}} | {{unapproved_or_deferred}} | {{evidence_that_would_change_priority}} |

'Now' does not automatically mean development has begun. Commitment is established only from actual owner decisions or provider state.

## Changes and trade-offs

| Decision | Alternative rejected or deferred | Consequence | Date, approver and source |
|---|---|---|---|
| {{choice}} | {{alternative}} | {{consequence}} | {{record}} |

## Release observations

{{real_delivery_risks_dependencies_and_known_unknowns}}

Do not impose a fixed docs/_product/prd.md path or silently overwrite an existing roadmap. ANGENT Root and the authorized project sources determine the actual location, schedule and ownership.
