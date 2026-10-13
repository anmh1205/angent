---
name: ak-media-processing
description: Process image, audio and video with deterministic media tooling, explicit quality targets and reproducible verification.
license: MIT
metadata: {port: angent-fallback, mode: portable}
---

# Media Processing — Portable Fallback

Use for conversion, trimming, encoding, compositing, thumbnails, filters, streaming outputs and batch media work.

## Load progressively

- `references/video-audio.md` — codecs, containers, timing and audio/video transformations.
- `references/images.md` — image conversion, resizing, compositing and quality.
- `references/batch-streaming.md` — bulk processing and HLS/DASH-style outputs.

## Workflow

1. Inspect source metadata before transforming.
2. Define the target artifact precisely: dimensions, container/codec, bitrate/quality, channels/sample rate, frame rate, alpha/color needs.
3. Prefer stream-copy/lossless operations when re-encoding is unnecessary.
4. Use installed deterministic tools such as FFmpeg/ImageMagick when available.
5. Preserve originals unless destructive replacement is explicitly requested.
6. Verify output metadata and inspect representative content.
7. For batch jobs, sample several outputs and report failures rather than assuming uniform success.

Do not guess tool support or codec compatibility; inspect the installed toolchain.
