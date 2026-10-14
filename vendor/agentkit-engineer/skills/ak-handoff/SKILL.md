---
name: ak-handoff
description: Create a portable, redacted continuation artifact that lets a successor resume in-progress work safely across sessions, models, harnesses, or Kits.
license: MIT
metadata:
  author: agentkit
  port: angent-fallback
  upstream: "handoff@ce70edaa26247b84c2b9491a0cdb4964f65cf3a5"
---

# Handoff — Portable Fallback

Handoff is a **continuation view**, not the canonical source of truth and not permission to perform future effects.

ANGENT Continuity owns the active-work frontier. This Skill renders enough of that frontier, verified source/provider evidence, and decision context for a successor to resume safely.

Read:
- `references/artifact-schema.md`;
- `references/redaction-patterns.md`.

## When to use

Use when:
- switching session/model/harness/Kit;
- context is being compacted;
- handing a bounded workstream to another agent;
- preserving a readable continuation artifact for later work.

Use `ak-watzup` for a status reconstruction from Git/worktrees/plans rather than a conversation/session continuation artifact.

Continuity should still persist active work proactively; handoff is not the only time state is saved.

## Gather verified state

Collect only what can be supported:
- mission/outcome and current scope;
- important constraints and authority boundary;
- verified completed work;
- unfinished frontier branches and dependencies;
- RUNNABLE / WAITING_EXTERNAL / BLOCKED state when it changes continuation;
- long-running operation handles + next informative observation condition when needed;
- consequential decisions plus compact decision basis/reconsideration trigger when useful;
- accepted baseline/artifact/source versions;
- tests/checks already run;
- blockers, stale/recheck state, and unresolved uncertainty;
- pending/ambiguous external effects;
- exact next safe/runnable action set.

Include rejected approaches/traps only when forgetting them would likely repeat a known failure.

Use “not captured / not verified” instead of reconstructing missing state from memory.

## Reconcile before writing

When practical, refresh state that may have changed:
- repository branch/HEAD/status/worktree;
- issue/task state;
- provider/deployment state;
- artifact existence/version;
- saved long-running operations whose current state matters.

The handoff reflects current evidence plus Continuity state.

## Redaction

Never include secrets, API keys, tokens, cookies, private credentials, customer data, or unrelated private/personal data.

Prefer pointers and provider/object identifiers over copied sensitive content.

## Artifact

Write concise portable Markdown in a safe project-local location when a durable file is appropriate.

The artifact should remain useful without the previous transcript.

Do not embed large diffs/logs; point to plans, commits, issues, artifacts, tests, files, and provider objects and summarize what they establish.

## Successor behavior

A successor should:
1. apply newest user instruction and applicable `AGENTS.md`;
2. load the handoff plus canonical Continuity state when available;
3. validate stale-sensitive pointers/decision premises;
4. reconcile ambiguous effects;
5. restore multi-branch scheduling state;
6. continue from a valid RUNNABLE branch rather than blindly repeating the last action.

Handoff context does not create authorization for implementation, Git delivery, deploy, publish, delete, spend, or other external effects.

## Effect boundary

Creating a handoff may write only the accepted handoff artifact/location.

It must not silently launch implementation, spawn workers, mutate unrelated project state, commit/push, or execute the “next step”.
