---
name: ba-dashboard
description: Business analysis dashboard specialist.
---

# ANGENT BA: dashboard

Maintained adaptation from MIT Dev BA Kit (copyright 2026 Edward Ngo): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/dashboard/SKILL.md

## Portability and authority

Use domain-specific steps below as methodology, not as authority or proof of tool execution. Original Claude-specific scripts, hooks, subagents, filesystem paths and approval levels are illustrative until verified in the current environment. ANGENT Root owns intent and routing; Execution owns writes and read-back; Quality verifies outcomes. Honor project naming and do not invent decisions. Validate completed Markdown with extensions/angent-ba/scripts/validate_documents.py when applicable. Jira and Confluence writes require current provider versions, granted permissions, idempotency review and read-back. Original agent-specific lifecycle or helper scripts are not assumed installed; report any validation that could not run.


# /dashboard — Vault status (one-file HTML)

## Goal

Scan the vault and render one self-contained HTML status page — features and their doc statuses, staleness (from `staleness.log`), recent activity (from `activity.log`), and Open-Question debt (unresolved OQs across the chain) — plus regenerate `docs/feature-list.md` (the status-lifecycle `* → approved` automation). **Outputs**: `docs/_shared/dashboard.html` + `docs/feature-list.md`.

## Constraints

- **Group C** (`feature-bootstrap.md`): empty vault → write a placeholder dashboard ("nothing yet — start with `/brainstorm` or `/urd`").
- **Read-only over sources** — scans docs; the ONLY writes are `dashboard.html` + `feature-list.md` (L1-gated; `approval-gate.md` notes dashboard is NOT exempt — it writes an HTML file).
- **Self-contained HTML** — inline CSS, no CDN; the gallery skill's self-contained pattern.
- **`dashboard.html` path** — `docs/_shared/dashboard.html` (a `_shared/` singleton like `traceability.md`).
- **Feature-list regeneration** — `docs/feature-list.md` from each feature's docs' `status:` (the status-lifecycle `* → approved` transition triggers this; `/dashboard` does it on demand too).
- **OQ debt** — count unresolved OQs per feature (parse the checkbox lists); a feature with 5 open OQs is visibly riskier.
- **Idempotent** — re-run regenerates (versioned diff).
- **Validate before done** — BA Markdown validation doesn't cover `.html`/`feature-list.md` (excluded types); self-check the HTML is well-formed.

## Inputs

```
/dashboard              # render + regenerate feature-list
/dashboard --open       # render, then open in browser
```

## Approach

1. **Scan the vault** — per feature: its docs + statuses + `updated:` dates; count OQs; recent activity from `activity.log`; staleness from `staleness.log` if present. Also read `docs/_shared/project-context.md` frontmatter (`source_watermark` + `staleness_budget_commits`) → compute commit drift (commits since the watermark vs the budget) for a project-context fresh/stale flag.
2. **Aggregate** — feature statuses (how many approved/in-review/draft), OQ debt per feature, stale docs, last-activity per feature.
3. **Render `dashboard.html`** — self-contained: a top-of-page **Project context: fresh / stale (N commits since scan)** callout (when a `/discover` profile exists) + a feature table (status pills, OQ count, last-updated, stale flag) + an activity feed (recent N events) + an OQ-debt callout. Light, no CDN.
4. **Regenerate `docs/feature-list.md`** — one row per feature: slug + status + doc count + OQ count + updated.
5. **scoped change preview** — feature count + status mix + OQ debt + stale count + project-context fresh/stale flag.
7. **Output report** — the dashboard path + the status mix + the riskiest feature (most OQs/stale) + next.

## Gotchas

- **Status, not coverage** — the dashboard answers "where are we?" (statuses, staleness, debt); `/gap` answers "what's missing in the chain?". Both, different jobs.
- **OQ debt is the leading indicator** — a feature with growing OQ debt is drifting from its sources; surface it, don't hide the count.
- **feature-list.md is auto-gen** — never hand-edit it; it's regenerated from the docs' statuses. (Excluded from the activity log like other auto-gen files.)
- **Self-contained matters** — a dashboard that fetches a CDN breaks offline/on intranet; inline everything.
