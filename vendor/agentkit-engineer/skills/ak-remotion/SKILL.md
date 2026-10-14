---
name: ak-remotion
description: Create and validate React/Remotion programmatic videos with frame-exact timeline, asset lifecycle and real render evidence.
metadata: {port: angent-fallback, mode: degraded}
---

# Remotion — Portable Fallback

Use for code-defined videos where React composition, data-driven motion, captions, charts and reusable components matter. Stable Engineer 2.19.0 imports a detailed **33-rule Remotion reference package** covering timing, compositions, fonts/assets, audio/video, transitions, captions, charts, metadata, 3D, decoding and render techniques. This fallback retains the workflow and important rules but does **not** claim those 33 original reference files are installed.

Read `references/timeline-and-qa.md` for frame/effects discipline. Check the project's **installed Remotion version**, React runtime and actual official/current API before writing components or assuming a helper exists.

## Scene/composition and media model

Define `Composition` identity, width/height, fps, durationInFrames and deterministic props; use dynamic metadata only when the result remains predictable and validated. Set sequence start/duration/overlap using **integer frames**, not loosely mixing seconds and frame indices. Keep timeline dependency order, transitions, audio alignment, overlays and subtitles consistent across framerates.

Use `useCurrentFrame`/`useVideoConfig` and appropriate interpolation/spring mechanics for frame-deterministic animation; do not rely on wall-clock timers, uncontrolled randomness, CSS animations whose browser-time behavior diverges from renders, or asynchronous side effects without a loading gate.

For image/video/audio assets, verify URLs/local availability, codec/decode support, loading timing, crop/aspect fit, font license/embedding, asset readiness, caption timing and color/alpha handling. For browser-based media metadata or frame extraction, use only APIs supplied by the installed release (upstream references may mention Mediabunny and related utilities).

## Implementation/QA

1. Build minimal reproducible composition, confirm props and frame budget.
2. Load and render representative key frames at beginning, transitions and end; inspect text clipping, cropped assets, typography, state and motion smoothness.
3. Review worst-case datasets and longest localized strings, video/audio delay, missing assets and concurrency/resource footprint.
4. Run actual Remotion/React type/build and composition checks. Produce video/stills through the available verified renderer; inspect media metadata, duration, frame size, frame sampling, audio sync and platform playback.
5. Distinguish authored React code, successful preview and generated video artifact. Export errors, codec/runtime omissions or unfinished assets must remain visible in the report.

Use HyperFrames for explicitly requested HTML-first/HeyGen work. Native Remotion package/reference and renderer availability cannot be inferred from this skill file.

**Capability:** VERIFIED_DEGRADED until rule corpus plus renderer and representative media-output tests are available.
