---
name: ak-worktree
description: Create, inspect and clean isolated Git worktrees for concurrent or risky feature work while preserving repository safety.
metadata: {port: angent-fallback, mode: portable}
---

# Worktree — Portable Fallback

Use when isolated working trees reduce collision or make parallel work safer.

## Operations

- inspect existing worktrees and branch ownership;
- create a worktree from the correct base;
- verify submodule/monorepo requirements;
- detect stale/locked/orphaned worktrees;
- remove only when no uncommitted work or live dependency remains.

## Parallel work

Assign clear file/module ownership even with separate worktrees; worktrees prevent filesystem collisions, not logical/API conflicts.

## Safety

Never delete a worktree just because its branch appears old.

Inspect status and active task/frontier before cleanup.
