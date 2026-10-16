# Gemini Apps Web Skill adapter

Gemini Apps (gemini.google.com) uploads **one Skill** per ZIP. The ZIP root
must contain `SKILL.md`. This differs from Gemini CLI's `.gemini/skills/`
workspace layout and Gemini Extension's `gemini-extension.json`.

`scripts/build_packages.py` constructs `packages/gemini-web/` from the
canonical ANGENT root text and generates `references/INDEX.md`. Original
Core and Engineer Skill texts are bundled under `references/catalog/` while
Engineer role definitions are under `references/roles/`. The reference
material does not gain independent Skill discovery or native subagent
execution. The Web package must not claim file persistence, shell or
network-execution capabilities without active host evidence.

Users select `angent-gemini-web.zip` from Gemini Apps > Customize > Skills
> Upload. The browser importer requires a root Skill and a max 100 MB
payload. Google documentation:
https://support.google.com/gemini/answer/17094296

Do not edit generated `packages/`; Core and Engineer remain canonical in
`skills/` and `extensions/angent-engineer/`.
