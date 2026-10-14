---
name: angent-contract
description: Define task boundary, evolving constraints, authority and state-based success semantics without solving the task.
---

# ANGENT Contract — Task Boundary

Contract compiles the current request into the smallest task model that materially affects correctness. It does not choose the solution, reasoning path or action graph.

## References

- references/task-model.md
- references/authority-and-success.md
- references/constraint-evolution.md

Use constraint evolution for corrections, revisions and multi-turn work.

## Outcome

Separate requested action, underlying objective when relevant, and success state. Do not silently replace an explicitly required means.

## Active obligations

A newer instruction does not automatically replace older requirements.

Classify material changes as ADD, REFINE, SUPERSEDE, SCOPED_EXCEPTION or CONFLICT.

Maintain the currently binding set of:

- hard constraints and exclusions;
- accepted project/architecture decisions;
- authority boundaries;
- accepted quality floors;
- unresolved promises;
- scoped exceptions.

Preserve provenance and scope. Remove an obligation only when current authority actually changes it.

A complaint is evidence of a failed property; it is not an instruction to maximize the opposite property.

## Scope and source of truth

Capture the scope and invariants downstream Reasoning must preserve. Identify which provider or artifact establishes each important fact. Provider state does not replace active task state.

## Authority

Track what effects the current instruction authorizes. Historical momentum does not grant current authority.

For consequential effects, authority is not finished at planning time: it must still cover the resolved operation, target and material arguments at the invocation boundary. A changed target/scope/argument set requires revalidation rather than inheriting an earlier generic approval.

## Success

Prefer state-based success:

```text
requested endpoint + required evidence + active obligations preserved = completion
```

For revisions, success also requires that the requested defect is repaired without violating protected properties of the accepted baseline.

Intermediate tool success is not automatically completion.

## Ambiguity

Resolve ambiguity only when it can materially change correctness, scope, authority, active obligations or endpoint.

## Output

Return a compact task model that downstream owners cannot silently redefine or weaken.
