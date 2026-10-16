---
name: figma-demo
description: Construct a stakeholder walkthrough using editable Figma prototype.
---

# figma-demo: Construct a stakeholder walkthrough using editable Figma prototype

## Applicability and context

Use this specialist when a requested Figma deliverable needs **construct a stakeholder walkthrough using editable figma prototype**. Gather only the context that changes the output: approved frames, userflow, demo scenario, required interactions. Preserve project-approved semantics and styles. ANGENT Root retains task intent, user authority, tool selection, reasoning, and completion checks.

## Diagram/design method

Create explicit click paths; review transitions for missing destinations; distinguish mocked states; record only if host supports authorized video capture. Model semantic entities and relationships **before** canvas geometry. Prefer stable node/edge identifiers and update-in-place semantics where the actual native tool supports them. Work on only the approved document/selection; preserve existing user edits and component identity.

## Target deliverable

Produce **runnable Figma prototype and demo checklist or fallback storyboard**. If live Figma tools are available and permission confirmed, create or edit actual editable objects and read back the changed target state. Otherwise provide a structured model and clear unsupported-operations section rather than pretending to have made canvas changes.

## Review gate

- No claim that video exists or prototype runs without tool evidence.
- Check role ownership, meaningful labels, accessible names, off-canvas/clipped nodes, edges without endpoints, rendering clarity and contradiction with accepted BA requirements where applicable.
- Distinguish structural validation from rendered visual QA; inspect native Figma result if tool exists.

## References

For portable graph data shape see `../figma-activity/references/diagram-model.md`; for authorized tool boundaries consult `extensions/angent-figma/adapter/routing.md` when available in your host. No proprietary Reqwise source is included.
