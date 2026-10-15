---
name: ak-team
description: Coordinate live teammate sessions with shared work, direct communication, ownership, verification and cleanup when the active runtime exposes a real team lifecycle.
metadata: {port: angent-fallback, mode: degraded, baseline: "AgentKit Engineer 2.19.0"}
---

# Team — Portable Fallback

Use only when the active harness exposes the **live team lifecycle** required for real multi-session teammate collaboration.

Read `references/team-protocol.md`.

## CLI independence

A live Team does not require the `ak` executable when the host itself provides persistent teammates, shared task state, direct messaging, joining and shutdown. Conversely, a Markdown Skill cannot supply these live capabilities on its own. For a requested *result* rather than a persistent Team, `ak-orchestrate` or sequential specialist Skills are the correct portable routes; keep Team's own lifecycle boundary intact.

## Required runtime capability

Before starting, verify the live runtime can provide the semantics this workflow depends on:

- create independent teammate sessions;
- maintain shared work/task state;
- send/receive direct messages or equivalent coordination;
- wait/join on teammate progress;
- shut down teammates;
- clean up team/session state.

If any required lifecycle capability is absent, **do not silently substitute ordinary one-shot subagents or sequential role simulation and still call it Team**.

Instead:
- use `ak-orchestrate` for independent one-shot/headless jobs when appropriate;
- use Cook/Reasoning for sequential work;
- otherwise return the exact capability blocker.

This explicit degraded boundary is part of portable correctness.

## When Team is justified

Use when:
- several independent workstreams need persistent context;
- teammates benefit from direct coordination during the run;
- shared state/ownership must evolve while work proceeds;
- lead-mediated integration is materially better than separate one-shot jobs.

Do not use Team merely to obtain more opinions or to parallelize tightly coupled work.

## Lifecycle

1. Define parent outcome, accepted scope and why live-team semantics are useful.
2. Decompose independent jobs and shared dependencies.
3. Give each teammate a narrow context contract: role, work unit, inputs, ownership, allowed effects, acceptance evidence and return format.
4. Establish shared work/task state and explicit ownership.
5. Isolate concurrent writers where required.
6. Coordinate through live messages/state rather than duplicated full-context prompts.
7. Join evidence/artifacts after prerequisites settle.
8. Preserve disagreement until Reasoning resolves it.
9. Verify the integrated result; teammate completion messages are not endpoint proof.
10. Shut down teammates and clean up team state.

## Lead responsibilities

The lead owns:
- decomposition/dependency order;
- authority propagation;
- plan approval when the workflow requires it;
- ownership conflict handling;
- synthesis/integration;
- checking worker claims against artifacts/evidence;
- shutdown and cleanup.

Teammates do not become independent strategic owners.

## Failure handling

- blocked teammate → resolve missing context/dependency or re-scope; do not resend unchanged;
- unavailable lifecycle capability → hard-stop Team and route to another workflow;
- overlapping writes → sequence/isolate before continuing;
- conflicting conclusions → compare evidence or use an independent arbiter; never majority-vote;
- teammate failure → preserve useful partial evidence and reassess the remaining graph.

## Boundary

Team does not create effect authority.

ANGENT Reasoning remains strategic owner; Continuity remains durable task-state owner.
