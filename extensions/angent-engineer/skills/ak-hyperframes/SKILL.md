---
name: ak-hyperframes
description: Build and render HTML-first HeyGen HyperFrames video compositions with pinned-CLI timing contracts, preview/lint and optional authorized cloud rendering.
license: Apache-2.0
metadata: {port: angent-fallback, mode: degraded}
---

# HyperFrames — Portable Fallback

Stable Engineer 2.19.0 HyperFrames uses the HeyGen HTML-first video CLI (pinned source example **hyperframes@0.7.99**). It is distinct from Remotion's React composition model or an arbitrary browser screen recording. The native CLI, renderer and remote HeyGen account are optional dependencies, **not** included by this Markdown.

Read `references/hyperframes-runtime.md` for preflight and the HTML timing protocol.

## Native workflow

1. Inspect the installed HyperFrames package/version and `--help`; the pinned `npx -y hyperframes@0.7.99` may download/execute a package and requires user authorization.
2. Scaffold the native composition in an approved output directory; inspect the package's generated structure before modifying it.
3. Implement HTML/CSS/JS composition using the actual **data-composition-id, data-start, data-width, data-height** timeline contract and any required duration, transition and audio properties from the matching version. Do not invent attribute names based on another renderer.
4. Preview in the local dev runtime and verify temporal order, canvas aspect ratio, fonts, asset loading, text legibility and visual synchronization.
5. Run the native lint/validation step to detect malformed timing/element metadata **before** rendering; render the MP4 using supported help-verified commands.
6. Inspect media metadata and representative frames/playback (start, transitions and end). Blank/short outputs are failures even with an exit-zero render; revisit timeline attributes.
7. Cloud rendering is a **separate** effect (native `hyperframes cloud render` pattern) requiring a real `HEYGEN_API_KEY`, privacy/billing authority and confirmation of uploaded assets; never call it automatically.

## Portable path

Where HyperFrames is unavailable, use another **actually available** browser/video renderer for the generic HTML-first animation goal or Remotion for React-driven video. Preserve dimensions, timing, asset semantics and a verified file output; label HyperFrames-specific animation/hosting features unavailable rather than claiming parity with a different engine.

**Capability:** VERIFIED_DEGRADED. A local HTML preview is not an MP4 and no exporter is implied by the presence of this skill.
