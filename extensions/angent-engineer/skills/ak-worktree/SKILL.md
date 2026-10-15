---
name: ak-worktree
description: Create, inspect, audit and safely clean isolated Git worktrees for parallel/risky work, including exact branch names, base selection, monorepos and submodules.
metadata: {port: angent-fallback, mode: adapted, baseline: "AgentKit Engineer 2.19.0"}
---

# Worktree — Portable Fallback

Worktrees isolate filesystem/history work; they do not isolate logical API/schema conflicts.

## Operations

- **info/list** — inspect repo type, worktree root, base, ownership and health;
- **create** — create an isolated worktree from an explicit or safely detected base;
- **status/audit** — inspect dirty state, branch divergence, locks and stale/orphaned metadata;
- **remove** — remove only after proving no uncommitted work/live dependency is lost;
- **prune** — clean stale metadata, preferably preview/dry-run first.

## Creation

Before create:
1. inspect canonical repository and existing worktrees;
2. preserve an explicitly supplied branch name exactly when requested;
3. otherwise derive a project-conformant branch name;
4. resolve the base from explicit instruction/project conventions/live refs rather than a blind global default;
5. for monorepos, resolve the intended project/workspace;
6. inspect submodule requirements;
7. choose worktree root according to project conventions/environment;
8. verify target path/branch does not collide.

After create, initialize submodules/dependencies only when the project/work unit needs them. Use the project's actual package/tooling, not a hard-coded ecosystem list.

## Parallel work

Assign explicit file/module/state ownership even with separate worktrees.

Before parallel integration, revalidate shared interfaces/dependencies; two worktrees can independently implement incompatible assumptions.

## Cleanup

Never delete a worktree because it merely looks old.

Check:
- dirty/untracked/staged state;
- commits not reachable from a preserved branch/remote;
- active Continuity/frontier ownership;
- open PR/worker dependency;
- submodule/monorepo implications.

If any material ownership is ambiguous, block cleanup or dry-run the prune.

## Result

Return worktree path, branch/base, dirty/divergence status and cleanup/creation effects.

A worktree is isolation convenience, not an OS sandbox or new effect authority.
