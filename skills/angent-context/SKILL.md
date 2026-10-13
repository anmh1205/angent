---
name: angent-context
description: Reconstruct only the authoritative prior state needed for the current decision or continuation, without treating history as source truth or permission.
---

# ANGENT Context — State Reconstruction

Context is not a history dump.

Reconstruct the minimum relevant state from distinct layers:
- **user model** — durable preferences that materially affect the task;
- **project model** — architecture, conventions and standing decisions;
- **task state** — verified frontier, unresolved decisions, saved artifacts and ambiguous effects;
- **conversation state** — temporary local context.

For continuation, prefer:
1. verified Continuity frontier;
2. live canonical provider/artifact state;
3. prior project records;
4. conversation/history summaries as hints.

Return facts with provenance and uncertainty. When sources conflict, preserve the conflict for Reasoning instead of choosing by recency alone.

Context does not mutate, execute or infer authorization from historical momentum.
