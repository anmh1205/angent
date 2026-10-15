# Root agent-context operation

Root AGENTS.md is a small set of imperative instructions that prevent specific costly agent actions. It is distinct from human docs and from task checkpoint/history.

For each line: (1) can the agent trivially discover it from files/config? (2) what wrong action does it prevent? (3) is it checkable? (4) does it contradict another instruction?

Keep mandatory toolchain, reliable test commands, expensive/forbidden operations, non-derivable gotchas, project-specific conventions and definition-of-done rules. Cut vague values, repeated README, module trees and dynamic progress. Mark audit blocks KEEP/CUT/MIGRATE and obtain approval for material deletions or rewrites.

Markdown guidance is not deterministic enforcement. Suggest host hooks/settings only after checking actual runtime support; do not silently change host enforcement files. Canonical portable AGENTS.md may have host-specific generated aliases, not divergent sources. Use `ak-folder-context` for nested folders.

Read back root plus nested instruction interactions after edits; never let outdated process memory impersonate the live task frontier.
