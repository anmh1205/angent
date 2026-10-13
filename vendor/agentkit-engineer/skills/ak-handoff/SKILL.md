---
name: ak-handoff
description: Create a portable, redacted continuation artifact that lets a successor agent resume in-progress work safely across sessions, models, or harnesses.
license: MIT
metadata:
  author: agentkit
  port: angent-fallback
  upstream: "handoff@ce70edaa26247b84c2b9491a0cdb4964f65cf3a5"
---

# Handoff — Portable Fallback

Handoff is a **continuation view**, not the canonical source of truth and not permission to perform future effects.

ANGENT Continuity owns the active-work frontier. This Skill renders enough of that frontier, plus verified local/provider evidence, for a successor agent to resume safely.

Read:
- `references/artifact-schema.md`;
- `references/redaction-patterns.md`.

## When to use

Use when:
- switching session/model/harness;
- context is being compacted;
- handing a bounded workstream to another agent;
- preserving a readable continuation artifact for later work.

Continuity should still persist active work proactively; handoff is not the only time state is saved.

## Gather verified state

Collect only what can be supported:
- mission/outcome;
- current scope and important constraints;
- completed/verified work;
- current unfinished frontier;
- consequential decisions and why they matter;
- artifacts/source versions;
- tests/checks already run;
- blockers and unresolved uncertainty;
- pending/ambiguous external effects;
- exact next safe action.

Use “not captured / not verified” instead of inventing missing state.

## Reconcile before writing

When practical, refresh state that may have changed:
- repository branch/HEAD/status;
- issue/task state;
- provider/deployment state;
- artifact existence.

The handoff reflects current evidence plus Continuity state.

## Redaction

Never include secrets, API keys, tokens, cookies, private credentials, or unrelated personal data.

Use the redaction reference before persisting a shared artifact.

## Artifact

Write a Markdown continuation artifact when a durable file/document is appropriate.

The artifact should remain useful without the previous transcript.

Do not embed large diffs/logs; point to artifacts/commits/files and summarize the evidence that matters.

## Successor behavior

A successor should:
1. read the handoff/frontier;
2. apply current AGENTS.md and newest user instruction;
3. validate stale-sensitive pointers;
4. reconcile ambiguous effects;
5. continue from the first unfinished valid unit.

Handoff context does not create authorization for deploy/publish/delete or other effects.

## No side effects

Creating a handoff must not launch a coding runtime, spawn workers, mutate the project beyond the handoff artifact, or silently execute the next step.
