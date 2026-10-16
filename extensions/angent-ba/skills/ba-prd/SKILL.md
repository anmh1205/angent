---
name: ba-prd
description: Produce a coherent product requirements document from validated opportunities.
---

# ba-prd: Produce a coherent product requirements document from validated opportunities

## Trigger and necessary evidence

Use this method when the user needs **produce a coherent product requirements document from validated opportunities**, not because a generic question merely mentions the subject. Required inputs to look for: users, business objective, scope boundary, constraints, existing decisions. Read existing accepted artifacts first; ask only for consequential absent decisions. If the inputs are incomplete, produce a bounded draft with explicit unresolved questions instead of fabricating agreements.

## Specialist method

Separate problem statement from proposed solution; rank goals and measurable outcomes; reconcile features with business rules and non-goals; tag unresolved decisions. For each decision, capture (a) observed or approved basis, (b) consequence for actors, data and failure conditions, and (c) the next verifiable action. Reuse project identifiers and cite the source revision of any requirement you derive. Verify whether this is a design proposal or observed live behavior before asserting it as fact.

## Deliverable

Produce **PRD with objectives, personas, capabilities, scope, assumptions, NFR references and release criteria**. Put the decision or useful artifact first, then the needed context and source links. Use `../ba-kg/references/operating-model.md` for ID provenance, graph semantics and change boundaries. Applicable original templates are indexed at `../ba-kg/references/template-index.md`; use a template only where it clarifies the user's actual task.

## Acceptance checks

- Each capability traces to a user/business problem; no imagined market facts.
- Detect missing success, negative, edge, permission and recovery paths when applicable; label any unverified runtime effects clearly.
- Review the result against current project evidence and unaffected approved decisions, not merely formatting or file existence.

## ANGENT boundary

ANGENT Core supplies general intent/context/reasoning/authoring; this Skill supplies only domain-specific discipline. Never invent stakeholder choices, interviews, production evidence, API responses, source lines or compliance conclusions. Treat source, inference and approved decisions separately; unresolved choices remain questions. Do not modify a provider, remote system or other files without checking ANGENT Execution permissions.
