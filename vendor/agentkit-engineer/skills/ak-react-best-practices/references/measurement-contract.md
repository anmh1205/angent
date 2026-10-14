# React performance measurement contract

A performance claim needs a comparable workload and environment.

Record only what is material:
- route/component/user interaction;
- build mode and relevant framework/runtime versions;
- representative dataset/content;
- cache state;
- browser/device or server environment;
- timing/bundle/render/network/profiler metric used;
- behavioral tests that protect correctness.

## Before/after

Use the same scenario and measurement method before and after the change.

If results are noisy, stabilize the dataset/build/network/cache state or run enough representative observations to distinguish the effect; do not choose a fixed repetition count by habit.

## Finding quality

For each material recommendation state:
- observed evidence;
- compatible rule/pattern;
- expected impact;
- behavior risk;
- verification method.

A bundled guideline identifies a candidate pattern. It does not prove the project has the problem or that the same gain will occur.

## Regression boundary

Performance improvement does not compensate for regressions in:
- data freshness/correctness;
- error/fallback behavior;
- accessibility;
- hydration/SSR behavior;
- privacy/tenant isolation;
- offline/loading behavior;
- bundle/runtime compatibility.
