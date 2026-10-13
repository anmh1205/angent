# Assets and lifecycle

For models/textures/audio:
- use explicit loading/error state;
- handle color-space/encoding correctly for the active version;
- keep cache/reuse policy intentional;
- bound texture resolution;
- dispose geometries/materials/textures/render targets when no longer owned;
- avoid duplicate loaders/resources after navigation/hot reload.

Verify model scale/orientation and animation clip names rather than assuming exporter conventions.
