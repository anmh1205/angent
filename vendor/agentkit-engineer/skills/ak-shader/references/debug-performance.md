# Shader debugging and performance

Debug by isolating intermediate values as colors.

Watch for:
- division by near-zero;
- NaN/Inf;
- discontinuities;
- precision qualifiers;
- coordinate-space mismatch;
- excessive dynamic loops;
- repeated expensive noise samples;
- branch divergence on target GPU.

When performance matters, measure frame/GPU time rather than guessing from line count.
