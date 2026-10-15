---
name: ak-journal
description: Select, investigate and preserve meaningful chronological engineering evidence as a technical journal, without confusing it with active work state or general memory.
metadata: {port: angent-fallback, mode: adapted}
---

# Journal — Engineering history as evidence

Use this Skill to help a later reader understand **what happened, why a decision was made, what was observed, and what remains unresolved**. It is not a log of every action or a mandatory completion ritual.

Read only the relevant references:
- `references/journal-semantics.md` — content/authority boundary.
- `references/incident-entry.md` — causal record for difficult failures.
- `references/using-journals.md` — retrospective retrieval and validity.
- `references/journal-judgement.md` — decide when to record, how to compose and how to reuse evidence.

## Decide whether a journal is useful

Record consequential attempts, incidents, failures that could recur, discoveries that explain a decision, or milestones where provenance and verification matter. If the user explicitly requests a journal, follow that request. Otherwise do not create one simply because a workflow ended; a short user answer or a Continuity update may be the correct artifact.

Start from the actual work and observations, not a generic template. Distinguish intended result, attempted action, observed outcome and inferred cause. Link commits, tests, issues, design choices and source versions; qualify stale or uncertain conclusions. A failed attempt is still worthwhile history, but must not be reported as successful.

## Preserve and retrieve

Choose the existing project journal/document owner; do not impose `plans/journals/` on a remote repository or a project already using another store. Author a readable entry and, when the user's authority and a real host file/editor tool permit, persist it and read it back. Avoid overwriting entries or duplicating an ambiguous write. For history search, inspect recorded entries read-only and verify time-sensitive claims before reusing them.

A journal is **historical evidence**, not the active Continuity frontier, the current project contract, a global user memory or a promoted Learning mechanism. Promote a reusable working lesson only after independent causal review; otherwise leave the observation in its original dated context.

Publication to social channels, a configured AgentKit store or another external system is a distinct provider effect requiring specific capability and authorization. Do not claim it occurred merely because an entry was written.
