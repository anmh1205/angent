# Three.js corpus, renderer and verification gates

Stable Engineer 2.19.0 advertises 556 searchable examples across webgl, webgpu, webxr, physics and advanced effects, plus an API/class index and use-case templates.

- **Native corpus:** Search using the actual installed `scripts/search.py`, domain `examples`, `api`, `use-cases` or `categories`. Preserve source/version/match identity; don't manufacture hits. The fallback does not include the catalog by implication.
- **Version:** record Three.js revision and browser rendering backend (WebGL1/2/WebGPU), platform capabilities, color management changes and asset loading formats.
- **Scene:** define ownership for scene/camera/renderer, asset loaders, animation frame loop, event handlers, resize and disposal.
- **Visual QA:** examine actual canvas frames, pick/camera behavior, material/light/color, asset orientation and empty/error UI.
- **Runtime QA:** monitor frame-time, draw calls, GPU allocations/leaks, context loss/recovery, and fallback behavior when API/GPU features are unavailable.

A passing TypeScript compiler cannot establish 3D visual correctness or GPU resource hygiene. A search corpus without the installed search tool is a knowledge source, not an executed capability.
