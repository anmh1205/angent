---
name: ak-mermaidjs-v11
description: Author Mermaid v11 diagrams, validate them for their actual target renderer, and render or integrate accessible SVG/PNG/PDF where supported.
metadata: {port: angent-fallback, mode: adapted}
---

# Mermaid.js v11 — Portable Fallback

Use Mermaid for relationships that genuinely benefit from a diagram: process decisions, interactions, state transitions, data cardinality, architecture, sequence, time or quantified flows. The outcome can be **inline Mermaid source**, a verified rendered image, or a diagram embedded in an application/document. Do not substitute Mermaid for a different requested chart/media format, or add it merely to decorate prose.

This fallback retains the stable Engineer 2.19.0 diagram-authoring, configuration, CLI and embedding workflows. A Markdown file cannot provide a Mermaid renderer, browser or npm CLI by itself. Discover the actual destination/version/tools first and distinguish authored source, parser acceptance and rendered/visually inspected output.

## Select by semantics

- Flowchart: process, decisions, dependencies and control routing.
- Sequence: time-ordered messages, activations, alternatives and concurrency.
- State: reachable states, event-labelled transitions, guards and terminal paths.
- ER: entities, schema/cardinality and optionality.
- Class: static types, inheritance, composition and interfaces.
- Gantt, timeline, journey, git graph, mindmap or requirement: only for the corresponding schedule, chronology, user experience, commit topology, hierarchy or traceability.
- C4, architecture-beta, block-beta, xychart-beta, Sankey, radar, treemap, packet and other newer/beta formats: first verify the destination renderer supports the exact grammar. Do not mark an unsupported type portable solely because upstream v11 documentation lists it.

Read **references/diagram-contracts.md** for syntax and semantic examples, including core and advanced types. Read **references/rendering-and-accessibility.md** for CLI, JavaScript, Markdown and SVG output, security and accessibility.

## Authoring workflow

1. State which question the diagram answers and identify entities, relations, directions and uncertain edges from the underlying source/requirements.
2. Choose the smallest diagram type that faithfully represents those relations. Separate source facts from inferred behavior; do not draw non-existent dependencies or success paths.
3. Author Mermaid source with meaningful IDs and readable labels. For flowcharts, prefer explicit branching conditions; for sequences, identify sender/receiver and order; for state diagrams, label triggers and failure paths; for ER diagrams, use accurate cardinality.
4. Bound complexity. Split independent concerns or use meaningful subgraphs rather than shrinking text to fit one unreadable image.
5. Identify the **actual parser/render target** (GitHub, docs platform, application Mermaid package, Mermaid CLI). Check version-sensitive and beta diagram types before relying on them.
6. Validate syntax with the target parser where possible; render/export and visually inspect labels, arrows, overlap, clipping, color/contrast and mobile/print readability when the requested output needs an image.
7. Add concise surrounding explanation, accessible title/description or a textual alternative when required by the destination. Do not assume any diagram alone communicates all engineering preconditions.

## Deliverables and honest evidence

Inline Markdown output uses a Mermaid fenced block when the destination supports it. File/image output requires a real renderer: Mermaid CLI (mmdc) for SVG/PNG/PDF, or a project-approved browser/Node renderer. Installation, CDN loading, export and file mutation require runtime capability/authorization and must not be claimed until observed.

Report the diagram source, chosen syntax/destination, syntax validation result, image rendering/visual review results and material limitations separately. A parse success does **not** establish correct data flow, visual quality or renderer compatibility across platforms.

For complex technical SVG diagrams whose labels and edges must be publication-grade, combine the Mermaid source with Tech Graph's rendered-layout inspection when actually available. Prefer a different representation when Mermaid cannot express the relation faithfully.
