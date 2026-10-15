---
name: ak-shader
description: Author and debug GLSL/WebGL fragment shaders with correct coordinates, SDF/noise math, version-specific compilation and GPU visual/performance checks.
metadata: {port: angent-fallback, mode: adapted}
---

# GLSL Shader — Portable Fallback

Use for procedural textures, distance-field geometry, noise/patterns, animation and shader effects in WebGL/Three.js/other graphics runtimes. Stable Engineer 2.19.0 describes fragment fundamentals, shader functions, shape/raster logic and progressively loaded math/reference patterns. Preserve the **rendering mechanism** rather than a generic 'write a shader' task.

Read `references/building-blocks.md` and `references/debug-performance.md`.

## Language/runtime contract

Identify GLSL ES 1.00/WebGL1 versus GLSL ES 3.00/WebGL2, three.js ShaderMaterial/RawShaderMaterial, or another target. Version affects precision declarations, `attribute/varying` versus `in/out`, and `gl_FragColor` versus named fragment outputs; do not paste incompatible boilerplate.

A fragment shader computes each fragment's output from interpolated coordinates/uniforms; it cannot safely assume arbitrary cross-fragment shared memory. Common uniforms include time, resolution, pointer position and textures; establish actual names from the target host rather than inventing bindings.

Normalize screen coordinates consistently, including aspect correction, texture UV origin, pixel density and derivatives. Compose simple signed-distance functions, `mix`, `smoothstep`, gradients, frequency/tiling/noise and fBm with numerical ranges and color space explicit.

## Build and debug

1. Start from the smallest static valid shader in the intended host, confirm compile/link errors.
2. Add one mathematical component at a time: shape/mask, coordinate mapping, color transformation, procedural noise, lighting and time evolution.
3. Visualize intermediate scalar masks/UVs and edge cases (zero resolution, NaN/divide-by-zero, precision on mobile, missing textures, extreme zoom) before introducing heavy animation.
4. Inspect actual rendered pixels at normal and atypical resolutions and device pixel ratios. Diagnose gamma/sRGB/linear mismatches, aliasing, banding, unstable temporal noise and seams at tile boundaries.
5. Profile GPU cost when relevant: loops, many noise octaves, branches, texture sampling and framebuffer passes. Simplify while preserving output semantics; avoid promises of cross-platform performance without measurements.
6. Return shader source, required uniforms/renderer version, observed compile/render checks and unsupported targets.

Without an actual GPU/browser shader compiler the outcome is **source with unverified visual/runtime behavior**, not a validated live effect.
