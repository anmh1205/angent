---
name: figma-activity
description: Diagram business activities with responsible owners.
---

# figma-activity: Diagram business activities with responsible owners

## Applicability and context

Use this specialist when a requested Figma deliverable needs **diagram business activities with responsible owners**. Gather only the context that changes the output: approved workflow, actors, branch conditions. Preserve project-approved semantics and styles. ANGENT Root retains task intent, user authority, tool selection, reasoning, and completion checks.

## Diagram/design method

Draw directed tasks/decisions/start/end; group by swimlane where useful; label outgoing decision guards; include compensating/retry paths. Model semantic entities and relationships **before** canvas geometry. Prefer stable node/edge identifiers and update-in-place semantics where the actual native tool supports them. Work on only the approved document/selection; preserve existing user edits and component identity.

## Target deliverable

Produce **editable activity diagram with edge semantics**. If live Figma tools are available and permission confirmed, create or edit actual editable objects and read back the changed target state. Otherwise provide a structured model and clear unsupported-operations section rather than pretending to have made canvas changes.

## Review gate

- All reachable nonterminal nodes lead to meaningful exits.
- Check role ownership, meaningful labels, accessible names, off-canvas/clipped nodes, edges without endpoints, rendering clarity and contradiction with accepted BA requirements where applicable.
- Distinguish structural validation from rendered visual QA; inspect native Figma result if tool exists.

## References

For portable graph data shape see `../figma-activity/references/diagram-model.md`; for authorized tool boundaries consult `extensions/angent-figma/adapter/routing.md` when available in your host. No proprietary Reqwise source is included.
