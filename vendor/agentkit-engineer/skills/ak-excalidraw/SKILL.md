---
name: ak-excalidraw
description: Create or edit Excalidraw-compatible architecture, data-flow and workflow diagrams, including codebase auto-diagramming, with editable source and rendered validation.
metadata: {port: angent-fallback, mode: adapted}
---

# Excalidraw — Portable Fallback

Use when the user wants an **editable Excalidraw-style diagram**.

For inline documentation, Mermaid may be simpler. For tightly controlled publish-grade SVG/PNG, Tech Graph may be a better fit.

## Load progressively

- `references/diagram-model.md` — convert a system/flow into diagram elements.
- `references/layout-validation.md` — keep the drawing readable.

## Modes

### Live canvas

Use an available Excalidraw/MCP/canvas integration when the harness exposes one and live iterative editing is useful.

### File based

Generate/edit `.excalidraw` JSON through deterministic file tooling and render/preview it with the best available viewer/exporter.

### Codebase auto-diagram

When asked to “diagram this repo/architecture”:

1. Scout the relevant system boundary.
2. Identify components, ownership, external systems and important flows.
3. Build the semantic diagram model.
4. Generate the Excalidraw artifact.
5. Render and self-review it.

Do not visualize every directory as a box.

## Workflow

1. Identify the relation the diagram must communicate.
2. Choose a small visual vocabulary.
3. Plan primary reading direction and grouping.
4. Generate the editable artifact.
5. Render/preview.
6. Fix overlaps, edge ambiguity, scale and text issues.
7. Export SVG/PNG when requested and supported.

If Excalidraw-specific tooling is unavailable, produce an equivalent supported diagram only when the user accepts a degraded destination.
