# Engineer routing — native first, fallback when needed

ANGENT obtains engineering specialist capability from one of two sources:

1. official native AgentKit Engineer;
2. ANGENT's portable Engineer fallback plugin.

Read `engineer-selection.md` for the source-selection contract and packaging boundary.

## Native usability

Do not equate “ak exists” with usable Engineer.

Native is selected only when the active harness/session establishes that native Engineer can actually be discovered/invoked.

AgentKit CLI version/doctor output can provide supporting health evidence, but cached files or binary presence alone do not prove active runtime visibility.

## Fallback

When native Engineer is absent, unusable, or its usability cannot be established, use the plugin root at:

`vendor/agentkit-engineer/`

The fallback plugin has its own Agent Plugins manifest and contains the exact 103 public stable-port Skill identities plus the 16 portable role definitions.

Do not expose native and fallback Skill libraries together by default.

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
2. expose native **or** fallback;
3. project fallback role files into native subagents when supported;
4. otherwise keep the same role semantics through one-shot or sequential execution.

If a fallback Skill depended on AgentKit-specific runtime machinery:

- preserve files-first plan semantics without requiring the CLI;
- map active-work state into ANGENT Continuity;
- use harness-native delegation when available;
- use proactive Continuity capture instead of requiring hooks;
- verify browser/render/provider/team lifecycle capability before relying on it.

Sequential degradation is valid only when it preserves the load-bearing workflow semantics. If live team lifecycle, interactive browser state, publication state, renderer behavior, or another capability is essential to the requested outcome, hard-stop or report the exact degraded boundary instead of pretending parity.

Fallback package readiness also requires the exact stable identity set; a matching directory count is not enough.
