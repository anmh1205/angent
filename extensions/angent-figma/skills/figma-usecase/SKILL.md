---
name: figma-usecase
description: Define editable actors, use cases and system boundary.
---

# figma-usecase: Define editable actors, use cases and system boundary

## Applicability and context

Use this specialist when a requested Figma deliverable needs **define editable actors, use cases and system boundary**. Gather only the context that changes the output: business actors, permissions, candidate use cases. Preserve project-approved semantics and styles. ANGENT Root retains task intent, user authority, tool selection, reasoning, and completion checks.

## Diagram/design method

Normalize actor goals; mark include/extend only with correct semantics; label boundary and external actors; cross-check SRS and AC. Model semantic entities and relationships **before** canvas geometry. Prefer stable node/edge identifiers and update-in-place semantics where the actual native tool supports them. Work on only the approved document/selection; preserve existing user edits and component identity.

## Target deliverable

Produce **use case graph with actor links and exclusions**. If live Figma tools are available and permission confirmed, create or edit actual editable objects and read back the changed target state. Otherwise provide a structured model and clear unsupported-operations section rather than pretending to have made canvas changes.

## Review gate

- Use cases denote business capabilities, not single UI buttons.
- Check role ownership, meaningful labels, accessible names, off-canvas/clipped nodes, edges without endpoints, rendering clarity and contradiction with accepted BA requirements where applicable.
- Distinguish structural validation from rendered visual QA; inspect native Figma result if tool exists.

## References

For portable graph data shape see `../figma-activity/references/diagram-model.md`; for authorized tool boundaries consult `extensions/angent-figma/adapter/routing.md` when available in your host. No proprietary Reqwise source is included.
