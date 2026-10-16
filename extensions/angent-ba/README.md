# ANGENT Business Analysis Kit

Independent implementation of **55 portable specialist Skills** matching the publicly described *categories of work* in AI4BA BA-Kit. No proprietary AI4BA skill source, templates or licensing rights are claimed. These are original ANGENT instructions, not a rebranded BA-Kit distribution.

ANGENT 2.0 Hub discovers all methods through `extension.json`. On OpenAI/Gemini Web the methods appear under the single ANGENT Root reference library; other targets project portable Skills into their own discovery paths.

The source methods are backed by a canonical evidence/traceability model in `skills/ba-kg/references/operating-model.md`, individually authored template starters and a constraint/rules library. Stronger artifact integrity checks live in `scripts/validate_artifacts.py` and `scripts/change_impact.py`; host environments without filesystem/CLI cannot claim to run them.

Scope: discovery; requirements; eleven modeling formats; backlog; interactive design; API analysis; testing; QA; handoff. The exact output format and real provider side effects require the relevant native tools. These instructions are *methods*, not assertions that Bruno/Figma/Jira/Confluence ran.

## Example path

`ba-brainstorm` → `ba-srs` → `ba-user-flow` / `ba-sequence` → `ba-userstory` / `ba-ac` → `ba-test-checklist` → `ba-test-cases` → `ba-gap`. Skip steps when the accepted artifact already exists. Scope changes go through `ba-cr` and provider writes through ANGENT Execution.
