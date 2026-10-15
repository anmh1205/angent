# Portable Engineer agents

These files define ANGENT's harness-neutral fallback roles for the 16 Engineer agents.

They are **role semantics**, not raw copies of upstream runtime prompts.

## Projection

A runtime adapter may map:
- `name` and `description` to the runtime's agent/subagent metadata;
- `capabilities` to available tools;
- `memory_scope` to the runtime's supported memory mechanism;
- the Markdown body to the agent's role instruction.

Model names and tool identifiers are intentionally not hard-coded because those are runtime-specific.

## Ownership

These roles provide specialist capability. They do not replace ANGENT's owner model.

- Reasoning retains strategic decision ownership.
- Contract retains scope/authority.
- Continuity retains active-work state.
- Quality retains final task-level verdict.
- Authoring retains reader-facing composition.

If the active harness cannot spawn subagents, use the same role semantics sequentially in the main agent rather than failing the workflow.
