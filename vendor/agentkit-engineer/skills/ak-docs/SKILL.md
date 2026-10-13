---
name: ak-docs
description: Create, refresh and audit codebase documentation while preserving the project's existing information architecture and canonical AGENTS.md instructions.
metadata: {port: angent-fallback, mode: adapted}
---

# Docs — Portable Fallback

Use for README, architecture docs, developer guides, runbooks, API/project documentation and AGENTS.md maintenance.

Read `references/docs-audit.md`.

## Principles

- verify docs against source/config/current behavior;
- update the smallest authoritative document set;
- link rather than duplicate;
- keep AGENTS.md focused on stable agent/project instruction;
- keep task progress and dynamic memory out of AGENTS.md;
- preserve existing docs hierarchy unless there is a reason to reorganize it.

## Output

Return changed docs, source evidence used, stale/conflicting guidance resolved and remaining gaps.

Do not invent commands/configuration to make documentation look complete.
