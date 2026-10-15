# Review scope and baseline

A reliable review starts by establishing what should be compared and what behavior is required.

## Inputs

Use:
- user/task requirements;
- applicable AGENTS.md;
- implementation plan/spec when one exists;
- baseline/head or before/after state;
- changed files;
- tests and generated artifacts;
- related interfaces/consumers.

## Diff is not full scope

A change may affect files not in the diff through:
- shared APIs;
- schema/types;
- generated code;
- config;
- state ownership;
- database migrations;
- protocol changes;
- shared UI components.

Expand only where dependency/behavior justifies it.

## Spec compliance

Check:
- each material requirement has an implementation path;
- implementation does not add unintended behavior;
- exclusions/constraints remain preserved;
- migrations/backward compatibility are handled where required.

Do not “review quality” before confirming the code is solving the requested problem.
