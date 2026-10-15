# Remotion timeline, assets and output QA

Stable Engineer 2.19.0 Remotion's extended rule set covers compositions/stills, animations, transitions, sequences, dynamically calculated metadata, audio, video, captions, asset loading, fonts, GIFs/images, charts, 3D and media extraction.

**Deterministic time:** `frame = round(seconds * fps)` with an explicit rounding policy and stable frame rate. Check sequence start/end boundaries, transitions and overlay z-order. In a frame-evaluated renderer, avoid `Date.now`, timers, nondeterministic random seeds or side effects that depend on live wall time.

**Composition contract:** composition ID, dimensions, FPS, durationInFrames, defaultProps, optional calculated metadata and codec/export policy. Prop changes should not silently cause assets or audio to overrun the duration.

**Media:** verify font loading, image/video decode, transparent backgrounds, audio start/end/volume, caption segment alignment and remote media authorization. A successful React render of one frame does not prove the video is playable.

**Acceptance:** inspect selected frame outputs, title/caption legibility and longest text; check generated video metadata and actual playback start, transitions and end. Label missing renderer or unsupported decoder as a blocking runtime capability rather than asserting an MP4 exists.
