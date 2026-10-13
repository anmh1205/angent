---
name: ak-deep-swe
description: Run or evaluate DeepSWE coding-agent benchmarks through the current official/compatible runner and model provider with explicit cost, prerequisites and reproducibility.
license: MIT
metadata: {port: angent-fallback, mode: degraded}
---

# DeepSWE Benchmark — Portable Fallback

Read `references/benchmark-reproducibility.md`.

This Skill is for external coding-agent benchmarking, not repository-local optimization.

## Preflight

Before spending model/runtime resources:

1. identify the current DeepSWE task set/version;
2. identify the supported runner and its installed/current version;
3. verify required local prerequisites such as Git/container runtime;
4. verify provider authentication without printing credentials;
5. resolve the exact model identifier from the provider;
6. estimate the requested run size/cost exposure when possible.

Do not hard-code old Pier/OpenRouter flags; inspect current help/docs.

## Run safely

1. run one representative task first;
2. verify the runner, model mapping, artifact path and evaluator work;
3. run a small deterministic subset when broader confidence is needed;
4. require explicit user authorization before a materially costly full-corpus run;
5. preserve raw job/evaluator artifacts.

## Report

Record:
- benchmark/task-set version;
- runner/evaluator version;
- model/provider identifier;
- task count and sampling method;
- runtime/environment;
- score/reward;
- failed/skipped tasks;
- usage/cost when reliably available;
- artifact pointers.

## Degraded path

If the official/compatible harness/provider is unavailable, do not invent or estimate a benchmark score.

Provide the missing prerequisite/setup path and optionally define local smoke tasks clearly labeled **non-comparable**.

Do not submit leaderboard results or publish benchmark artifacts unless requested.
