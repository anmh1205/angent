# Engineer routing — native first, fallback when needed

ANGENT obtains engineering specialist capability from one of two sources:

1. official native AgentKit Engineer;
2. ANGENT's portable Engineer capability bundled in the same plugin.

Read `engineer-selection.md` for the source-selection contract and packaging boundary.

## Native usability

Do not equate “ak exists” with usable Engineer.

Native is selected only when the active harness/session establishes that native Engineer can actually be discovered/invoked.

AgentKit CLI version/doctor output can provide supporting health evidence, but cached files or binary presence alone do not prove active runtime visibility.

## Fallback

When native Engineer is absent, unusable, or its usability cannot be established, use the bundled `ak-*` Skills from ANGENT's discoverable `skills/` directory. Their maintained source remains at `extensions/angent-engineer/`, and the 16 portable role contracts are included as supporting files.

A single installed plugin does **not** guarantee the host hides fallback Skills when native Engineer is present. Route the task to one provider; avoid mixing native and fallback workflows. See `engineer-selection.md` for this limitation and the package boundary.

## Same semantics

Regardless of source:

- Scout/Explore gathers codebase evidence;
- Researcher gathers external/technical evidence;
- Planner proposes implementation structure;
- Developer/Cook executes bounded plans;
- Debugger establishes root-cause evidence;
- Tester/Reviewer provide implementation checks;
- Handoff provides continuation state;
- Team/Orchestrate is used only when parallelism/isolation creates real value.

Reasoning retains strategic ownership.

## Portable runtime behavior

Do not create a generic Capability Broker.

The runtime adapter only needs to:

1. report whether native Engineer is actually usable;
2. select native **or** the already bundled fallback for the work, without claiming to install/uninstall or hide a static catalog;
3. project fallback role files into native subagents when supported;
4. otherwise keep the same role semantics through one-shot or sequential execution.

If a fallback Skill depended on AgentKit-specific runtime machinery:

- preserve files-first plan semantics without requiring the CLI;
- map active-work state into ANGENT Continuity;
- use harness-native delegation when available;
- degrade team/orchestrate to sequential execution when unavailable;
- use proactive Continuity capture instead of requiring hooks.

Do not claim portability if removing a runtime dependency silently removes the workflow capability.
