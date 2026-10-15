---
name: ak-tech-graph
description: Produce source-grounded, publish-ready SVG/PNG technical diagrams with explicit semantics, coherent visual style, deterministic validation and rendered visual review.
metadata: {port: angent-fallback, mode: adapted}
---

# Tech Graph — Portable Fallback

Use when the deliverable is a **finished, visually controlled technical diagram**: architecture, deployment, data flow, sequence, state, network, UML, use case, agent/memory, matrix or timeline. It is not a graph extraction/query engine (use Graphify/GKG) or merely an inline Mermaid document diagram (use Mermaid v11). Stable Engineer 2.19.0 has seven SVG style families and vendored generator/validation scripts; this fallback preserves their design/output semantics without asserting the scripts/templates exist here.

## Read only the relevant references

- **references/diagram-language.md** — choose view, nodes, edges, data/control semantics and topology.
- **references/styles-and-layout.md** — seven style families, selection, icon usage, spacing, connectors, captions and render order.
- **references/svg-output.md** — SVG construction, escaping, marker/XML validation and PNG export.
- **references/visual-review.md** — rendered-result verification and repair.

## Workflow

1. Identify the audience, exact system/question and target output (vector/raster/both); choose one abstraction level. Obtain source/requirements evidence for components, states, flows and dependencies rather than drawing guessed relationships.
2. Classify diagram type and specify entities, layers, groups, edge direction/meaning, failure paths, state transitions, legend and source uncertainty. For diagrams involving agent memory, show *read* and *write* paths separately where they differ.
3. Choose a style appropriate to the content/destination (from seven upstream families or authorized project brand tokens). Default to restrained flat-icon clarity when no visual direction is requested; avoid effect-heavy style for dense UML/sequence/data diagrams.
4. Plan the actual geometry. Reserve node and edge-label bounding boxes, connector corridors, ports, containers and consistent reading direction before rendering. Use named icons only if corresponding SVG assets are available/authorized; do not invent brand artwork.
5. Produce deterministic, portable SVG with escaped labels, meaningful viewBox, stable marker IDs, safe links, correct arrowheads and reproducible layout. Use actual template/generator scripts only if present and inspected; otherwise construct SVG directly with available file tooling.
6. Validate XML and SVG dependencies. Use any genuinely available SVG renderer (rsvg-convert, Inkscape, headless browser or tested native tool) to export required PNG at appropriate size.
7. **Inspect the rendered image**, including scale, labels, crossing arrows, lifelines, node interiors, overlays, legends, contrast and typography. Repair overlap/layout issues and re-render until the diagram is legible. XML validity does not prove readable or correct illustration.
8. Return verified generated paths and distinguish SVG source, raster export, parser validation and visual review. If an output cannot be generated/inspected, say so rather than claiming a finished artifact.

## Truth and visual quality

Do not create decorative boxes, arbitrary memory layers, redundant arrows or color-coded relations without evidence. Prefer orthogonal edge routes or purposeful curves, explicit guard/error labels, edge anchoring and clean spacing. For two or more line styles or arrow meanings, include a legend when ambiguity would otherwise remain. Do not make numeric spacing heuristics into universal geometry laws; check actual rendered text extents at the destination size.

Use Mermaid instead when native editable diagrams render correctly in the target document and bespoke vector styling adds no value. Use image generation only for explicitly desired illustrative imagery, not as a substitute for exact topology/labels/relationships or SVG editability.

## Capability boundary

The upstream Engineer bundle includes SVG templates, seven visual style guides, helper generators, rsvg-convert validation and a preview workflow. These are **not implicitly installed** with this Markdown fallback. Select verified runtime equivalents, preserve editable source, and never invent a successful render/export or local file path. Publication-quality verdict requires both semantic accuracy and a reviewed final render.
