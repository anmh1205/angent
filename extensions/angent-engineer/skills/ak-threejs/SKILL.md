---
name: ak-threejs
description: Build and verify real Three.js/WebGL/WebGPU scene graphs, assets and animation using version-matched APIs and renderer performance evidence.
license: MIT
metadata: {port: angent-fallback, mode: degraded}
---

# Three.js — Portable Fallback

Use for interactive 3D scenes, GLTF/FBX assets, WebGL/WebGPU effects, animations, picking, physics, XR, architectural/product displays or data visualization. Stable Engineer 2.19.0 includes a **556 searchable example corpus**, an API/class index and category/use-case templates, plus scripts for searching them. Those assets and search scripts are **not bundled** here; a generic code example cannot honestly claim a catalog search.

Read `references/scene-architecture.md`, `references/assets-lifecycle.md`, `references/performance-debug.md` and `references/runtime-and-search.md`.

## Choose target backend

Inspect installed Three.js revision, project bundler and render backend. WebGPU support, API names and examples can vary materially by version and browser; treat source examples as versioned, not universal. Explicitly choose scene/camera/projection, renderer, coordinate spaces, tone mapping, color space, lighting/environment and pixel ratio before adding detail.

For native corpus available from the installed skill, use its real `scripts/search.py` with **examples/api/use-cases/categories** domains to narrow code exploration and cite match identity. If unavailable, use official Three.js current docs and local source, and disclose that no corpus hit was fetched.

## Scene behavior and lifecycle

Construct real scene graph, geometry/material/texture/model transforms, loading and asynchronous error paths. Prefer glTF/PBR workflow when appropriate; validate units/scale, normals, textures and scene origin. Separate init, update, input, render, resize, suspend and disposal. Use `requestAnimationFrame` only when interactive animation is needed and stop/cleanup after component unmount.

For picking, controls, lighting, skeletal animation, GPU simulation, postprocessing, WebXR and physics, verify actual backend, device and license support. Do not assume geometry API or WebGPU/WASM behaviors from older snippets. Release textures/buffers/materials, event listeners and animation loops on teardown.

## Validation and performance

1. Compile/build with installed Three.js/TS versions and inspect actual browser console for GL errors.
2. Preview representative viewport/device pixel ratios and camera extremes, resize, keyboard/pointer/touch controls and missing/slow assets.
3. Validate material colors (linear vs sRGB), overdraw, draw calls, GPU memory, frame time and adaptive quality under realistic load when performance matters.
4. Check browser/GPU feature detection and fallback, 3D loading progress, animation stop/restart, context loss/recovery and dispose/memory leak paths.
5. Return source/asset provenance, actual renderer/backend, observed visual/performance checks, tested devices and unresolved compatibility gaps.

**Capability:** VERIFIED_DEGRADED without the 556-example search bundle; Three.js code may still run through the user's installed project toolchain.
