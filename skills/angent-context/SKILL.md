---
name: angent-context
description: Reconstruct the minimum authoritative state needed for the present decision or continuation, without treating history as source truth or authority.
---

# ANGENT Context — State Reconstruction

Context is not a memory dump.

Reconstruct only the state needed now from four distinct layers:
- **user model**: durable preferences that materially affect the task;
- **project model**: architecture, conventions and standing project decisions;
- **task state**: verified frontier, unresolved decisions, pending/ambiguous effects;
- **conversation state**: temporary local context.

For resumed work, locate the durable Continuity stream and canonical provider state first. Historical summaries are hints, not final truth.

Return facts with provenance and uncertainty to Contract/Reasoning. Do not mutate, execute or infer permission from prior momentum.
