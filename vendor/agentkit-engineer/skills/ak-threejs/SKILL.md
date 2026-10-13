---
name: ak-threejs
description: Build and debug Three.js/WebGL/WebGPU scenes with explicit scene graph, asset lifecycle, interaction and measurable performance behavior.
license: MIT
metadata: {port: angent-fallback, mode: portable}
---

# Three.js — Portable Fallback

Use for interactive 3D web experiences.

## Load progressively

- `references/scene-architecture.md` — scene/update/render organization.
- `references/assets-lifecycle.md` — models, textures, loading and disposal.
- `references/performance-debug.md` — profiling and rendering bottlenecks.

## Workflow

1. Inspect installed Three.js/runtime version.
2. Define scene graph, coordinate system and camera.
3. Separate load/init/update/render/input responsibilities.
4. Add assets with explicit loading/error/disposal.
5. Add interaction/animation deliberately.
6. Verify resize/pixel ratio/device behavior.
7. Profile when performance matters.
8. Test teardown/navigation for leaks.

Use examples as version-specific references, not code to paste blindly.
