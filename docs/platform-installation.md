# ANGENT 1.6.x — platform installation

ANGENT has one maintained Core (`skills/`), an Engineer fallback source (`extensions/angent-engineer/`) and a visual frontend extension (`extensions/angent-frontend/`). `platforms/` contains host-specific bootstrap templates; `packages/` and `dist/` are generated, Git-ignored release outputs. Build from a Git checkout (or download the ready-made platform ZIPs and `SHA256SUMS` from the matching GitHub Release once published):

```bash
python3 scripts/build_packages.py --all
python3 -m unittest discover -s tests -p 'test_multi_packages.py' -v
```

Local agent, Gemini CLI and Claude Code bundles contain 115 discoverable Skills (12 Core + 102 Engineer + 1 ANGENT Frontend), including their references and portable support trees. The ChatGPT/OpenAI bundle differs deliberately: it exposes **only the ANGENT Root Skill**, with those other methods in its internal reference library. Do not use the raw root `skills/` checkout alone as the full ANGENT distribution: it contains only the 12 Core Skills.

## Local coding agents

Copy the **contents** of `packages/local-agent/` into the target project root. The `AGENTS.md` activates the universal cognitive standard and `.agents/skills/` exposes the 115 Skills on clients that recognize that standard. For a project with an existing `AGENTS.md`, copy the `.agents/` and `extensions/` directories, then merge ANGENT's small `AGENTS.md` guidance into the existing file without overwriting its project rules. Clients that do not support `.agents/skills/` require their native adapter.

## Gemini Apps Web (Gemini browser Skill upload)

Download `angent-gemini-web.zip` from the GitHub Release. On
`gemini.google.com`, open Customize > Skills > Upload and select that ZIP
directly. The ZIP has exactly one top-level `SKILL.md`, plus a generated
`references/INDEX.md`, the 12 Core, 102 Engineer and 1 Frontend Skill texts,
and 16 role definitions as *references*.

Gemini Web imports **one Skill** from this package. The nested library does
not become 115 separately discoverable Skills or 16 running subagents. You must
select/use the uploaded ANGENT Skill in Gemini Apps. The browser does not gain
filesystem persistence, native AgentKit, remote shell or external-action
scripting merely by importing reference files. Keep the original CLI targets
separate: `angent-gemini-skills.zip` contains a `.gemini/skills/` tree and
**does not work as a Gemini Web Skill upload**.

Reference: https://support.google.com/gemini/answer/17094296

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

Use `packages/openai-plugin/` or `dist/angent-openai-plugin.zip`. The compatibility builder `scripts/package_unified.py` produces `dist/angent-chatgpt.zip` with the same **single public `skills/angent/SKILL.md`**. The other eleven Core specialists, 102 Engineer fallback methods and one Frontend art-direction method are stored under `skills/angent/references/catalog/`, not as directly discoverable `skills/ak-*/SKILL.md` entries.

This package layout prevents ChatGPT from discovering bundled Engineer methods as independent plugin Skills. It does not force ChatGPT to select ANGENT in every conversation, and it does not suppress other installed plugins. Installing a new ZIP is separate from updating an already installed plugin; verify the actual provider catalog (exactly one public `skills/angent/SKILL.md`) with `scripts/verify_activation.py` and an actual provider observation.

## Package design and safety

- Source Skills are never rewritten for a host. Exact source bytes are copied into the target discovery path.
- Engineer fallback support paths are preserved, and source-only nested Engineer plugin metadata is not installable as a second plugin.
- The 16 portable roles remain under `extensions/angent-engineer/agents/`; two native-capable hosts also receive conservative role projections under `agents/` without unsupported memory/tool guarantees.
- Generated packages contain no symlinks and do not reference the repository source checkout at runtime.
- Build reproducibility, manifest consistency, complete catalog, metadata projection and compatibility with the legacy OpenAI ZIP are checked by CI.
- Do not blindly overlay bundles across an existing project. A project-specific `AGENTS.md`, `GEMINI.md` or `CLAUDE.md` must be preserved and merged.
- Structural validation cannot prove platform-specific model behavior, actual provider activation, native AgentKit availability or live subagent delegation. Run targeted live checks on each runtime before asserting those outcomes.

On each validated `main` push, the publish workflow creates a matching version tag and GitHub Release if that version has not already been tagged. The Release provides six platform-specific ZIPs, the compatible `angent-chatgpt.zip`, the single combined `angent-all-targets.zip`, and SHA256SUMS. The Actions artifact `angent-all-targets` includes the same outputs for inspection/download (30-day retention). Changes to `main` without a version bump do not replace a published tag. A personal ChatGPT plugin is not automatically updated when the GitHub Release changes; use its separately authorized plugin updater with `angent-openai-plugin.zip` and verify the installed version. Workspace GitHub marketplace sync is a different administration feature.

Tagged releases are published by `.github/workflows/publish-packages.yml`: the tag must exactly match the version in both OpenAI manifests, the full packaging checks run, and the workflow refuses to overwrite an existing release. Branch CI ZIP artifacts are short-lived candidates rather than a permanent distribution channel.

Versions and provider release IDs are obtained from active manifests/providers, not pinned in runtime instructions.
