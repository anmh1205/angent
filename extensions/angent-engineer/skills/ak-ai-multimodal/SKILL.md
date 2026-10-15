---
name: ak-ai-multimodal
description: Safely analyze/generate image, video, audio and documents using available host modalities or exact-pinned Multix when installed, preserving backend limits and source evidence.
license: MIT
metadata: {port: angent-fallback, mode: degraded}
---

# AI Multimodal — Portable Fallback

Stable Engineer 2.19.0 routes vision, image generation/editing, video/audio/music analysis or synthesis and document understanding through the **exact-pinned `@mrgoonie/multix@0.2.0`** CLI and multiple provider catalogs. Do not silently substitute a floating `multix` install or assume that a host image generator also supports video, OCR, music or speech.

Read `references/modality-routing.md`, `references/evidence-quality.md` and `references/backend-boundaries.md`.

## Tool and model selection

1. Identify operation and input/output: image analysis/edit/generation; video analysis/generation; transcription/speech/music; structured document extraction or another exact modality.
2. Prefer structured document/text access over lossy OCR. Preserve page/frame/time/source pointers for analyses and distinguish directly observed content from model inferences.
3. Detect **actually available** native multimodal capabilities before reaching for an external provider. Host-native image, video, audio and file tools may be independent and have different limitations.
4. For the native stable CLI, check Node version (source requires Node 20+), pinned package presence and help. Use `npx -y -p @mrgoonie/multix@0.2.0 multix --version` only when package installation/network execution is authorized; the command may download code.
5. Consult real provider model catalog and current pricing/controls, choose an explicit model supporting the required modality, resolution, duration and format, and record version for reproducible results. Provider routing may include Google, OpenRouter and MiniMax; no credentials are assumed.
6. Before transmitting user-supplied media or voice, assess privacy, consent and service cost. Read only key **presence**; never print, persist or pass secret values into untrusted prompts.

## Execute and validate

Use actual backend inputs/help, bounded resource limits, transparent errors and predictable output paths. On failure identify the stage (model unsupported, credentials, file format/size, provider quota, timeout, export) and preserve useful error context without leaking secrets. Check actual exported artifact integrity, duration, frame/sample/codec properties or generated image dimensions; visually/audibly inspect representative output where possible.

An analysis response must identify the material it could see (page/frame/timestamp) and confidence limits. Generation must not assert ownership of a downloadable file unless its path is verified. Don't force provider-backed OCR when built-in vision or structured PDF/doc parsing is better.

**Capability:** VERIFIED_DEGRADED where exact Multix CLI/model provider or requested modality isn't present; report missing backend separately from analytical content.
