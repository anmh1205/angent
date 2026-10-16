---
name: ba-jira
description: Business analysis jira specialist.
---

# ANGENT BA: jira

Maintained adaptation from MIT Dev BA Kit (copyright 2026 Edward Ngo): https://github.com/nv-minh/dev-ba-kit/blob/main/skills/jira/SKILL.md

## Portability and authority

Use domain-specific steps below as methodology, not as authority or proof of tool execution. Original Claude-specific scripts, hooks, subagents, filesystem paths and approval levels are illustrative until verified in the current environment. ANGENT Root owns intent and routing; Execution owns writes and read-back; Quality verifies outcomes. Honor project naming and do not invent decisions. Validate completed Markdown with extensions/angent-ba/scripts/validate_documents.py when applicable. Jira and Confluence writes require current provider versions, granted permissions, idempotency review and read-back. Original agent-specific lifecycle or helper scripts are not assumed installed; report any validation that could not run.


# /jira — Push/sync user stories to Jira

## Goal

Sync the feature's user stories ↔ Jira issues bidirectionally: push stories as issues (one `US-` → one issue), write the returned key into `{feature}-story-index.md`'s `jira-key` column, and pull issue status back into the index. Mapping state in `.claude/state/atlassian/sync-state.yaml` `mappings.jira`.

## Constraints

- **External-write — hard HITL** (`atlassian-sync.md` §1): preview every issue + target project, explicit **Y** per write. `--dry-run` runs to the diff, writes nothing.
- **Jira MCP must be authenticated** — not connected → STOP with connect instructions; never fabricate keys.
- **Group B** (`feature-bootstrap.md`): needs `userstories/us-*.md` + the story index; missing → refuse + route `/userstory`.
- **One issue per story** (`atlassian-sync.md` Jira-specific); the story-index `jira-key` column is the canonical pointer.
- **Refuse `status: stale` stories** (`approval-gate.md` named hard gate) — route to `/userstory` to refresh first; a stale story pushed propagates outdated scope.
- **Watermark by story hash** — re-push only changed stories (no full-backlog re-push every run).
- **Bidirectional status map** — Jira statuses → our lifecycle (`draft`/`in-review`/`approved`/`shipped`); ambiguous mappings → ask, never guess.
- **No local doc output** — only the story-index `jira-key`/`status` columns + sync-state are edited.
- **Idempotent** — re-run updates existing issues (keys stable).

## Inputs

```
/jira <feature> --push              # push changed stories (default)
/jira <feature> --pull              # pull issue status into the index
/jira <feature> --push --dry-run    # preview, write nothing
```

## Approach

1. **Gate.** No stories → refuse + route `/userstory`. Verify Jira MCP auth; probe project access.
2. **Diff vs watermark** — read sync-state `mappings.jira`; compute changed stories (hash ≠ stored `source_hash`). Stale-status stories → BLOCKING, route to `/userstory`.
3. **Push preview** — per changed story: the issue title/summary/desc (from the story), the target project, the expected key (new vs update). `--pull` instead → the issues whose status changed.
4. **L1 hard-gate preview** — list every issue write + "this writes to Jira"; get explicit **Y** (or stop at `--dry-run`).
5. **On Y → MCP writes** — create/update each issue; collect returned keys.
6. **Edit the story index** — write keys into `jira-key` (push) or status from the pull map (pull); tick `updated`.
7. **Update sync-state** — `mappings.jira` per story (key/url/last_synced/source_hash).
9. **Output report** — pushed/pulled counts + any stale-refused + coverage (`jira-key` filled / total).

## Gotchas

- **Never invent a key** — a write that returns nothing leaves the cell empty + reported, not faked.
- **Stale = hard stop** — it's the named gate for a reason; pushing a story whose FRs changed silently corrupts the backlog.
- **Status map ambiguity** — Jira's "In Progress" could be our `draft` or `in-review`; ask once, record the mapping, don't guess per run.
- **One issue per story** — don't bundle stories into an epic issue; the `jira-key` column is 1:1 (epics are a Jira-side grouping, not a story-side one).
