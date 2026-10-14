---
name: ak-plans-kanban
description: Open a verified AgentKit integrated plans dashboard when installed; otherwise present an evidence-labelled read-only plan board without claiming native dashboard parity.
metadata: {port: angent-fallback, mode: degraded}
---

# Plans Kanban — Portable Fallback

Stable Engineer 2.19.0 Plans Kanban is **a thin launcher for the integrated AgentKit CLI dashboard**, not a standalone renderer or an independent plan-management engine. Native behavior is a browser view of the CLI's project/global-scoped `/plans` route. It must not be replaced silently by a Markdown table while still claiming the native dashboard is operational.

## Native dashboard path

1. Discover the actual installed AgentKit CLI and `ak config --help` / `ak config status --json`. Use a packaged `scripts/open-dashboard.cjs` only if it genuinely exists in that installation.
2. Reuse an existing compatible dashboard URL when available. The stable default is `http://127.0.0.1:8766/plans`, **but the actual port is read from the CLI**; do not hard-code it when the service moved.
3. Probe compatibility before opening: stable launcher accepts either `/api/health` whose features include `plans-dashboard`, or a successful `/api/plans` response. If incompatible, report the missing feature; don't open a misleading route.
4. Starting a persistent local server, opening a browser, changing its host/port, stopping processes or upgrading CLI is a real effect subject to runtime support and authorization. Upstream `ak config start --port 8766 --no-open --no-interactive` is an example, not implicit permission.
5. Project dashboard must show project-scoped plans; global dashboard global-scoped plans. Deprecated launch flags are compatibility inputs owned by the actual launcher, not a stable fallback contract.
6. For plan status/dependency mutations, use live `ak plan --help` or the authorized project-manager flow. This Skill remains visualization/navigation-only.

## Portable visualization

When the integrated CLI/server is unavailable, present a **clearly labeled fallback board** from the active plan, phase files and optional authoritative provider tasks. Common columns: pending, active, blocked/decision and verified complete. Include source provenance, dependency ordering and checked-vs-verified distinction. It may be a Markdown table, provider-native board or supported interactive view, depending on what actually exists.

A fallback board is not a replacement for multi-plan native live dashboard features (timeline, grid, navigation, user-scoped filtering) unless those features were really implemented/tested. Report that degradation.

## Safety

Never overwrite a plan, start an unrequested background service, fetch remote state or change issue status simply to display the board. Do not claim its data is fresh until the actual source and time boundary were observed.
