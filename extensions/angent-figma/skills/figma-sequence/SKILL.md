---
name: figma-sequence
description: Model synchronous and asynchronous cross-component messages.
---

# figma-sequence: Model synchronous and asynchronous cross-component messages

## Applicability and context

Use this specialist when a requested Figma deliverable needs **model synchronous and asynchronous cross-component messages**. Gather only the context that changes the output: participants, call protocols, success and error replies. Preserve project-approved semantics and styles. ANGENT Root retains task intent, user authority, tool selection, reasoning, and completion checks.

## Diagram/design method

Align lifelines and time order; show responses/timeouts/retries; avoid fabricated APIs; compare message names to contract. Model semantic entities and relationships **before** canvas geometry. Prefer stable node/edge identifiers and update-in-place semantics where the actual native tool supports them. Work on only the approved document/selection; preserve existing user edits and component identity.

## Target deliverable

Produce **editable sequence diagram with trace references**. If live Figma tools are available and permission confirmed, create or edit actual editable objects and read back the changed target state. Otherwise provide a structured model and clear unsupported-operations section rather than pretending to have made canvas changes.

## Review gate

- No calls without meaningful result or explicit fire-and-forget behavior.
- Check role ownership, meaningful labels, accessible names, off-canvas/clipped nodes, edges without endpoints, rendering clarity and contradiction with accepted BA requirements where applicable.
- Distinguish structural validation from rendered visual QA; inspect native Figma result if tool exists.

## References

For portable graph data shape see `../figma-activity/references/diagram-model.md`; for authorized tool boundaries consult `extensions/angent-figma/adapter/routing.md` when available in your host. No proprietary Reqwise source is included.
