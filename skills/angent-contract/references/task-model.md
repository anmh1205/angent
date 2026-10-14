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
- **success components** — optional independently verifiable required components when the endpoint is genuinely composite;
- **required evidence** — what proves the success state;
- **blocking ambiguity** — unresolved ambiguity that truly prevents correct work.

## Requested means and objective

Use:

~~~text
requested action → intended effect → success state
~~~

Reason about whether the requested action produces the objective, but do not silently substitute another means when the user explicitly constrained the method.

## Collaboration instructions that constrain action

Some collaboration instructions are descriptive method state; others also create binding task constraints.

Examples:
- “audit only” restricts write authority/scope in Contract and is also represented as the current collaboration mode;
- “report before edit” creates a sequencing obligation and may be represented in collaboration state;
- “continue autonomously” describes initiative but does not grant an effect outside the current authority boundary.

Context may reconstruct how to work; Contract remains the owner of anything that changes what actions are allowed or required.

## Composite success

Use component outcomes only when the requested endpoint naturally has independent required parts.

A component can be verified complete while the overall task remains incomplete. Preserve that verified progress so Continuity/Quality do not redo it, but never promote partial completion to overall success.

Do not invent a numeric score or partial-credit system for a task that has a binary endpoint. Components exist to preserve truth about progress and dependency, not to make an unfinished task look complete.

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
