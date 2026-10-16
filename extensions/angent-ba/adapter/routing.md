# Business Analysis Kit Adapter

This is a bounded specialist under ANGENT Hub, not a second planning agent or memory system. Core Reasoning owns the actual decision; Core Authoring owns reader-comprehensible prose; Execution owns mutations; Quality owns outcome verification. Use BA methods only when the requested artifact or specialist analysis needs domain-specific discipline.

## Selection and interoperability

- Prefer `ba-brainstorm` for unresolved requirements; never demand interview questions already answered in project evidence.
- Select `ba-srs` for contract-grade FR/NFR/BR and `ba-userstory`/`ba-ac` for backlog refinement; use the same stable IDs and accepted baseline.
- Use `ba-gap`, `ba-doc-drift`, `ba-cr`, and `ba-kg` as different *views* on project evidence, not separate sources of truth.
- For implementation, API execution, Playwright, deployments, native Figma and provider mutations, cooperate with a real Engineer/tool specialist only when needed; BA methods alone cannot claim those effects.
- If a request is a general explanation, ANGENT Core handles it; do not activate `ba-ask` merely because the words resemble a business question.

## Artifact policy

Stable references `FR-*`, `NFR-*`, `BR-*`, `UC-*`, `US-*`, `AC-*`, `TC-*` express project-local IDs, never imply a proprietary global convention. Evidence has source, revision and confidence. Use `ba-kg/references/operating-model.md` as the canonical shared BA artifact contract for all source Skills and a portable reference within each host package. Source-of-truth is the user's current project providers, not the graph file itself.

Never copy commercial AI4BA prompts/templates. The entries here are independently authored methods and carry no claim of behavioral parity with inaccessible commercial materials.
