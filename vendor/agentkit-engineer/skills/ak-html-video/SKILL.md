---
name: ak-html-video
description: Render video from HTML/CSS/JS compositions using an available HTML-to-video toolchain while keeping preview/render settings reproducible.
license: Apache-2.0
metadata: {port: angent-fallback, mode: adapted}
---

# HTML Video — Portable Fallback

Use when video content is naturally authored as HTML/CSS/JS.

## Workflow

1. Define dimensions, frame rate, duration and audio needs.
2. Build a deterministic HTML composition.
3. Preview key frames/timestamps.
4. Render through the installed HTML-video/browser capture toolchain.
5. Inspect the produced video for timing, clipping, font/load and animation issues.
6. Record the exact render command/config.

If the expected upstream renderer is unavailable, use a compatible browser-capture pipeline or recommend Remotion/another supported path.

Do not claim render success without inspecting the output artifact.
