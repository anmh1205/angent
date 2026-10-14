---
name: ak-ai-artist
description: Generate or edit branded imagery using a real image backend, with explicit native Nano Banana prompt-pack mode and honest provider/asset limits.
metadata: {port: angent-fallback, mode: degraded}
---

# AI Artist — Portable Fallback

Stable Engineer 2.19.0 AI Artist is a workflow with **129 curated Nano Banana prompts**, a BM25-style catalog search, Python `search.py`/`generate.py` and a Google/OpenRouter-backed `ai-multimodal` rendering path. Those scripts, database and third-party model access are not supplied by this Markdown. General-purpose visual generation is a valuable substitute for the user-facing creative outcome, **not** evidence the original search/generator was run.

Read `references/creative-brief.md`, `references/iteration.md` and `references/visual-review.md`.

## Brief and native modes

Collect purpose, audience, medium/aspect ratio, brand constraints, required text and visual exclusions from the existing request. On the **native** workflow, the prompt-validation interview is required unless the user explicitly supplies `--skip`; do not re-ask already supplied decisions. Do not assume skipping the interview waives safety or actual output checks.

- `search` (default): retrieve best-ranked curated prompt from the **present and verified** 129-item catalog.
- `creative`: remix the top three retrieved prompts into a coherent concept.
- `wild`: deliberate unexpected visual direction while retaining user must-haves.
- `all`: create all three distinct directions, not three cosmetic duplicates.

Stable CLI `python3 scripts/generate.py "<concept>" -o <path> --mode search|creative|wild|all --provider auto|google|openrouter` and optional `--aspect-ratio`, `--model`, `--dry-run`, `--skip` are **examples only**; inspect existing scripts and help before executing. A provider choice can incur cost and transmit private inputs; require genuine backend access/authority, never reveal keys or assume provider auto routing.

## Portable outcome

When native catalog and scripts are absent, use the active authorized image-generation capability to achieve the requested creative output. Preserve exact shapes, logo proportions, specified copy and visual references where requested; for strict vector deliverables use a real editable-vector tool rather than a raster illustration. Discuss catalog-specific modes as unavailable, not simulated BM25 retrieval.

Inspect generated images for subject/object fidelity, text errors, framing, brand colors, legibility, artifacts and compliance with constraints. Iterate from observed defects rather than continuously replacing a previously accepted direction. Distinguish brief, generated visual, editable source, exported file and user acceptance; never claim export or stored artifact if only a rendered chat image exists.

**Capability:** VERIFIED_DEGRADED until the curated dataset/scripts/backend are actually available and exercised.
