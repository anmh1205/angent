---
name: ak-deep-swe
description: Evaluate an external coding model on DeepSWE through a verified Pier/OpenRouter benchmark harness with cost and reproducibility gates.
license: MIT
metadata: {port: angent-fallback, mode: degraded}
---

# DeepSWE — Portable Fallback

Stable Engineer 2.19.0 uses **DeepSWE + Pier + OpenRouter** to benchmark external coding-agent capability, not to optimize the local repository. The task corpus, runner, container images and paid provider are not bundled with this Markdown; no benchmark score is implied.

Read `references/benchmark-reproducibility.md` for version, evaluator and environment requirements.

## Prerequisite and authorization gate

Confirm uv, Git, Docker client **and working daemon**; installed/current Pier CLI; available DeepSWE task corpus and revisions; exact OpenRouter model slug; and presence of `OPENROUTER_API_KEY` without printing or recording its value. Stable source documents a 113-task corpus, but confirm the current run's real task count.

Cloning a repo, installing Pier, pulling images and consuming paid model tokens are external effects requiring appropriate user authority. Never copy keys into logs, commands, prompts or result files. Check `pier --help` and `pier run --help` before using flags; source examples may drift.

## Bounded execution and evidence

1. Run **one identified task first**, validate its agent/model mapping, container, evaluator and artifact output.
2. If justified and authorized, run a reproducible small subset with fixed task selection/sample seed, recorded environment, concurrency and budget.
3. Before a full corpus run, present task scope, command, expected cost exposure and stop criteria and require **explicit additional confirmation**.
4. Read actual Pier results (view/analyze/critique when supported). Report exact runner/evaluator and benchmark revisions, model identifier, completed/failed/skipped tasks, sampling method, scores, observed usage/cost, logs/artifacts and uncertainty.

On auth/model/flag mismatch, stop and inspect current help rather than blindly retrying or silently changing the model. Do not publish to a leaderboard without approval. Without compatible runner/provider, only provide a setup/blocker report or clearly **non-comparable** local checks; never invent benchmark results.

Use ak-loop instead for source-local numeric optimization.
