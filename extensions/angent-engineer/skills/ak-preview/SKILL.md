---
name: ak-preview
description: Inspect existing files or create Markdown/HTML visual explanations, diagrams, slide decks, diffs, plan reviews and recaps with verified rendering.
metadata: {port: angent-fallback, mode: degraded}
---

# Preview — Portable Fallback

Stable Engineer 2.19.0 Preview has two different contracts: **View** an already-existing file/directory without rebuilding it, or **Generate** a visual explanation/presentation artifact. The native package contains HTML templates, design references and mode-specific generation rules; an inert fallback Markdown file does not automatically supply that renderer.

Read `references/preview-routing.md` and `references/preview-modes.md`.

## Argument and intent routing

- Existing path or no generation flag → view the natural artifact through a real viewer; no new deck or diagram is implied.
- `--explain <topic>` → source-grounded illustrated technical explanation.
- `--diagram <topic>` → architecture/process visualization with accurate edges.
- `--slides <topic>` → coherent slide presentation.
- `--ascii` → terminal-friendly diagram (only when user explicitly wants text format).
- `--html --explain|--diagram|--slides` → self-contained HTML artifact with purpose-specific layout, theme switching and file/browser review.
- `--html --diff` → readable Git/source changes with observed baseline/reference.
- `--html --plan-review` → plan requirements against actual source/acceptance evidence.
- `--html --recap` → bounded real project state/history, not a fabricated summary.

If a path/name is ambiguous, resolve the actual resource before creating a competing artifact. For each mode, enforce its essential inputs (Git ref/diff, actual plan, source topic); do not treat an error as permission to manufacture input files.

## Creation and visual review

Select destination mode and target renderer first; author from source facts and intended reader. For HTML output prefer portable self-contained CSS/JS without untrusted remote scripts, use accessible light/dark/system controls when supported, responsive layouts and a usable reading order. Preserve editability or attached sources as requested. A source diagram can have correct syntax and still fail visual acceptance through overlap, clipping or false topology.

Render/read back at representative viewports/slide sizes. Validate fonts, links, navigation, text overflow, diagrams, zoom and tables. Fix actual defects. Do not claim an image, HTML file or running preview server until a real runtime verified it.

## Process and write boundary

Native Preview may start/stop local servers and writes outputs under an active plan's visuals directory; a portable host needs an actual authorized destination. Never overwrite an existing file by implicit mode inference or assume a background process/port has been created. Use a real file viewer for read-only requests, and generated output only when that medium was requested.

**Capability:** VERIFIED_DEGRADED without the pinned HTML templates/viewer runtime, even though another host renderer may satisfy a particular preview task.
