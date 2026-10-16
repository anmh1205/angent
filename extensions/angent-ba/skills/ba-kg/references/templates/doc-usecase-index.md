---
type: usecase-index
feature: {{feature_slug}}
status: draft
updated: {{date}}
links: []
---

# {{feature_name}} — use case inventory

Use stable actor-goal identities that are already accepted in the project. A use-case index is a *source mapping*, not proof an actor flow has been tested or implemented.

## Use cases

| Slug | Status | Primary actor | Covers FR | Screens | Related errors | Open decisions | Source |
|---|---|---|---|---|---|---|---|
| [uc-{{id}}]({{existing_relative_usecase_path}}) | draft | {{actor}} | FR-{{feature}}-001 | {{screen_ids}} | E-{{feature}}-001 | {{question_or_none}} | {{source_revision}} |

## Data access and responsibility

| Use case ID | Entity | Interaction: C / R / U / D | Business authorization | Evidence |
|---|---|---|---|---|
| UC-{{id}} | {{entity}} | {{C_or_R_or_U_or_D}} | {{guard_or_unknown}} | {{source}} |

## Relationships

| Type | From | To | Why this relationship holds |
|---|---|---|---|
| include / extend / generalization | {{usecase_id}} | {{usecase_id}} | {{source_aligned_rationale}} |

## Diagram (optional, only after actual rendering)

- Editable source: {{verified_local_diagram_source_or_not_produced}}
- SVG: {{existing_rendered_svg_or_not_produced}}
- Renderer and check: {{actual_local_tool_command_or_unverified}}

Do not embed an SVG or claim a viewable image until a real renderer produced it. The BA use-case method may emit PlantUML source, but ANGENT does not bundle a native PlantUML renderer or the source kit's own render helper. For Figma, confirm a live capable provider and read back editable nodes.

## Linked sources and unresolved gaps

- Requirements and error matrix: {{real_relative_SRS_path}}
- Screen inventory: {{real_relative_screen_model_or_wireframe_path}}
- Unresolved cross-document references: {{ids_or_none}}

A source graph or gap audit can check **explicit IDs**, not invent a mandatory project-global traceability file. Handle missing FR and error references as review items rather than inserting invented requirements.
