---
name: ak-context-engineering
description: Diagnose context pressure, memory boundaries and degradation using measured host signals, scoped retrieval, compaction and behavioral evaluation.
metadata: {port: angent-fallback, mode: adapted}
---

# Context Engineering — Portable Fallback

Use for agent context design, token or quota questions, lost context, multi-agent handoffs and memory architectures. Distinguish context correctness, token cost, and provider quota; each requires different evidence.

## Evidence and runtime awareness

1. Identify the concrete decision or failure: stale frontier, retrieval miss, context poisoning, incomplete tool data, instruction conflict, or measured pressure.
2. Inspect actual host-provided usage and truncation signals, saved task revisions, retrieval scope and representative failures.
3. Never invent remaining tokens, model-window percentage, cache hits, reset time, usage API access or cost multipliers. Upstream Claude Code PostToolUse hooks, statusline files and Anthropic OAuth endpoints are not portable runtime telemetry.
4. Mark measured, inferred and unavailable evidence separately. Fixed 70/80/90 percent thresholds in upstream examples are heuristics, not universal policy.

## Four-bucket lifecycle

- **Write:** stable project instruction in canonical AGENTS.md; active frontier/effect identity in Continuity; durable knowledge in its owned store.
- **Select:** use only high-signal context that can change the current action.
- **Compress:** preserve accepted outcome, verified units, first unfinished unit, decisions and their basis, operation IDs, unresolved effects and evidence pointers. Do not collapse verified and pending work.
- **Isolate:** partition genuinely independent specialist contexts; provide complete handoff evidence, and do not pretend the harness has subagent support.
- **Evaluate:** compare representative task correctness, stale-resume behavior, retrieval omissions and context cost before and after changes.

## Progressive references

- `references/context-lifecycle.md` — instruction, task state and history.
- `references/retrieval-memory.md` — memory ownership and retrieval.
- `references/compaction-isolation.md` — compaction and specialist boundaries.
- `references/context-degradation.md` — failure modes.
- `references/tool-context.md` — tool descriptions and payload quality.
- `references/context-evaluation.md` — behavioral tests.

Optimize decision quality per unit of context. Compression that loses a dependency or mutation identity is a regression.
