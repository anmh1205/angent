# Engineer routing — native first, fallback when needed

ANGENT obtains engineering specialist capability from one of two sources:

1. official native AgentKit Engineer;
2. ANGENT's portable Engineer fallback plugin.

Read `engineer-selection.md` for the source-selection contract and packaging boundary.

## Native usability

Do not equate “ak exists” with usable Engineer.

Native is selected only when the active harness/session establishes that native Engineer can actually be discovered/invoked.

AgentKit CLI version/doctor output can provide supporting health evidence, but cached files, documentation, binary presence, or a historical install receipt do not prove active runtime visibility.

## Fallback

When native Engineer is absent, unusable, or its usability cannot be established, use the plugin root at:

`vendor/agentkit-engineer/`

The fallback plugin has its own Agent Plugins manifest and targets the **documented stable public Engineer workflow contract**:

- **103 public Skill identities**;
- **16 portable Agent role definitions**.

Expected identities are recorded in `vendor/agentkit-engineer/STABLE_CATALOG.json`.

This identity target is deliberately distinct from an exact upstream package-parity claim. On 2026-10-14, current stable CLI 2.19.0 exported 102 portable Skill identities while stable documentation described 103 public identities. The fallback follows the documented public workflow contract and records the observed registry/export drift explicitly.

Fallback readiness requires the exact discovered Skill/Agent identity sets to match that catalog. A matching directory count alone is not parity evidence.

Retired routes remain compatibility documentation outside public Skill discovery. Internal support also remains outside the public `skills/` root.

Do not expose native and fallback Skill libraries together by default.

## Same strategic boundary, workflow-specific runtime semantics

Regardless of source:

- Scout/Explore gathers codebase evidence;
- Researcher gathers external/technical evidence;
- Planner proposes implementation structure;
- Developer/Cook executes bounded plans;
- Debugger establishes root-cause evidence;
- Tester/Reviewer provide implementation checks;
- Handoff provides continuation state;
- Team/Orchestrate are used only when their actual coordination semantics are available or honestly adapted.

ANGENT Reasoning retains strategic ownership.

Do not flatten distinct upstream workflow guarantees into one generic delegation fallback.

In particular:

- **Team** requires the live team lifecycle its contract depends on: creation, shared work/state, bounded delegation, direct coordination, wait/status, shutdown/cleanup, and required isolation controls. If that lifecycle is unavailable, `ak-team` must block/degrade honestly and offer another explicitly named route. Do not silently run ordinary subagents or sequential role-play and call it Team.
- **Orchestrate** may map a dependency-aware job graph onto harness-native workers/subagents or an explicit sequential degradation when that preserves the selected workflow semantics. It must not fabricate parallelism, durable background execution, supervisor state, or isolation the harness does not provide.

## Portable runtime behavior

Do not create a generic Capability Broker.

The runtime adapter only needs to:

1. report whether native Engineer is actually usable;
2. expose native **or** fallback;
3. project fallback role semantics into the selected workflow only where that workflow permits the available runtime;
4. expose real limitations rather than simulating unavailable guarantees.

When an upstream workflow depends on AgentKit-specific mechanics:

- preserve files-first plan semantics without requiring the CLI;
- map active-work state into ANGENT Continuity;
- use harness-native delegation when the workflow permits it;
- use proactive Continuity capture instead of requiring hooks;
- use the browser/computer-use/test capability actually available;
- block or choose a separately named route when the missing runtime capability is load-bearing.

Do not claim portability if removing a runtime dependency silently removes a workflow guarantee.
