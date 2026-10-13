---
name: ak-codex-goal
description: Guide a long-running goal with a verifiable stop condition; use Codex goal-mode features when available and portable Continuity semantics otherwise.
license: MIT
metadata: {port: angent-fallback, mode: adapted}
---

# Goal Mode — Portable Fallback

This Skill generalizes the useful semantics of long-running Codex goal work without requiring Codex.

## Goal contract

Define:
- durable objective;
- hard constraints;
- acceptance evidence;
- authorized effects;
- stop conditions;
- current frontier.

## Runtime selection

If the active harness exposes a native durable-goal mode, use it.

Otherwise implement the same semantics through ANGENT Continuity:
- proactive frontier persistence;
- dependency-aware next action;
- periodic endpoint verification;
- no stop merely because a status report was produced.

## Stop

Stop only at verified goal completion, a true blocker, required user decision, authority boundary or exhausted explicit budget.

Never reinterpret “autonomous goal” as permission for unauthorized external effects.
