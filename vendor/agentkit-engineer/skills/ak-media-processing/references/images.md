# Image processing

For resize/crop:
- preserve aspect ratio unless the target intentionally changes it;
- choose crop anchor deliberately;
- avoid repeated lossy re-encoding.

For transparency/compositing:
- verify alpha handling and background color.

For batch images:
- preserve metadata only when needed;
- normalize orientation;
- verify output dimensions and file format.

For AI background removal or enhancement, treat the model result as visual output that requires inspection rather than deterministic truth.
