---
name: ba-api-map
description: Align field semantics across API, domain and UI.
---

# ba-api-map: Align field semantics across API, domain and UI

## Trigger and necessary evidence

Use this method when the user needs **align field semantics across api, domain and ui**, not because a generic question merely mentions the subject. Required inputs to look for: source schema, internal data model, screen needs. Read existing accepted artifacts first; ask only for consequential absent decisions. If the inputs are incomplete, produce a bounded draft with explicit unresolved questions instead of fabricating agreements.

## Specialist method

Build three-column field mapping; document transformations, null semantics, enums and validation; detect lossy conversion. For each decision, capture (a) observed or approved basis, (b) consequence for actors, data and failure conditions, and (c) the next verifiable action. Reuse project identifiers and cite the source revision of any requirement you derive. Verify whether this is a design proposal or observed live behavior before asserting it as fact.

## Deliverable

Produce **Field mapping spec with examples and provenance**. Put the decision or useful artifact first, then the needed context and source links. Use `../ba-kg/references/operating-model.md` for ID provenance, graph semantics and change boundaries. Applicable original templates are indexed at `../ba-kg/references/template-index.md`; use a template only where it clarifies the user's actual task.

## Acceptance checks

- Required fields mapped; incompatible enum values flagged.
- Detect missing success, negative, edge, permission and recovery paths when applicable; label any unverified runtime effects clearly.
- Review the result against current project evidence and unaffected approved decisions, not merely formatting or file existence.

## ANGENT boundary

ANGENT Core supplies general intent/context/reasoning/authoring; this Skill supplies only domain-specific discipline. Never invent stakeholder choices, interviews, production evidence, API responses, source lines or compliance conclusions. Treat source, inference and approved decisions separately; unresolved choices remain questions. Do not modify a provider, remote system or other files without checking ANGENT Execution permissions.
