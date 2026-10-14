---
name: ak-journal
description: Maintain chronological technical journals as historical evidence without treating them as current authority, task state or promoted learning.
metadata: {port: angent-fallback, mode: adapted}
---

# Journal — Portable Fallback

Journal create/list/show/validate are ordinary file/document actions and **do not require native `ak journal`**. Read `references/cli-free-lifecycle.md`; prefer existing project storage and real host file tools. Native journal publication/provider scripts remain separate capabilities and cannot be presumed.

## Runnable optional local helper

For a local worktree with Python and writable project files, `scripts/journal_files.py` provides **real** `create`, `list`, `show` and `validate` actions without `ak`. It uses collision-safe exclusive file creation, scoped `plans/journals/` paths and read-only history queries. Use a project's own existing journal system or connected document editor when that is authoritative. Do not assume a local filesystem exists in ChatGPT-only execution.

```bash
python3 scripts/journal_files.py --project-root /path/to/project create --title "Fix install race" --date 2026-10-15 --summary "Causal findings" --stdin
python3 scripts/journal_files.py --project-root /path/to/project list
python3 scripts/journal_files.py --project-root /path/to/project validate --name 2026-10-15-fix-install-race.md
```

File generation writes evidence only after actual authorized invocation. `create` reads its private body from stdin, never overwrites existing entries, and returns the verified file path. The helper is a subset of journal **document semantics**, not social publication or an AgentKit-managed journal database.

## Load progressively

- `references/journal-semantics.md` — what a journal is and is not.
- `references/incident-entry.md` — capture hard failures/incidents.
- `references/using-journals.md` — retrieval, retrospective and Learning use.

## Use for

- meaningful implementation milestones;
- failed approaches worth preserving;
- production/staging incidents;
- difficult debugging sessions;
- important environment/provider observations;
- retrospective evidence.

Keep entries compact and linked to artifacts/commits/issues.

A journal is historical evidence—not AGENTS.md, not Continuity, not a current architecture decision and not an automatic global lesson.

## Stable 2.19.0 lifecycle and publication boundary
The native workflow offers `ak journal create` (stdin-compatible), `validate`, `list`, and `show` with dated collision-safe filenames. With or without native `ak`, use the project's actual authorized journal store or connected file tool. Read and write the durable Markdown directly, enforcing collision-safe names and read-back; only use the native command when explicitly administering an AgentKit-managed journal store. Explicit journal requests are not suppressed by automatic closeout preferences. For automatic journal steps respect `--skip-journal` (when supported), then project/user `journal.auto`, then default. Record actual session evidence, changed artifacts, decisions, results and next steps, while keeping durable decisions and current work state in their separate owners.

For optional social distribution load `references/publication-boundaries.md`. Upstream Zernio CLI scripts, config cascade, media generation and idempotent post state are not bundled. Require an actual provider, per-channel content, exact effect authorization, dry-run where available, success URLs and reconciliation of uncertain writes. Without a provider, journal locally and do not claim publication.
