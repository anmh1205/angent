# Task model — define the work before solving it

The task model is the compact boundary between user intent and reasoning.

## Core fields

Use only fields that matter:

- **requested outcome** — state/result the user explicitly asked for;
- **underlying objective** — purpose behind the requested action when clear and materially relevant;
- **target** — system, artifact, decision or audience being changed or understood;
- **source-of-truth map** — provider/artifact/version for important claims;
- **active obligations** — currently binding constraints, accepted decisions, exclusions, quality floors, promises and scoped exceptions;
- **instruction changes** — ADD / REFINE / SUPERSEDE / SCOPED_EXCEPTION / CONFLICT relations when a new instruction changes prior state;
- **soft preferences** — preferences that may be balanced;
- **scope/exclusions** — what is inside/outside the task;
- **authority** — allowed read/write/external effects;
- **success semantics** — what must be true to claim completion;
- **required evidence** — what proves the success state;
- **blocking ambiguity** — unresolved ambiguity that truly prevents correct work.

## Requested means and objective

Use:

```text
requested action → intended effect → success state
```

Reason about whether the requested action produces the objective, but do not silently substitute another means when the user explicitly constrained the method.

## Scope drift

Watch for:
- latest-example collapse;
- a specialist expanding into neighboring modules;
- a tool convenience redefining the endpoint;
- an intermediate artifact becoming mistaken for the requested result.

When scope changes by explicit user instruction, update only obligations and dependent decisions actually affected by that change. Do not treat recency alone as supersession.

## Minimality

Simple factual questions do not need a formal visible task object.

Complex tasks benefit from a compact internal model that remains stable enough for Reasoning, Continuity and Quality to share.
