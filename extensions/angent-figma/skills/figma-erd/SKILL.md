---
name: figma-erd
description: Visualize entities, keys and foreign-key relationships.
---

# figma-erd: Visualize entities, keys and foreign-key relationships

## Applicability and context

Use this specialist when a requested Figma deliverable needs **visualize entities, keys and foreign-key relationships**. Gather only the context that changes the output: entity catalog, identifiers, cardinality and nullability. Preserve project-approved semantics and styles. ANGENT Root retains task intent, user authority, tool selection, reasoning, and completion checks.

## Diagram/design method

Create structured table/relationship model; preserve key types, optionality, relationship semantics and schema provenance. Model semantic entities and relationships **before** canvas geometry. Prefer stable node/edge identifiers and update-in-place semantics where the actual native tool supports them. Work on only the approved document/selection; preserve existing user edits and component identity.

## Target deliverable

Produce **editable ERD with connected entities and source mapping**. If live Figma tools are available and permission confirmed, create or edit actual editable objects and read back the changed target state. Otherwise provide a structured model and clear unsupported-operations section rather than pretending to have made canvas changes.

## Review gate

- No non-existent FK target or unverifiable relationship cardinality.
- Check role ownership, meaningful labels, accessible names, off-canvas/clipped nodes, edges without endpoints, rendering clarity and contradiction with accepted BA requirements where applicable.
- Distinguish structural validation from rendered visual QA; inspect native Figma result if tool exists.

## References

For portable graph data shape see `../figma-activity/references/diagram-model.md`; for authorized tool boundaries consult `extensions/angent-figma/adapter/routing.md` when available in your host. No proprietary Reqwise source is included.
