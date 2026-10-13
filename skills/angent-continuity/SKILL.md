---
name: angent-continuity
description: Persist interruption-tolerant ANGENT task state through durable verified checkpoints and safely reconcile ambiguous effects on resume.
---

# ANGENT Continuity — Durable Frontier

Continuity owns persistence, not task strategy.

For non-trivial tool work or long artifacts, establish a stable work key and authorized cross-session store from the first substantive step.

Before a consequential external effect, persist and read back a PREPARED record with target, intent, expected before/after state and reconciliation query. Afterward inspect the authoritative target and persist COMMITTED/VERIFIED or ATTEMPTED_UNKNOWN.

For read-only/research/authoring work, persist meaningful completed units rather than waiting for a predicted interruption.

On resume:
1. locate the highest coherent verified revision;
2. apply newest user instructions/authorization;
3. reconcile PREPARED or ATTEMPTED_UNKNOWN effects before replay;
4. restore the first unfinished dependency and validate saved artifact pointers.

A chat transcript, model memory or unsynced local scratch file is not a durable checkpoint. ANGENT cannot run after host Stop or guarantee zero token loss.
