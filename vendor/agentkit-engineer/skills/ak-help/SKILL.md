---
name: ak-help
description: Discover the currently available Engineer capability that best fits a requested outcome and give the exact active-runtime route without relying on a stale remembered catalog.
metadata: {port: angent-fallback, mode: adapted}
---

# Help — Portable Fallback

Use when the user knows the outcome but not the correct Skill/capability.

## Discovery authority

The live installed/active catalog is the authority for availability.

For ANGENT fallback:
1. inspect the active fallback Skill discovery surface when the harness exposes it;
2. otherwise inspect the fallback `skills/` tree/frontmatter;
3. use `STABLE_CATALOG.json` as package-provenance/expected-identity evidence, not as proof that a Skill is active in this runtime.

Do not recommend from memory merely because a name existed in an older port.

## Workflow

1. Restate the desired outcome and authority boundary.
2. Distinguish Skill workflow from CLI/provider/tool capability.
3. Discover current candidates.
4. Remove candidates that are unavailable in the active scope/runtime.
5. Recommend the smallest specific route that owns the outcome.
6. When CLI syntax matters, inspect current CLI help rather than reconstructing flags from prose.
7. If a requested identity is retired, use `COMPATIBILITY.md` and state the current route.

Do not dump the complete 103-Skill inventory unless the user explicitly asks for it.

Help does not install, invoke, mutate, publish, or deploy on behalf of the recommended workflow.
