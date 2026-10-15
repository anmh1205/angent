# Skill design

A mature Skill answers:

- When should I activate?
- What outcome do I own?
- What do I explicitly not own?
- What input/context do I need?
- What is the core workflow?
- What are the important branches/gates?
- Which reference should be loaded for a deeper case?
- What evidence proves the Skill completed its job?
- What happens when a required capability is unavailable?
- Which runtime assumptions are essential versus replaceable?
- What safety/privacy/authority boundary constrains the workflow?

Discovery metadata should describe user intent/capability, not implementation trivia.

Use AGENTS.md for project-specific instruction rather than baking one project's conventions into a reusable Skill.

## Resource design

Add:
- `references/` for reusable depth or domain rules needed only in some cases;
- `scripts/` for deterministic/repeatable computation or file mechanics;
- `assets/` for output resources/templates;
- `agents/` only when the target ecosystem supports/uses those semantics and the role adds value.

Do not create resources because a template has empty directories.

## Existing Skill update

Before an update:
- identify the accepted behavior/baseline;
- determine the repair target and affected scope;
- preserve discovery/behavior outside the change;
- re-run relevant positive and counter-cases afterward.

An "optimization" that improves one benchmark while breaking established activation or workflow behavior is a regression.
