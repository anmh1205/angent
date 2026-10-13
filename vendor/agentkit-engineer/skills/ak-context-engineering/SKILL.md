---
name: ak-context-engineering
description: Design high-signal agent context using AGENTS.md, scoped memory, retrieval, compaction, isolation and evaluation instead of loading all available history.
metadata: {port: angent-fallback, mode: adapted}
---

# Context Engineering — Portable Fallback

## Load progressively

- `references/context-lifecycle.md` — stable instruction, active work and historical evidence.
- `references/retrieval-memory.md` — scoped memory selection/synthesis.
- `references/compaction-isolation.md` — compaction and specialist isolation.
- `references/context-degradation.md` — diagnose why context is harming performance.
- `references/tool-context.md` — tool/Skill descriptions as part of context design.
- `references/context-evaluation.md` — evaluate context changes behaviorally.

## Core moves

- **Write** stable project instruction into AGENTS.md.
- **Select** context that can change the current decision.
- **Retrieve** detail just in time.
- **Compress** active state into a frontier/memory summary with pointers.
- **Isolate** independent specialist work.
- **Synthesize** memory updates instead of appending forever.
- **Evaluate** context changes against representative tasks.

Do not use fixed token-percentage thresholds as universal laws.

The objective is decision quality per unit of context, not maximum compression.
