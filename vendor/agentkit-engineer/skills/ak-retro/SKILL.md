---
name: ak-retro
description: Generate source-grounded engineering retrospectives with defined Git time windows, reproducible metrics, contextual delivery evidence and optional period/team comparisons.
license: MIT
metadata: {port: angent-fallback, mode: adapted}
---

# Retro — Portable Fallback

Use for a sprint, release, project or quarterly retrospective grounded in actual Git/issue/plan and test history. Stable Engineer 2.19.0 explicitly supports period selection, Git metrics, prior-period comparison, team-level breakdown and Markdown/self-contained HTML reports. These features are not inferred from subjective impressions.

## Time window and sources

Resolve a requested timeframe (7d, 2w, 1m, sprint, or explicit YYYY-MM-DD range) against the local repo calendar and Git history. If 'sprint' has no discoverable bounds, obtain its dates rather than treating the last seven days as the sprint. For comparisons, use an **equal-length preceding period**, consistent inclusive/exclusive timestamp boundaries, and the same collection methods.

Collect actual Git log and diff evidence for commit/activity distribution, change hotspots, authored revisions, test-file touches, churn and code change categories where measurable. Add PR/issue closing, test/CI, incident and plan acceptance evidence **only when available**; distinguish those providers from Git-only measurements. Avoid writing a synthetic history or interpreting shallow histories as full repo activity.

## Metrics

Read **references/metrics-and-reporting.md** for defensible formulas and common pitfalls. Commit frequency, LOC churn, active days, test-file change ratio and task completion are **descriptive indicators**, not judgments of individual productivity, code quality or 'velocity'. Identity aliases, bots, squash/rebase history, merge commits, generated changes and vacations can distort them.

Treat zero denominators and missing provider data as N/A, not fabricated zero. Do not estimate elapsed engineering effort solely from commit count or lines changed. For compare/team mode, state grouping and identity assumptions and avoid ranking people by LOC.

## Analysis and actions

1. Ground what shipped, was reverted or remained blocked in relevant change/test evidence.
2. Identify recurring rework, review/test gaps, concentrated hotspots, unplanned scope, dependencies and useful delivery practices.
3. Separate observation from causal hypothesis. Cross-check major interpretations against actual incidents, stakeholder context, issue state or source changes.
4. Recommend a small number of specific actions with affected owners/processes and observable next-period signals. Do not manufacture positives or 'lessons' for balance.
5. Deliver the requested Markdown or self-contained HTML report **only when the runtime can actually create/read back that artifact**. Respect the project's real report destination and don't claim upstream `plans/reports/` automatically exists.

## Boundaries

Retrospective inspection is read-only with respect to source code and branches. Report-file creation is an explicit allowed output only when requested/authorized. No commit, checkout, push, merge or silent team task mutation is implied. Identify command/environment access limits and uncollected metrics.
