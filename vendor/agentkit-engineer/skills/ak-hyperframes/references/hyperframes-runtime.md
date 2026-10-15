# HyperFrames renderer decision and QA

Pinned Engineer stable 2.19.0 uses HeyGen HyperFrames around version 0.7.99. Check actual package/runtime help before copying syntax or installing anything.

**Native sequence:** version/installed CLI preflight → scaffold → HTML with matching timeline attributes (data-composition-id, data-start, data-width, data-height) → local preview → native lint → local MP4 render → media metadata and frames/playback check.

For timing, decide frame rate, duration, scene/transition boundaries, simultaneous layers and event-triggered animation. Confirm the source tool's rules rather than treating CSS animation length as exported video duration. Export success requires an actual file, correct duration, dimensions/audio behavior and at least representative viewed frames.

**Cloud render:** only if user authorizes a provider upload, API credential/budget and output destination. The cloud subcommand is a distinct top-level workflow, not a toggle on the local renderer.

**Fallback:** HTML/JS animation plus verified browser/media tooling or Remotion can meet some deliverables but may change timing APIs and preview semantics. Disclose the substituted backend and missing capabilities.
