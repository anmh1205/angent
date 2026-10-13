---
name: ak-find-skills
description: Discover the best available Skill or capability for a requested task, preferring native AgentKit when usable and ANGENT fallback otherwise.
metadata: {port: angent-fallback, mode: adapted}
---

# Find Skills — Portable Fallback

Use when the user asks whether a capability exists, which Skill should be used, or how to extend the active agent.

## Workflow

1. Identify the capability/outcome, not just keywords.
2. Inspect the active capability catalog.
3. If native AgentKit is usable, prefer native Skill discovery.
4. Otherwise inspect ANGENT fallback Skills and installed harness tools/plugins.
5. Rank candidates by fit, dependencies, side effects and current usability.
6. Recommend the smallest sufficient capability.

Do not claim a Skill is available merely because a historical catalog mentions it.

If no capability fits, say so and recommend the smallest extension path.
