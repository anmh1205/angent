---
name: angent-contract
description: Define the current task boundary, source-of-truth, constraints, authority, risk boundaries and state-based success semantics without solving the task.
---

# ANGENT Contract — Task Boundary

Contract compiles the user's current request into the smallest task model that materially affects correctness.

It does not choose the solution, reasoning path, teaching structure or action graph.

## Load references progressively

- references/task-model.md — requested outcome, underlying objective, target, scope and constraints.
- references/authority-and-success.md — effect authority, blast radius, completion semantics and evidence.

## Establish the actual outcome

Separate:
- the **requested action** — what the user explicitly asked to do;
- the **underlying objective** — why the user wants it, when that is clear and materially changes correctness;
- the **success state** — what must actually be true before completion can be claimed.

Do not replace an explicitly required means with another strategy merely because the objective seems obvious.

If requested action and objective materially conflict, preserve the instruction and surface the conflict only when it changes the work.

## Scope and invariants

Capture hard constraints, exclusions and durable invariants that downstream Reasoning must preserve.

Examples:
- use one production Docker image;
- do not release yet;
- audit all pages, not only the latest example;
- use GitHub for source edits and a separate runtime for testing;
- keep a particular architecture decision intact.

Do not inflate trivial preferences into hard constraints.

## Source of truth

Identify which provider/artifact establishes each important fact.

A task can have several sources of truth for different claims:
- Git for repository content/version;
- Jira for issue state;
- Notion for documentation;
- deployment/provider APIs for runtime state.

Source-of-truth does not replace active task state in Continuity.

## Authority

Track what the user has actually authorized:
- answer-only;
- read/audit;
- local reversible change;
- repository mutation;
- external communication;
- deploy/release/delete or other high-impact effects.

Historical momentum does not grant current authority.

## Success semantics

Prefer state-based success:

```text
requested endpoint
+ required evidence
+ preserved constraints
= completion
```

A commit, tool response, generated file, progress report or issue comment is not automatically completion.

## Ambiguity

Resolve ambiguity only when it can materially change correctness, scope, authority or endpoint.

Do not stop a runnable task merely to ask about harmless details that can be handled with a reasonable assumption.

## Output

Return a compact task model to Context/Reasoning/Execution/Quality.

It should be small enough to stay active across the task and explicit enough that downstream owners cannot silently redefine the objective.
