---
name: angent-execution
description: Execute authorized actions from an explicit ANGENT plan, observe real effects, reconcile ambiguity and return evidence for reasoning and verification.
---

# ANGENT Execution — Actuator and Observer

Execution owns tool selection, dependency-respecting action, retries, mutation safety, observation and provider reconciliation.

It does **not** own strategic reasoning when new evidence invalidates the plan.

## Before action

Receive or reconstruct:
- authorized target and operation;
- dependency/precondition;
- expected observation/result;
- replan/stop condition;
- verification target.

Use Continuity before consequential effects.

## After action

Read the authoritative provider when outcome matters. Return:
- what was attempted;
- observed result/evidence;
- changed identifiers/versions;
- mismatch with expectation;
- residual uncertainty.

If an observation contradicts a plan assumption, return to Reasoning before executing dependent stale steps.

## Completion

A command exit, commit, issue transition or progress message is not automatically the requested endpoint. Continue while an authorized next step remains runnable; stop only at verified completion, genuine blocker, required decision, authorization/safety boundary or unavailable capability.
