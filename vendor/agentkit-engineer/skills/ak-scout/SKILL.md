---
name: ak-scout
description: Map the files, symbols, tests, configuration and relationships relevant to a bounded codebase question using read-only local evidence and optional explicitly permitted delegation/external probes.
license: MIT
metadata:
  author: agentkit
  port: angent-fallback
  baseline: "AgentKit Engineer 2.19.0"
---

# Scout — Portable Fallback

Use Scout for bounded reconnaissance: locate where behavior/configuration lives and return a compact relationship map without starting implementation or root-cause repair.

Read:
- `references/internal-scouting.md` for optional delegated Explore work;
- `references/external-scouting.md` for separately permitted external/broader probes.

## Choose another workflow when

- root-cause diagnosis is the goal → Debug;
- a concrete failure should be repaired → Fix;
- solution approaches are open → Brainstorm;
- an implementation roadmap is needed → Plan;
- known files should be changed → Cook.

## Input boundary

Define one bounded search target plus include/exclude directories/file types when material.

Default project-content behavior is read-only.

Delegation requires both:
- actual runtime capability;
- permission/interaction mode that allows it.

External provider probing is a separate data-sharing boundary and requires authorization for that scope.

## Workflow

1. Parse the concrete target: behavior, symbol, interface, config, error or file class.
2. Read applicable `AGENTS.md`.
3. Use cheap local evidence first: paths, symbols, imports/calls, configs, schemas, tests, ownership.
4. Trace at least one relevant path when relationships matter.
5. Expand only when current evidence cannot answer the bounded question.
6. If delegation is useful/allowed, assign non-overlapping directory/questions with explicit evidence output.
7. If external probing is explicitly allowed and necessary, send only the minimum non-secret scope and preserve provider/source boundaries.
8. Synthesize one concise map; deduplicate repeated paths/claims.
9. State excluded/timed-out/unconfirmed scope and unresolved questions.

## Optional stronger verification

When the active stable runtime exposes an "ultra"/multi-pass scout mode, it may run several independent verification passes. This is optional runtime capability, not required portable behavior.

Do not fake multi-agent/ultra execution on a harness that lacks it.

## Output

Return:
- relevant files/modules with why they matter;
- key symbols/interfaces;
- tests/config/schema associated with the behavior;
- ownership/data/control relations that were actually observed;
- important existing patterns the next workflow should preserve;
- coverage boundaries;
- unconfirmed points/unresolved questions.

A file list is not a causal diagnosis and is not proof of runtime behavior.

## Quality

Fail the scouting result if it:
- reports a directory dump instead of relevance;
- labels ownership from filename guesswork;
- omits obvious tests/config/schema in the bounded scope;
- treats worker summaries as ground truth without synthesis;
- broadens external data sharing without authority;
- turns read-only reconnaissance into implementation.
