---
name: ak-repomix
description: Package bounded local/remote repositories for model context or audit using verified Repomix, with source, secret, format and token-budget checks.
metadata: {port: angent-fallback, mode: degraded}
---

# Repomix — Portable Fallback

Stable Engineer 2.19.0 Repomix packages selected code/repository content into AI-friendly **XML, Markdown, plain text or JSON** with Git-aware selection, token estimation, optional remote-repository fetching, comment removal, security scanning and support for scoped monorepo packs. It is **not** the same as repository search, and a hand-written excerpt is not full native parity.

## Native preflight and packaging

1. Confirm installed Repomix command/version or a trusted project-native invocation; do not run an installer or `npx` download implicitly.
2. Establish source (local repository/ref or user-authorized remote URL), exact change/version scope, intended reader/model, required output style, include/ignore patterns and sensitive/excluded paths.
3. Favor the smallest relevant folder/package scope. Honor `.gitignore`, a project Repomix ignore config and explicit exclusions for secrets, generated artifacts and irrelevant vendor trees. Avoid `--no-gitignore` and `--no-security-check` unless user intent and a safer alternative genuinely justify them.
4. Check active CLI help for supported formats and switches. Examples from stable upstream are `repomix --style markdown`, `--style json`, `--include`, `--remove-comments`, `--remote`, `--token-count-tree`, `-o` and `--skill-generate`; their syntax/capabilities are not guaranteed across versions.
5. Execute under the authorized network/file effects, then inspect actual output for format integrity, completeness/selection, unexpected sensitive material, token consumption and warnings. Built-in Secretlint is helpful but **not** proof no secrets leaked.
6. If packaging a remote repository, verify its URL, ref and confidentiality, and disclose remote-tool network use. Do not export private source to an external model without the required authority.

## Token and context management

Use observed per-file and total token metrics when available. Reserve space for other instructions, dialog, evidence and response within the **actual** active model context limit; never depend on a hard-coded historic model-limit table. Large repo snapshots may require package-scoped packs or targeted Scout/GKG search instead.

## Batch and fallback limits

The pinned AgentKit package includes a separate Python batch helper, manifest-style repository configuration and tests. They are **not present by implication** in this portable fallback; don't promise batch orchestration from a Markdown file.

When native Repomix is absent, assemble a small clearly marked **partial** snapshot only from exact authorized files, or use bounded source search if packaging is unnecessary. Report that native formatting/token counts/security scanner and remote fetch features were not exercised.

## Deliverable

Provide verified artifact path and format, source revision, included/excluded scope, token count **when measured**, security review status and limitations. Never fabricate an output path or use `--copy` to silently publish sensitive context to the clipboard.
