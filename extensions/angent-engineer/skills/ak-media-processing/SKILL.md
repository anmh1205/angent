---
name: ak-media-processing
description: Convert and inspect audio/video/images with FFmpeg, ImageMagick and optional RMBG, preserving originals, deterministic batch behavior and format-aware QA.
license: MIT
metadata: {port: angent-fallback, mode: adapted}
---

# Media Processing — Portable Fallback

Stable Engineer 2.19.0 routes video/audio/transcoding/streaming to **FFmpeg**, image conversion/resizing/batches to **ImageMagick**, and optional AI background removal to **RMBG**. The distinction between tool choice, codec/container semantics and inspection matters more than remembering a single command.

Read `references/video-audio.md`, `references/images.md` and `references/batch-streaming.md` as the task requires.

## Preflight

Inspect actual source media: container and codecs, streams, duration, dimensions/frame rate/aspect/rotation, pixel/color profile, alpha, channel/sample rate and relevant subtitles/metadata. Define output target: format/codec, frame/audio quality, resize/crop policy, dimensions, bitrate, streaming segments or image transparency.

Verify installed FFmpeg/ImageMagick/RMBG binaries and their supported codecs/models. Do not install optional software without authority. Never overwrite original media unless the user explicitly requests destructive in-place replacement.

## Route and execute

- **FFmpeg**: stream copy only when compatible with target container and no transform is needed; otherwise select a correct codec/preset/quality/filter graph. Extraction, thumbnails, GIFs, HLS/DASH packaging and re-encoding have different validation needs.
- **ImageMagick**: distinguish aspect-preserving resize from fill/crop; check alpha/color, output metadata and batch file selection. `mogrify` can edit inputs in place; use new output paths by default.
- **RMBG**: requires actual model/CLI; evaluate edges/alpha and disclose model/provider requirements. Do not assume every supported image tool has AI background removal.
- **Batch**: bounded concurrency, deterministic filenames and per-file failures. Preserve a manifest when output volume makes verification difficult.

Choose project-owned destination paths using the actual file workflow, with no invented default. Inspect output using ffprobe/identify or suitable readers, then validate representative visual frames, audio synchronization, background edges and playback/seek. For HLS/DASH check segment existence, manifests, keyframe alignment and stream startup. A successful command exit **does not** prove perceptual quality.

Report verified files, codec/dimension metadata, requested transformations, destructive effects avoided, inspection evidence and remaining limitations. Use genuine image-generation tools for new illustrative art rather than media conversion commands.
