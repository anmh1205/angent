---
name: ak-loop
description: Run a bounded experimental optimization loop against a mechanical metric, keeping or reverting each iteration based on evidence.
metadata: {port: angent-fallback, mode: adapted}
---

# Loop — Portable Fallback

Use when the target can be measured repeatedly: coverage, benchmark latency, bundle size, memory usage, lint count or another mechanical metric.

## Contract

Require:
- metric and measurement command;
- target or stop threshold;
- allowed change surface;
- iteration/budget limit;
- baseline;
- revert method.

## Iteration

1. Measure baseline/current state.
2. Choose one hypothesis/change.
3. Apply the smallest experiment.
4. Measure with the same method.
5. Keep only if it improves the objective without breaking constraints.
6. Otherwise revert cleanly.
7. Record result and next hypothesis.

Stop at target, saturation, budget, invalid metric, or decision-required condition.

Do not optimize a proxy that harms the real product objective.
