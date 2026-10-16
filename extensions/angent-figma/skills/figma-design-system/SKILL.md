---
name: figma-design-system
description: Create editable reusable Figma foundations from approved art direction.
---

# figma-design-system: Create editable reusable Figma foundations from approved art direction

## Applicability and context

Use this specialist when a requested Figma deliverable needs **create editable reusable figma foundations from approved art direction**. Gather only the context that changes the output: brand/design tokens, accessible states, component inventory, target file. Preserve project-approved semantics and styles. ANGENT Root retains task intent, user authority, tool selection, reasoning, and completion checks.

## Diagram/design method

Read existing variables/components first; propose incremental tokens and variants; edit only with live tool and permission; inspect geometry, contrast, responsive rules. Model semantic entities and relationships **before** canvas geometry. Prefer stable node/edge identifiers and update-in-place semantics where the actual native tool supports them. Work on only the approved document/selection; preserve existing user edits and component identity.

## Target deliverable

Produce **Figma variables, styles, components, variants plus audit or offline spec**. If live Figma tools are available and permission confirmed, create or edit actual editable objects and read back the changed target state. Otherwise provide a structured model and clear unsupported-operations section rather than pretending to have made canvas changes.

## Review gate

- No claim of created component until read-back on target file.
- Check role ownership, meaningful labels, accessible names, off-canvas/clipped nodes, edges without endpoints, rendering clarity and contradiction with accepted BA requirements where applicable.
- Distinguish structural validation from rendered visual QA; inspect native Figma result if tool exists.

## References

For portable graph data shape see `../figma-activity/references/diagram-model.md`; for authorized tool boundaries consult `extensions/angent-figma/adapter/routing.md` when available in your host. No proprietary Reqwise source is included.
