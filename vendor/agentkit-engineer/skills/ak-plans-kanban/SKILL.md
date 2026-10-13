---
name: ak-plans-kanban
description: Render active plan/frontier data as a Kanban/progress view using available artifacts or task systems; no AgentKit dashboard is required.
metadata: {port: angent-fallback, mode: adapted}
---

# Plans Kanban — Portable Fallback

Use when the user wants a visual/status view of active plans.

## Sources

Read:
- files-first plan;
- ANGENT Continuity frontier;
- connected issue/task system when it is authoritative for status.

## Columns

Use only statuses that reflect the actual work model, commonly:
- Ready / Todo;
- In Progress;
- Blocked / Decision Required;
- Done / Verified.

Do not mark Done from worker self-report without evidence.

## Output

Render as Markdown table, task board, connected project view or another supported surface.

The board is a projection of task state, not the canonical plan itself.
