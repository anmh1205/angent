# Three.js performance

Measure before optimizing.

Inspect:
- draw calls;
- triangle/vertex count;
- material/shader count;
- texture memory/resolution;
- render targets/postprocessing;
- object count and scene traversal;
- animation/update CPU cost;
- garbage/allocation churn;
- device pixel ratio;
- asset load/decode time.

Possible techniques:
- instancing;
- geometry/material reuse;
- LOD;
- culling;
- lower DPR/resolution;
- texture compression;
- batching;
- reduced postprocessing.

Choose based on the measured bottleneck.
