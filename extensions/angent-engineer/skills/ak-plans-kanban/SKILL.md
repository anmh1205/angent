---
name: ak-plans-kanban
description: Open a verified AgentKit integrated plans dashboard when installed; otherwise present an evidence-labelled read-only plan board without claiming native dashboard parity.
metadata: {port: angent-fallback, mode: degraded}
---

# Plans Kanban — Portable Fallback

The transferable capability is reasoning about work state and dependencies so the user can decide **what to act on next**. A visual board is one representation. Do not default to launching a server just to understand progress. When the user specifically requests the proprietary AgentKit dashboard, treat that separately as a native-product feature.

## Progress reasoning and representation

1. Discover actual plan source: active `plan.md`/phase files, authorized Jira/Notion/issue board or project-native plan owner; if none, ask for the missing plan **only if material**.
2. Inspect current phase/task states and dependencies without mutation. Separate user-marked `[x]` from evidence-backed verified complete, and blocked from merely pending.
3. Identify the **next feasible work** from dependencies and available evidence; avoid treating percentages/checked items as completion proof. Present a board only if it clarifies ownership, blocked state or next action, using the rendering medium the host genuinely supports.
4. Preserve source revision and freshness; expose contradictions between plan and live issue/task state rather than forcing a single invented status. Do not promise interactive drag/drop or history when no backend implements them.
5. For a status change, use `ak-plan` or the actual provider task editor under explicit update authority, then read back. Viewing alone is read-only.

## Portable visualization

When the integrated CLI/server is unavailable, present a **clearly labeled portable board** from the active plan, phase files and optional authoritative provider tasks. Common columns: pending, active, blocked/decision and verified complete. Include source provenance, dependency ordering and checked-vs-verified distinction. It may be a Markdown table, provider-native board or supported interactive view, depending on what actually exists.

A fallback board is not a replacement for multi-plan native live dashboard features (timeline, grid, navigation, user-scoped filtering) unless those features were really implemented/tested. Report that degradation.

## Safety

Never overwrite a plan, start an unrequested background service, fetch remote state or change issue status simply to display the board. Do not claim its data is fresh until the actual source and time boundary were observed.
