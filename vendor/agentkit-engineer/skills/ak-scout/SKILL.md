---
name: ak-scout
description: Fast codebase scouting using native search/inspection and optional delegated Explore workers when the active harness supports safe delegation.
license: MIT
metadata:
  author: agentkit
  port: angent-fallback
  upstream-generation: "2.12.0"
---

# Scout — Portable Fallback

Use this Skill to rapidly understand where relevant code lives and how the requested behavior crosses files/modules.

The fallback must work without AgentKit CLI, Claude-specific APIs, or any particular subagent implementation.

## Choose the smallest scouting mode

**Direct scouting** is the default when:
- the scope is narrow;
- one agent can search/read the relevant files cheaply;
- the runtime has no safe delegation surface;
- the user did not request parallel agents.

**Delegated scouting** is useful when:
- the scope spans many independent directories/modules;
- separate workers can inspect disjoint areas;
- the active harness exposes a real delegation/subagent capability;
- parallelism will reduce wall time or protect the main context.

Do not spawn workers merely because this Skill supports them.

Read `references/internal-scouting.md` for delegated work and `references/external-scouting.md` for broader/external discovery.

## Workflow

1. Restate the concrete scouting target: behavior, symbol, error, feature, interface, or file class.
2. Read applicable `AGENTS.md` before scanning a repository subtree.
3. Start with cheap structural evidence: filenames, symbols, imports, callsites, configs, tests, ownership boundaries.
4. Trace at least one relevant path through the code when the task depends on relationships rather than file presence.
5. Expand the search only when current evidence cannot explain the requested behavior.
6. If delegation is justified, partition by non-overlapping scope and give each worker an exact question plus expected evidence.
7. Synthesize findings into a compact map for the next owner.

## Evidence to return

Return:
- relevant files/modules;
- why each matters;
- key symbols/interfaces;
- observed ownership/data/control flow when material;
- unresolved ambiguity;
- suggested next read/probe.

Do not return a directory dump.

## Quality gates

A scout result is weak if it:
- lists files without explaining relationships;
- assumes the most obvious file owns the behavior;
- misses tests/config/schema that define the same behavior;
- fans out workers with overlapping scope;
- reports guesses as confirmed ownership.

## Delegation contract

When the harness supports delegated workers, give each worker only:
- target question;
- exact directory/file scope;
- project constraints from applicable AGENTS.md;
- expected evidence/artifact;
- stop condition.

Do not dump the full conversation into every worker.

## Fallback behavior

If delegation is unavailable or blocked, continue with main-agent search/read instead of failing the Skill.

If external search tooling is unavailable, use repository-native search and targeted reads.

The capability is **scouting**, not “spawn Explore”.
