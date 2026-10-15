---
name: ak-find-skills
description: Route to installed AgentKit/ANGENT capabilities or discover trustworthy external skills through real ecosystem tools with explicit install approval.
metadata: {port: angent-fallback, mode: adapted}
---

# Find Skills — Portable Fallback

Use when the user asks which Skill handles a job, whether a specialized capability exists, or to search for or install an external Skill. Stable Engineer 2.19.0 makes an essential distinction: **local routing** among installed AgentKit Skills vs **external discovery/installation** through the open Skills ecosystem. Do not merge these into generic keyword matching.

Read **references/discovery-and-install.md** for evidence, commands, trust and approval boundaries.

## Local capability routing

1. Clarify the task's outcome and required effect; honor a specifically selected Skill.
2. Inspect the **currently installed and callable** skills/catalogs and runtime tools, not just the vendored fallback directory.
3. Choose one most-specific primary capability per distinct intent. Secondary Skills may support a genuinely different subtask without an invented team pipeline.
4. Distinguish task shape: diagram source (Mermaid) vs finished vector artifact (Tech Graph) vs queryable code graph (Graphify/GKG), code reading (Scout/Explore) vs implementation (Cook/Frontend/Backend), advice (Advise) vs plan (Plan) vs risk scenario (Scenario).
5. Prefer usable native AgentKit when available; otherwise use the ANGENT portable replacement **with its recorded degraded limits**. If two candidate Skills overlap, choose based on ownership of the actual outcome and binding tool constraints, not branding.
6. Verify required runtime capability before recommending a command or promising a result.

## External skill discovery

When the user wants a **new or installable** Skill, search a connected real registry/catalog or the separate Skills CLI where available. An upstream example is `npx skills find <query>`; source listing is not installed capability. Inspect package/repository identity, permissions, scripts, instruction surface, trust, maintenance and requested scope before proposing installation. Never execute installers, globally modify skills or update existing ones without actual user authority.

When a skill is found, explain the relevant ability, verified source and platform support, meaningful risks, whether already connected, and the command or supported install flow. If none fits, say which catalogs were actually checked; direct problem solving may still be possible without a new Skill.

## Boundaries

Never call `npx skills add -g -y` or trigger network installation merely to finish a suggestion. Do not assert registry search, installed status or security review unless observed. When user asks to update installed skills, distinguish native AgentKit update from external Skills CLI update; protect user-owned colliding styles/files and respect the current runtime's update/approval mechanics.
