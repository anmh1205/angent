# Frontend/runtime verification

Use only when the defect affects rendered UI, browser interaction, or client runtime behavior.

## Capability selection

Use the best available route:
1. project-native repeatable browser tests;
2. harness browser/computer-use capability;
3. another installed browser/testing capability.

Do not require a named AgentKit browser Skill.

## Verify the actual symptom

Depending on the bug, inspect:
- rendered state;
- interaction flow;
- responsive/layout behavior;
- loading/empty/error/auth states;
- console/network failures;
- accessibility/keyboard behavior when relevant.

A successful build is not visual/runtime verification.

## Authenticated state

Use existing authorized test/session state when the harness supports it.

Do not copy cookies/tokens into reports or handoff artifacts.

## Evidence

Capture screenshot/trace/log only when it proves something material.

State what each artifact demonstrates.
