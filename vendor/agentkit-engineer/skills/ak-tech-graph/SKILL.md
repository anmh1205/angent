---
name: ak-tech-graph
description: Generate publish-grade technical diagrams such as architecture, data-flow, flowchart, sequence, agent/memory, topology and UML-style visuals as deterministic SVG with optional PNG export.
metadata: {port: angent-fallback, mode: adapted}
---

# Tech Graph — Portable Fallback

Use when the user wants a **finished technical diagram artifact**, not a knowledge graph and not merely an inline Mermaid snippet.

For knowledge-graph extraction/querying, use `ak-graphify`.

## Load progressively

- `references/diagram-language.md` — choose diagram type, node/edge vocabulary and layout.
- `references/svg-output.md` — create valid portable SVG and optional PNG.
- `references/visual-review.md` — inspect legibility, semantics and render quality.

## Output routing

Prefer:
- **Mermaid** when an inline documentation diagram is sufficient;
- **Tech Graph** when the deliverable needs controlled layout, publish-grade SVG/PNG, branding/style, or diagram types that require manual visual composition.

## Workflow

1. Identify the relationship/system the diagram must explain.
2. Select the smallest diagram type that represents it truthfully.
3. Build the semantic model first: nodes, groups, flows, states and edge meaning.
4. Choose a readable layout and visual hierarchy.
5. Generate deterministic SVG using the available file/code tooling.
6. Validate SVG/XML and render it.
7. Export PNG only when requested or useful for the destination.
8. Inspect the rendered artifact and fix overlaps, clipping, ambiguous arrows and unreadable text.
9. Return both editable/vector source and raster export when both are useful.

## Runtime portability

Do not require `rsvg-convert`.

For rasterization use the best available deterministic renderer, for example:
- `rsvg-convert`;
- Inkscape;
- ImageMagick when SVG support is reliable;
- browser/headless rendering;
- another project-native SVG renderer.

If no rasterizer exists, deliver verified SVG and state that PNG export is unavailable.

## Quality

A technical diagram must communicate a real relationship. Decorative complexity is not quality.

Do not use an image-generation model for exact architecture/flow semantics when deterministic vector drawing is available.
