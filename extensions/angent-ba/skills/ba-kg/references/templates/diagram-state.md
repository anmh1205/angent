---
type: srs-states
feature: {{feature}}
updated: {{date}}
---

# {{feature_name}} — state and transition review

## Entity and sources

- State-bearing entity: {{entity}}
- Related FR/BR/UC and actual source links: {{real_identifiers_and_paths}}
- Revision / approval state: {{revision_and_current_decision}}
- Scope: one entity per diagram; represent cross-entity processes separately.

## Allowed transitions

| From | Event or trigger | Guard | Action / side effect | To | Business source |
|---|---|---|---|---|---|
| {{source_state}} | {{event}} | {{guard}} | {{observable_side_effect}} | {{target_state}} | {{FR_or_BR_id}} |

## Invalid or disputed transitions

| From | Event | To | Why prohibited or unapproved | Expected response |
|---|---|---|---|---|
| {{state}} | {{trigger}} | {{invalid_target}} | {{rule_or_unknown}} | {{actual_contract_or_open_question}} |

## Diagram source and visual check

- Optional Mermaid stateDiagram source: {{actual_source_file_or_not_produced}}
- Actual renderer and checked image: {{renderer_output_or_not_run}}
- Invalid transitions covered by test: {{test_cases_or_not_executed}}

Verify unreachable states, competing event guards, missing recovery, forbidden transitions and data ownership. A valid state diagram is not evidence that the production state machine enforces it. Do not claim a visual render based only on a Markdown code fence.
