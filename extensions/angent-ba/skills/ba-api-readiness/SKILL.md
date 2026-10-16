---
name: ba-api-readiness
description: Business analysis api-readiness specialist.
---

# ANGENT BA: api-readiness

Maintained adaptation from MIT Dev BA Kit (copyright 2026 Edward Ngo): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/api-readiness/SKILL.md

## Portability and authority

Use domain-specific steps below as methodology, not as authority or proof of tool execution. Original Claude-specific scripts, hooks, subagents, filesystem paths and approval levels are illustrative until verified in the current environment. ANGENT Root owns intent and routing; Execution owns writes and read-back; Quality verifies outcomes. Honor project naming and do not invent decisions. Use the real BA Markdown validator only for completed documents and report the result. For HTML/prototype/API use the actual browser, contract runner or test tool when authorized; generating source is not equivalent to successful execution. Other original Claude-only helper script names describe possible implementations, not installed ANGENT commands.


# /api-readiness — Go-live gate (API chain [6])

## Goal

Produce the go-live gate for the integration — cutover sequence, feature flags (kill switch), monitoring + runbook, rollback, SLA/deprecation, and a go/no-go table that hard-refuses "go" if `/api-test` results are absent. **Single output**: `docs/{feature}/integration/api-readiness.md` (type `api-readiness`).

## Constraints

- **Step [6], the gate** (`api-integration.md`): reads the whole chain — summary, design, map, checklist, **tests**. `api-tests.md` missing → **hard-refuse "go"** (can't enable what you haven't proven works); still write the readiness doc with status `blocked`.
- **Go/no-go is evidence-based** — the table's "go" requires: tests present + monitoring defined + rollback defined + flags named. A "go" with any of these absent is BLOCKING.
- **Five mandatory concerns** — cutover (enablement sequence + who flips what), feature flags (kill switch name + owner + off-state = degraded UX), monitoring (alerts: error rate/latency/their-status-page + runbook link), rollback (disable sequence + partial-data back-out), SLA/deprecation (their SLA we depend on + sunset date + our deprecation notice).
- **No fabrication** — flag names, alert thresholds, SLA figures cite the design/SRS/provider docs; unknowns → OQ or a `blocked` row.
- **Degraded-UX is the flag's off-state** — the kill switch doesn't just turn the feature off, it routes to the degraded path the design specified.
- **Validate before done** — BA Markdown validation (step 8).

## Inputs

```
/api-readiness <feature>          # reads the whole chain, assesses go/no-go
```

## Approach

1. **Gate.** Read the whole chain. `api-tests.md` absent → write readiness with go/no-go = **blocked (no test evidence)**; refuse to issue "go".
2. **Interview gaps** (one batched round): the cutover sequence + who flips each step · the kill-switch flag name + owner · the monitoring alerts + thresholds + runbook · the rollback sequence · the provider SLA + any sunset.
3. **Fact-list** — every gate item + its evidence/owner; the unknowns → `blocked` rows or OQs.
4. **Draft** per the template — the five concerns + the go/no-go table (each gate item: ready/blocked + evidence).
5. **scoped change preview** — go/no-go verdict + the blocked items (if any) + the cutover summary.
7. **Self-check** — a "go" requires every gate item `ready`; any `blocked` → verdict stays `no-go`.
9. **Output report** — the verdict + the blocked items (the path to "go") + next (flip the flags on "go").

## Gotchas

- **"Go" is a verb with consequences** — a soft "looks ready" is not a go; the table forces each gate item to declare ready/blocked with evidence.
- **Rollback must be real** — "disable the flag" is half a rollback; the other half is backing out data already written to our DB / sent to the provider.
- **Their SLA is our dependency** — if the provider's SLA is worse than our NFR availability, that's a `blocked` row, not a hope.
- **Sunset dates bite** — a provider EOL in the cutover window is a hard block; record the date.
