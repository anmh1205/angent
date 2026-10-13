# Three.js scene architecture

Separate:
- renderer/canvas lifecycle;
- scene graph creation;
- camera;
- asset loading;
- animation/update state;
- user input;
- physics/simulation when present;
- postprocessing;
- cleanup.

Avoid putting every responsibility in one animation-loop function.

Use a consistent coordinate/unit convention.

For React bindings or another framework, preserve the same ownership concepts while following framework lifecycle rules.
