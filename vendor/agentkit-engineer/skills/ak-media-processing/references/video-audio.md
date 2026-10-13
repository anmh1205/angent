# Video and audio processing

## Video

Track:
- container vs codec;
- dimensions/aspect ratio;
- frame rate/time base;
- pixel format/color space;
- bitrate/quality mode;
- keyframe/GOP needs;
- subtitle/audio stream mapping.

Avoid unnecessary generation loss.

## Audio

Track:
- codec;
- sample rate;
- channel layout;
- loudness/normalization target;
- trim/fade timing.

## Verification

Inspect duration, stream list, dimensions, frame rate, audio channels and a representative playback segment.

A successful encoder exit does not prove sync, clipping or visual correctness.
