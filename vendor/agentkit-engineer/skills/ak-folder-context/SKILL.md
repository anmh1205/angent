---
name: ak-folder-context
description: Create or refine a nested AGENTS.md that adds durable conventions for one project subtree without duplicating the root instructions.
license: MIT
metadata: {port: angent-fallback, mode: adapted}
---

# Folder Context — Portable Fallback

Use when a subfolder has conventions, commands, architecture or constraints that differ meaningfully from the project root.

## Workflow

1. Read root and intermediate AGENTS.md files.
2. Inspect the target subtree.
3. Identify only durable instructions specific to that subtree.
4. Create/update the nearest nested AGENTS.md.
5. Avoid repeating root guidance unless needed to clarify an exception.
6. Verify the file does not contain task progress, secrets or transient memory.

Do not create harness-specific instruction files as independent sources of truth.

If a harness needs another filename, project/generate it from AGENTS.md through compatibility tooling.
