---
name: ak-common
description: Internal-only shared conventions and support material for Engineer skills; never selected as a standalone user task.
metadata: {port: angent-fallback, mode: portable}
---

# Common — Portable Fallback

Stable Engineer 2.19.0 declares Common **internal-only** with model invocation disabled. It provides reusable conventions/resources to other skills rather than a user-invocable workflow. Load it only when another selected Skill explicitly needs its common material; never route a user's request to Common as an agent.

The upstream Common SKILL.md is a small index pointing to package-local support directories. Discover and load any actually bundled files rather than presuming scripts, references or resources were copied into this fallback.

## Shared integration boundaries

- Follow relevant AGENTS.md and the consuming repository's current instructions.
- Preserve ANGENT Contract/Reasoning ownership; shared helpers do not override skill-specific domain contracts.
- Prefer the real host's available tools, commands and schemas to upstream-specific assumed names or inactive support files.
- Distinguish read-only observation, proposed change, authorized effect and verified completion.
- For high-impact Git/system changes, preserve branch, file, credential, privacy and rollback boundaries.
- For long-running work, keep only decision-relevant Continuity state, evidence and next valid action.
- Return source-backed results without inventing executed scripts, live subagents, status, files or test passes.

Individual skills may require more restrictive safety rules. No shared generic helper should flatten their distinctions, introduce mandatory process ceremonies or silently weaken a destination's authority model.
