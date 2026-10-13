---
name: angent-execution
description: Execute authorized actions from an explicit ANGENT plan, observe real effects, reconcile ambiguity and return evidence for reasoning and verification.
---

# ANGENT Execution — Actuator and Observer

Execution owns tool selection, dependency-respecting action, retries, mutation safety, observation and provider reconciliation.

It does not own strategic reasoning after evidence invalidates the plan.

Read `adaptive-planning.md`. Use Continuity according to `continuity-protocol.md`.

## Before action

Require enough state to act safely:
- authorized target/operation;
- precondition/dependency;
- expected result/observation;
- replan/stop condition;
- verification target.

For consequential external effects, Continuity must persist a PREPARED record before the effect.

## Execute

Prefer actions that advance the current frontier. Respect user-requested tool boundaries and defer expensive tests when explicitly requested, while preserving later verification.

Do not blindly replay a timed-out or response-lost external write.

## Observe

After an effect, inspect authoritative state when the result matters. Return an **observation delta**:
- attempted action;
- actual observed state;
- changed identifiers/versions;
- mismatch with expectation;
- residual uncertainty.

If the observation contradicts a plan assumption, return to Reasoning before dependent stale steps.

## Completion

A command exit, commit, issue transition, generated artifact or progress report is only intermediate evidence unless the Contract defines it as the endpoint.

Continue while an authorized next step remains runnable. Stop only at verified completion, genuine blocker, required user decision, authorization/safety boundary or unavailable capability.
