---
name: ak-diagram
description: Compile or render reviewable system/editorial diagrams from typed structure, Mermaid, or prepared HTML using the capabilities actually available in the active harness.
metadata: {port: angent-fallback, mode: adapted}
---

# Diagram — Portable Fallback

Use when the requested **artifact is a diagram**, not merely when a topic could be illustrated.

Read `references/diagram-contract.md`.

## Route by artifact

Prefer:
- typed structured input for architecture/workflow/sequence/dataflow/lifecycle maps when a compatible compiler exists;
- Mermaid source for reviewable textual diagrams;
- prepared HTML/SVG for editorial or interactive presentation when supported.

Do not convert a request for editable Mermaid into an opaque raster image.

## Workflow

1. Identify the relation the diagram must encode and the requested output format.
2. Inspect available filesystem, renderer, browser, image/video, and dependency capabilities.
3. Choose the closest route that preserves the requested semantics.
4. Generate the source/artifact deterministically where possible.
5. Render/preview when a renderer exists.
6. Inspect labels, grouping, arrows, clipping, contrast, and interaction.
7. Report the exact artifact plus any capability gap that prevented full verification.

If the upstream-style typed-IR/editorial compiler is not available, do **not** claim that exact compiler behavior. Use a semantically adequate available route or return a blocked/degraded result.

Use `ak-mermaidjs-v11` when Mermaid source itself is the deliverable.
