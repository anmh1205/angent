---
name: ak-watzup
description: Summarize in-flight work from Git branches/worktrees, plans and roadmaps, prioritizing safe next steps with truthful scanner and remote-ref limitations.
metadata: {port: angent-fallback, mode: degraded}
---

# Watzup — Portable Fallback

Stable Engineer 2.19.0 Watzup is a **read-only project handoff/status scanner**, distinct from ak-handoff conversation/context compaction. Its packaged `watzup-scan.cjs` traverses local/remote refs, worktrees, incomplete plans, roadmap milestones and priority-ranked next steps. This fallback cannot claim the original scanner ran or reproduce its cross-ref inventory automatically.

## Native scan if available

First verify the scanner file and Node runtime **in the installed Skill's actual package location**. If available and authorized for read-only inspection, invoke the native scanner with `--json`, parse its actual output and disclose failures. Network `--fetch` is **not** default: use only when the user specifically wants freshly fetched remote refs and the active Git scope permits it. Scanner invocation must not silently checkout, merge, edit, commit or push.

The stable priority scheme places checkout hygiene (dirty tree/detached HEAD) first, followed by active branch/worktree alignment, plan statuses/progress, visible source provenance and roadmap milestones. Scores are heuristic navigation aids, not acceptance evidence or permission to switch branches.

## Portable scan

Read only relevant supported surfaces:
1. current repository, exact branch/detached HEAD, clean/dirty status and authoritative current Git ref;
2. existing worktrees and local/remote branch refs **as observed**, with a stale-ref warning when not refreshed;
3. active and incomplete plan/phase files from **the worktrees/ref contents actually readable**; completed/total checkboxes are progress claims needing source checks;
4. roadmap/milestone docs when they exist and are authoritative;
5. ANGENT Continuity frontier and connected task status when necessary to avoid selecting the wrong currently active work.

A provider GitHub branch listing alone does not prove all local worktrees are present. Never extrapolate a local checkout status from remote-only inspection. If source access or scanner fails, report the exact observation boundary and provide only supported partial findings.

## Report and next action

Summarize current state (branch/head/working tree), recent relevant work, in-flight plans with checked vs unchecked counts, current roadmaps, 1–6 prioritized next steps with concise rationale and unresolved issues (stale ref, dirty tree, unresolved plan mapping, unsupported worktrees). Prefer the first **valid unfinished unit**, not the most recent commit summary.

Watzup **does not** implement, mutate plans/tasks, checkout branches, push, merge or fetch without separate user authority. It also does not replace durable Continuity or ak-handoff.
