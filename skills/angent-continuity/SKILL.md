---
name: angent-continuity
description: Persist interruption-tolerant ANGENT task state through durable verified checkpoints and safely reconcile ambiguous effects on resume.
---

# ANGENT Continuity — Durable Frontier

Continuity owns persistence, not task strategy.

Read `continuity-protocol.md`.

For non-trivial tool work or long artifacts, establish a stable work key and authorized cross-session store from the first substantive step.

Before a consequential external effect, persist/read back PREPARED intent with target, expected before/after state and reconciliation query. Afterward inspect the authoritative target and persist COMMITTED/VERIFIED or ATTEMPTED_UNKNOWN.

For research/read-only/authoring work, persist meaningful completed units and durable artifact pointers rather than waiting for a predicted interruption.

On resume:
1. recover the highest coherent verified record;
2. apply newest instructions and current authorization;
3. reconcile ambiguous effects before replay;
4. validate saved artifacts;
5. return the recovered frontier to Context/Reasoning for current-state reconstruction.

A chat transcript, model memory or unsynced scratch file is not durable persistence. ANGENT cannot run after host Stop or guarantee zero token loss.
