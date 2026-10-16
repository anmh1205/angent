# ANGENT 1.5.0 — platform installation

ANGENT has one maintained Core (`skills/`) and one Engineer fallback source (`extensions/angent-engineer/`). `platforms/` contains host-specific bootstrap templates; `packages/` and `dist/` are generated, Git-ignored release outputs. Build from a Git checkout:

```bash
python3 scripts/build_packages.py --all
python3 -m unittest discover -s tests -p 'test_multi_packages.py' -v
```

All five bundles contain the same 115 discoverable Skills, including their `references/`, `scripts/` and portable Engineer support tree. Do not use the raw root `skills/` checkout alone as the full ANGENT distribution: it contains only the 12 Core Skills.

## Local coding agents

Copy the **contents** of `packages/local-agent/` into the target project root. The `AGENTS.md` activates the universal cognitive standard and `.agents/skills/` exposes the 115 Skills on clients that recognize that standard. For a project with an existing `AGENTS.md`, copy the `.agents/` and `extensions/` directories, then merge ANGENT's small `AGENTS.md` guidance into the existing file without overwriting its project rules. Clients that do not support `.agents/skills/` require their native adapter.

## Gemini CLI workspace Skills

Copy `packages/gemini-skills/.gemini/` into the project root and merge `packages/gemini-skills/GEMINI.md` into its existing **project-root** `GEMINI.md`. If no such file exists, copy it to project root. This is a *workspace Skills* package rather than an Extension. Verify with `/skills list` and `/memory show`.

Gemini can also discover the Universal `.agents/skills/` alias. Do not install overlapping Universal and Gemini bundles into the same workspace.

Official reference: https://geminicli.com/docs/cli/using-agent-skills/

## Gemini CLI Extension

Use the directory `packages/gemini-extension/` containing `gemini-extension.json` as the local extension source:

```bash
gemini extensions install /absolute/path/to/packages/gemini-extension
```

Its `GEMINI.md` is loaded by the declared `contextFileName`. Its `skills/` and 16 conservative `agents/` role projections are self-contained within the package. Gemini subagent support is preview/version dependent; a role contract does not certify successful spawning.

Official reference: https://geminicli.com/docs/extensions/writing-extensions/

## Claude Code plugin

Load `packages/claude-code/` as a plugin directory, for example:

```bash
claude --plugin-dir /absolute/path/to/packages/claude-code
```

Its `.claude-plugin/plugin.json` exposes one plugin identity, `skills/` exposes ANGENT and portable Engineer, and `agents/` contains native-minimal role metadata plus the original role instructions.

**Important:** Claude Code does not automatically load a `CLAUDE.md` from the plugin root. If ANGENT's universal cognitive standard should be present in every conversation, merge `bootstrap/CLAUDE.md` into the target project's existing `CLAUDE.md`. Do not overwrite existing project instructions. Skills-only installation does not make this always-on guarantee.

Official reference: https://code.claude.com/docs/en/plugins

## ChatGPT and Codex

Use `packages/openai-plugin/` or `dist/angent-openai-plugin.zip`. The existing `scripts/package_unified.py` continues to create the compatible `dist/angent-chatgpt.zip` artifact. Both manifests share the same version and single ANGENT identity, not a second Engineer plugin. The current running ChatGPT/Codex plugin remains separate from Git source; installation and actual skill activation must be verified in that provider.

## Package design and safety

- Source Skills are never rewritten for a host. Exact source bytes are copied into the target discovery path.
- Engineer fallback support paths are preserved, and source-only nested Engineer plugin metadata is not installable as a second plugin.
- The 16 portable roles remain under `extensions/angent-engineer/agents/`; two native-capable hosts also receive conservative role projections under `agents/` without unsupported memory/tool guarantees.
- Generated packages contain no symlinks and do not reference the repository source checkout at runtime.
- Build reproducibility, manifest consistency, complete catalog, metadata projection and compatibility with the legacy OpenAI ZIP are checked by CI.
- Do not blindly overlay bundles across an existing project. A project-specific `AGENTS.md`, `GEMINI.md` or `CLAUDE.md` must be preserved and merged.
- Structural validation cannot prove platform-specific model behavior, actual provider activation, native AgentKit availability or live subagent delegation. Run targeted live checks on each runtime before asserting those outcomes.

Versions and provider release IDs are obtained from active manifests/providers, not pinned in runtime instructions.
