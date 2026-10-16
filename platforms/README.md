# Platform adapters

This directory contains only host-specific bootstrap or manifest templates. Canonical ANGENT Core Skills stay under `skills/`, while portable Engineer Skills and roles stay under `extensions/angent-engineer/`.

`scripts/build_packages.py` assembles platform-ready copies into the ignored `packages/` directory and deterministic ZIP releases into `dist/`. Never edit a generated package as an independent source of truth.

- `universal/AGENTS.md`: project-level instructions for interoperable local coding agents.
- `gemini/GEMINI.md`: persistent Gemini context for workspace copies and extensions.
- `claude/CLAUDE.md`: optional project bootstrap; Claude Code does **not** automatically load a plugin-root CLAUDE.md.
- `openai/AGENTS.md`: runtime entry for the single OpenAI Agent Plugin (ChatGPT/Codex).

The builder projects the same Skills into host-recognized paths and converts Engineer role frontmatter to conservative native subagent metadata only for Claude Code and Gemini Extension. This does not attest live agent execution or behavioral parity.
