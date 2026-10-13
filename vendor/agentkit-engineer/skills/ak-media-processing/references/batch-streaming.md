# Batch and streaming media

## Batch

Use a deterministic file selection rule and predictable output naming.

Record per-file failure instead of terminating silently halfway.

Consider concurrency only when I/O/CPU/memory limits are understood.

## Streaming outputs

For segmented streaming:
- choose segment duration/keyframe alignment;
- verify manifests reference existing segments;
- keep bitrate ladders coherent;
- test actual playback/startup/seek behavior.

Do not infer stream health from manifest generation alone.
