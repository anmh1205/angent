---
name: ak-folder-context
description: Create minimal subfolder AGENTS.md instructions only when durable subtree-specific constraints merit their cost.
license: MIT
metadata: {port: angent-fallback, mode: adapted}
---

# Folder Context — Portable Fallback

This skill is for subfolders, not root instructions or project documentation. Route root agent instruction to `ak-docs agent-context` and human docs to `ak-docs`.

## Workflow

1. Confirm the target is a subtree; read root and intermediate AGENTS.md, local files, source/config and any existing CLAUDE.md.
2. Apply a creation gate: static reference folders and discoverable conventions do not need instruction files.
3. Identify only durable scoped commands, constraints, locked decisions and non-obvious differences from parent rules. Never write secrets or transient task progress.
4. For a new file, conflicting authority or material rewrite, propose a grouped outline/diff before writing unless that specific change is already authorized.
5. Write nested AGENTS.md as the canonical portable source. If a runtime needs CLAUDE.md, use a symlink/generated alias or a clear pointer; never maintain independent conflicting copies.
6. Read back, verify ancestor consistency and preserve user edits. Re-read after subsequent user modifications; never revert them silently.

Do not invent policies or create files outside the approved subtree.
