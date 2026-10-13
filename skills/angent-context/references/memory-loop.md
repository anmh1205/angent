# Memory loop

This memory model is for knowledge that should survive sessions. It is distinct from AGENTS.md and Continuity.

## Scopes

- **user/global memory** — durable preferences/context across projects;
- **project memory** — architecture facts, conventions, recurring project knowledge;
- **learning memory** — promoted causal mechanisms owned by Learning.

Active task frontier belongs to Continuity.

## Candidate capture

Capture a candidate when information is likely to matter again: stable user preference, confirmed project fact, accepted durable project decision, or recurring context that would otherwise be rediscovered.

Do not persist confidential or transient content merely because it appeared in context. Prefer a source pointer when copied content is unnecessary.

Do not interrupt the main task just to maintain memory.

## Synthesis

Memory must not be append-only.

When a candidate overlaps an existing topic:

1. retrieve the current compact entry;
2. compare scope and provenance;
3. determine whether the candidate confirms, refines, supersedes or conflicts;
4. write one synthesized compact entry when justified;
5. preserve contested status when evidence is insufficient;
6. keep source/history pointers when useful.

The deterministic storage layer does **not** perform this semantic merge. Context does.

## Authority

Current explicit user correction outranks inferred preference.

Current project source can supersede stale project memory.

Memory cannot grant authorization or override a newer task-specific instruction.

## Retrieval

Retrieve only memories relevant to the current task/decision.

Use topic prefixes/status to discover candidate entries before loading the full store. Prefer exact-topic lookup when the topic is known. Ignore superseded entries unless historical conflict matters.

Raw session logs, journals and archived chats may be searched when compact memory is insufficient; they are evidence, not default prompt context.

## Local file backend

For local harnesses, `scripts/memory_store.py` provides a small optional persistence backend.

Default locations:

- project memory: `<project>/.angent/runtime/memory/project.json`;
- user memory: `${ANGENT_HOME:-~/.angent}/memory/user.json`;
- project Learning: `<project>/.angent/runtime/learning/mechanisms.json`;
- user/global Learning: `${ANGENT_HOME:-~/.angent}/learning/mechanisms.json`.

Use `learning-project` or `learning-user` only for promoted/reopened/retired Learning mechanisms. Do not mix them into ordinary project/user memory merely because the same backend is used.

The script provides topic-scoped entries, prefix/status discovery, provenance pointers, status, a store revision and compare-and-swap writes.

A writer reads the current revision and passes `--expected-revision` when updating. Concurrent stale writers receive a conflict instead of silently overwriting newer memory.

This backend is storage, not a replacement for Context reasoning.

Do not persist credentials, tokens, cookies, private keys or unrelated sensitive data. The local backend restricts file permissions where the platform allows it, but it is not an encrypted secret store.

## Maintenance

Consolidation can occur at meaningful work boundaries, compaction, handoff, task completion or available idle/cleanup hooks.

A missing hook must not disable the memory model.