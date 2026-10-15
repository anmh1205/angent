---
name: ak-debug
description: Diagnose software failures by proving the causal root cause before changing code, then verify the original symptom and relevant blast radius with fresh evidence.
license: MIT
metadata:
  author: ANGENT fallback
  port: angent-fallback
  mode: adapted
  inspired-by: AgentKit Engineer ak-debug
---

# Debug — Portable Fallback

Debugging is an evidence workflow, not a quick-fix workflow.

The objective is to establish **why the failure occurs**, change the earliest correct owner, and verify the original path after the fix.

This Skill does not require AgentKit CLI, Claude-specific subagents, or any particular browser/debugger integration.

## Load references progressively

- `references/causal-diagnosis.md` — build hypotheses and trace invalid state to its source.
- `references/investigation-workflow.md` — multi-step/system incidents, logs, CI, performance, and coordination.
- `references/verification.md` — prove the original symptom is fixed without overclaiming.
- `references/frontend-runtime-verification.md` — visual/runtime verification using whatever browser capability actually exists.

## Start from the failure, not from the suspected fix

Capture the failing state first:
- exact symptom;
- expected behavior;
- reproduction path;
- environment/version;
- relevant logs/test output;
- whether the failure is deterministic, intermittent, data-dependent, or environment-dependent.

If the failure cannot be reproduced, identify the strongest available observation boundary before editing code.

## Build the smallest causal model

Trace:

```text
input / trigger
   ↓
state transition
   ↓
owner / interface
   ↓
first divergence from expectation
   ↓
visible failure
```

Do not stop at the first suspicious line.

A stack trace location may be where invalid state becomes visible, not where it originated.

## Keep competing hypotheses when needed

When multiple mechanisms remain plausible and they imply different fixes:
1. state the live hypotheses;
2. identify the observation each predicts;
3. choose the cheapest discriminating probe;
4. update the model from evidence.

Do not enumerate possibilities endlessly when one mechanism is already established well enough for the consequence level.

## Use scouting deliberately

If code ownership or flow is unclear, use the available Scout capability before diagnosis.

Scout is for locating and tracing. Debug remains responsible for the causal explanation.

Do not hard-require a particular invocation syntax.

## Fix only after root cause is established enough

Prefer the smallest change that addresses the actual mechanism.

Avoid:
- suppressing an error while preserving corrupt state;
- adding retries around a deterministic defect;
- validating only at the final consumer when the producer owns the invariant;
- broad refactors that are not needed to fix the established cause.

When a broader design change is genuinely necessary, return the evidence to ANGENT Reasoning before turning diagnosis into architecture work.

## Long investigations

For multi-step incidents, use ANGENT Continuity to preserve:
- current hypotheses;
- evidence already gathered;
- rejected explanations;
- experiments/attempts;
- current frontier;
- unresolved blockers.

Do not rely on a transient chat summary or a runtime-specific task list as the only record.

## Parallel evidence collection

Use delegated workers only when evidence sources are independent enough to benefit from separation, such as:
- CI logs vs application logs;
- frontend vs backend traces;
- two independent subsystems;
- performance profiling vs code path analysis.

Join evidence before claiming a root cause.

If the harness has no delegation capability, continue sequentially.

## Output

A useful diagnostic result includes:
- reproduced/observed symptom;
- established root cause or remaining hypotheses;
- decisive evidence;
- affected owner/boundary;
- proposed fix direction;
- verification needed after the change;
- residual uncertainty.

If the user asked for a fix, hand the established diagnosis to the appropriate execution path rather than hiding uncertainty behind code changes.

## Quality gates

Do not claim the bug is fixed unless fresh verification exercises the original failure path or an equally strong acceptance path.

Do not claim a root cause merely because a code change made one test green if another plausible mechanism remains unexamined.

Do not stop after a failed attempt if there is still a safe, runnable diagnostic step.
