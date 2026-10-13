# Task model — define the work before solving it

The task model is the compact boundary between user intent and reasoning. It is not a form to expose by default.

## Core fields

- **requested outcome** — what state/result the user asked for;
- **underlying objective** — the purpose behind the requested action when it is clear and materially changes the solution;
- **target** — system, artifact, decision or audience being changed or understood;
- **source of truth** — the authoritative provider, artifact, version or live state;
- **hard constraints** — conditions that cannot be traded away;
- **soft preferences** — preferences that may be balanced against other goals;
- **scope / exclusions** — what is inside and outside the task;
- **authorization** — answer-only, read-only/audit, or permitted mutations/effects;
- **success semantics** — what must be true to claim completion and what evidence proves it;
- **open ambiguity** — only ambiguity that materially blocks correct reasoning.

## Requested action is not always the objective

A user may request a means because it is expected to produce an outcome. Preserve the means as a constraint when explicitly required, but reason about whether the result satisfies the underlying objective.

Example structure:

```text
requested action → intended effect → success state
```

Do not silently replace an explicit instruction with a different strategy. When action and objective conflict, preserve the current instruction and surface the conflict only if it matters.

## Success semantics

A completion criterion should be state-based where possible:

```text
provider/artifact state + acceptance evidence → completion
```

A commit, tool response, draft, or progress message is not automatically a success state.

## Minimality

Capture only fields that change correctness. Simple factual questions should not be inflated into a formal task object.
