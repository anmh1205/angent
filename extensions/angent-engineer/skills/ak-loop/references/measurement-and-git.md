# Loop measurement, guard and Git memory

The stable Engineer 2.19.0 loop uses an 8-stage sequence: preflight, review, ideate, modify, commit, verify, guard/decide, log and repeat. Apply it only after verifying the active host's Git authority and clean workspace.

## Measurement contract

- Baseline metric: finite numeric value with explicit unit and direction.
- Repeatability: fixed input data, load level, random seed, warm/cold cache policy, toolchain and environment as relevant.
- Guard: different question from Verify. Verify checks the optimized metric; Guard asserts other required behavior still works. A missing or failing baseline guard blocks the experiment.
- Noise: deterministic counts can be measured once; variable timings need repeated comparable runs. Median or a confidence-aware method is preferable for noisy metrics; do not accept microscopic improvements inside normal variance.
- Min-Delta: meaningful threshold in the metric's actual units; for lower-is-better, improvement = previous_metric - new_metric.
- Failures: command error, timeout, nonnumeric output, metric discontinuity or changed benchmark input does **not** count as improvement.

## Git/branch contract

Upstream advises a clean Git tree, atomic commit **before** verification, then Git revert for rejected candidates, preserving experimental history. That is appropriate only on an authorized isolated experiment branch. Do not use reset --hard or force push to discard anything when another user/worker could have contributed to the branch; do not assume a revert always succeeds without conflicts.

A safe experimental branch or worktree is preferred over using the current shared checkout. One hypothesis per commit enables attribution. Keep the log append-only, make accepted candidate SHA explicit, and inspect the HEAD/ref before a remote update. Rejected trials must be distinguishable from accepted results; do not falsely call them 'never changed'.

## Guard and command safety

Treat Verify/Guard as executable actions, not neutral strings. Screen for destructive file operations, privileged commands, arbitrary installer/download pipelines, credential interpolation, production data, unauthorized HTTP writes and cost-amplifying repeated calls. Never weaken or modify the guard to win the metric. Redact tokens and sensitive values from logs, commands, sample outputs and reports.

## Example decision table

| Observation | Decision |
|---|---|
| Directional improvement exceeds Min-Delta; guard passes; comparable measurement | Keep candidate |
| Metric regresses or stays within noise; guard passes | Discard or mark inconclusive |
| Guard fails (including crash) | Reject and diagnose |
| Verify crashes or emits no valid number | Invalid measurement; recover safely |
| Many consecutive discards | Revisit hypothesis/scope; stop when saturation persists |
| User interrupts or branch/ownership changes | Stop; preserve truthful frontier |

Never claim performance, code quality, robustness or true outcome improvements from a proxy alone.
