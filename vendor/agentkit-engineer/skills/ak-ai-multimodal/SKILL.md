---
name: ak-ai-multimodal
description: Analyze or generate image, audio, video and document content through the strongest multimodal tools available in the active harness.
license: MIT
metadata: {port: angent-fallback, mode: adapted}
---

# AI Multimodal — Portable Fallback

## Load progressively

- `references/modality-routing.md` — choose the correct modality/tool.
- `references/evidence-quality.md` — bind observations to page/frame/file evidence.

## Workflow

1. Identify the requested modality operation.
2. Prefer native structured access/vision before conversion/OCR.
3. Select a tool that actually supports the input/output.
4. Preserve source identity/page/frame/timestamp.
5. Generate/transform only when requested.
6. Verify output or uncertainty.

Do not route every modality through one external CLI when the harness already has a better native capability.
