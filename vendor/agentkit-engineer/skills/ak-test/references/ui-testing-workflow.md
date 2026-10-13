# UI testing workflow — portable fallback

Use the browser or UI-testing capability available in the active harness.

## Choose a route

Prefer, in order of fit:
1. project-native repeatable browser tests;
2. harness-provided browser/computer-use capability;
3. an installed external browser Skill/tool.

Do not require AgentKit-specific browser commands.

## Authentication

Prefer project-native fixtures/test accounts for repeatable testing.

If the test requires an already-authenticated real user session, use only a harness capability explicitly authorized for that state.

Do not copy credentials/cookies into reports or handoff artifacts.

## Visual validation

Check the states relevant to the task:
- target page/component renders;
- responsive/layout behavior where promised;
- loading/empty/error/auth states;
- interactive flow;
- console/network errors when observable;
- accessibility/keyboard behavior when in scope.

Build success alone is not UI verification.

## Parallel testing

Use multiple workers only when pages/flows are independent and the harness supports safe delegation.

Each worker needs a bounded page/flow and exact evidence to return.

## Output

Record screenshots/artifacts when useful and state what each proves.

If a visual capability is unavailable, mark the gap explicitly.
