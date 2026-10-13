# System model — reason across interacting components

Use a system model when the task depends on interactions rather than one isolated object.

## Dimensions

Model only relevant dimensions:

- **boundary** — what is inside/outside the system for this task;
- **components** — hardware, software, people, services or artifacts;
- **interfaces** — APIs, protocols, files, buses, queues, UI transitions or contracts;
- **data flow** — where information originates, transforms and terminates;
- **control flow** — who initiates actions and who can block/redirect them;
- **state ownership** — where authoritative state lives;
- **dependencies** — prerequisites and runtime/build/order relationships;
- **invariants** — relationships that must remain true;
- **failure boundaries** — where one layer can fail independently of another;
- **observability** — what evidence each boundary exposes;
- **side effects** — what actions can change external state.

## Choose the right boundary

Repository layout, organization chart and UI navigation are not automatically the system architecture. Pick the boundary that explains the user's objective.

## Cross-layer trace

For debugging or mechanism explanation, follow one stable object/event through layers when possible:

```text
input → interface → transformation → state change → output/observation
```

This exposes missing ownership or translation boundaries better than a catalogue of components.

## Failure localization

When an end-to-end outcome fails, distinguish:
1. whether each upstream prerequisite exists;
2. whether the interface transfers the expected representation;
3. whether the downstream component accepted/acted on it;
4. where observable evidence first diverges from expectation.

Do not attribute a downstream symptom to the most visible upstream component without this trace.
