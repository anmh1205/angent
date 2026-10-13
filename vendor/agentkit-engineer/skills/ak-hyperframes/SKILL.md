---
name: ak-hyperframes
description: Build short HTML-first motion/video compositions using HyperFrames when installed, with a portable fallback to other HTML/video renderers.
license: Apache-2.0
metadata: {port: angent-fallback, mode: degraded}
---

# HyperFrames — Portable Fallback

If the HyperFrames CLI is installed, use its current official workflow for HTML-first video generation.

Otherwise preserve the capability through:
- HTML/CSS/JS composition;
- a supported browser-to-video renderer; or
- Remotion when React-based composition is more appropriate.

Keep timing, dimensions, assets and render configuration explicit.

Do not emulate HyperFrames-specific features that the available renderer cannot reproduce; mark them degraded.
