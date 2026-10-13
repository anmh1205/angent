---
name: ak-shader
description: Design and debug GLSL-style procedural shaders with explicit coordinate systems, SDF/noise/color math and measurable performance constraints.
metadata: {port: angent-fallback, mode: portable}
---

# Shader — Portable Fallback

## Load progressively

- `references/building-blocks.md` — coordinates, SDF, patterns, noise and color.
- `references/debug-performance.md` — diagnose visual/numeric/performance failures.

## Workflow

1. Identify shader language/runtime version and uniforms.
2. Normalize coordinates explicitly.
3. Build the effect in layers.
4. Preview after each meaningful layer.
5. Keep numeric ranges/space transforms understandable.
6. Animate with time only after static structure works.
7. Profile expensive loops/noise/layers when target hardware matters.

Explain the mechanism, not only the final code.
