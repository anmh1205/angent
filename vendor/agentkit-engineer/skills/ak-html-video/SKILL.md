---
name: ak-html-video
description: Create and verify local MP4 video from HTML/CSS/JS template projects using the available html-video/Chromium/ffmpeg toolchain, with explicit setup, preview and artifact validation.
license: Apache-2.0
metadata: {port: angent-fallback, mode: adapted, baseline: "AgentKit Engineer 2.19.0"}
---

# HTML Video — Portable Fallback

Use for HTML-first, template/project-driven video generation.

Use Remotion for React/Remotion compositions and frame-oriented project code. Use Media Processing for pure encode/trim/transcode/thumbnail/HLS work.

## Preflight

Resolve:
- audience/goal, duration and aspect ratio;
- source assets/content;
- desired template/project or whether one must be created;
- output path and draft/final quality expectation;
- local `html-video` availability or a compatible source checkout;
- Node/package-manager/browser/ffmpeg prerequisites;
- installation/network/process/file authority.

Prefer the installed/published tool. If a source checkout is required, keep it outside the user's project unless the user explicitly wants otherwise.

Run the tool's current diagnostics/help before relying on memorized command flags.

## Workflow

1. Pin the brief and output contract.
2. Discover candidate templates and inspect their actual configurable inputs.
3. Create or locate the video project.
4. Attach assets/content and set only variables the selected template supports.
5. Preview the project before final rendering.
6. Use the available Studio/editor route when the template requires interactive layout/copy adjustment.
7. Render to an explicit output path.
8. Verify the final media artifact using `ffprobe` or an equivalent media inspector: non-zero duration, expected dimensions/stream(s), and no obvious blank/clipped/font/timing failure.
9. Preserve the exact tool/version/config/command needed to reproduce the result when reproducibility matters.

## Artifact organization

Follow the target repository's existing artifact conventions.

Keep disposable preview/render scratch separate from finished deliverables.

Do not commit large MP4 outputs merely because a render succeeded.

## Failure handling

If the expected renderer/browser/ffmpeg dependency is missing, report the missing capability and the smallest supported setup route.

Do not silently replace a template-driven html-video task with a different video technology when the distinction matters to the user.

## Completion

CLI exit success is not video acceptance.

The final claim requires inspection of the produced artifact and, when visual fidelity matters, representative playback/frame review.
