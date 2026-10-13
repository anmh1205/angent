---
name: ak-mermaidjs-v11
description: Create Mermaid diagrams that encode real flow, state, sequence, data or architecture relationships using syntax supported by the target renderer.
metadata: {port: angent-fallback, mode: portable}
---

# Mermaid — Portable Fallback

Use Mermaid when a relationship is clearer as a diagram than as prose.

## Choose diagram type

- flowchart → process/dependency;
- sequence → message interaction;
- state → lifecycle;
- ER → data relations;
- class → static type structure;
- timeline/Gantt/journey → only when the semantics fit.

## Workflow

1. Identify the exact relationship to show.
2. Keep node labels concise.
3. Use consistent direction/grouping.
4. Avoid decorative arrows with no semantic meaning.
5. Validate syntax using the renderer/version available at the destination.
6. Render/preview when possible.

Do not create Mermaid just to increase visual density.
