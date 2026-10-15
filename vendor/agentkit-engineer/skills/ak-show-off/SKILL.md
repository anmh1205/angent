---
name: ak-show-off
description: Build preference-aware bilingual or single-language HTML showcases with proof-led narrative, responsive visuals, optional verified screenshot capture and explicitly authorized publication.
metadata: {port: angent-fallback, mode: degraded}
---

# Show Off — Portable Fallback

Use when the user wants to **present/showcase completed work** as a scrollable HTML story, demo or visuals for posts/articles, not ordinary documentation or proof of feature implementation. Stable Engineer 2.19.0 defines user-level preferences, a project-management checklist, frontend-design generation, optional AgentWiki publishing, viewport-specific screenshots and a browser review. Its Node preference/capture helpers and AgentWiki/browser runtime are **not bundled with this Markdown**, so visual/publishing parity is explicitly degraded.

## Preferences and scope

The pinned source's default workflow values were `screenshots=true`, `publishing=true`, `languages=["vi","en"]`. Treat them as **source defaults, not permission to publish**, share private work or run a browser. Honor explicit user instructions first, including 'no screenshots', 'local only', 'English/Vietnamese only', one-run overrides and preference reset. Native installs may store preferences under `$AGENTKIT_HOME/show-off/preferences.json` or a known override using `scripts/preferences.js`; use that mechanism only if actually available, requested and authorized. Do not claim persisted opt-outs from a missing helper or repeatedly ask for already known decisions.

## Plan and content ownership

In a native workflow, resolve preferences, then let Project Management create/mirror the dated plan and actual stage tasks (request, content, HTML, local review, optional capture, optional publish), preserving a shared output root. In portable fallback, reuse the project's existing authorized plan/frontier rather than inventing mandatory dated plan directories or mutating unrelated project state simply to prepare a visual artifact.

1. Confirm showcase subject, audience, real completed artifacts, confidentiality, style/brand and language preference.
2. Write source-grounded narrative with clear main proposition, 2–6 meaningfully separate sections, notable constraints, data references and cited external claims where available. Do not hallucinate results, metrics or feature completion.
3. Produce a self-contained HTML page with an effective introductory hero, cohesive hierarchy, purposeful motion/illustrations and suitable light/dark/system presentation. Bilingual output needs an actual legible toggle or deliberate parallel treatment; monolingual must not inherit unnecessary toggle text.
4. Ensure the project HTML is responsive and inspect critical content/viewport clipping at approximately 16:9, 9:16 and 1:1 sizes as relevant. Preserve Vietnamese glyph support where requested; avoid leaking credentials/private URLs in HTML, images and footnotes.
5. Screenshot capture, if enabled and actually available, should wait for fonts, images, CSS backgrounds and scroll-triggered reveals before each section export. Native helper `scripts/capture-sections.js` can generate horizontal/vertical/square captures where installed; a network screenshot service requires its own credentials, exposure and approval boundary.
6. If publishing is **explicitly authorized**, use an available reviewed provider/AgentWiki workflow, verify public reachability and honor requested destination. Local-only or no-publish settings categorically prohibit publication. Publishing cannot occur just because upstream default says `true`.

## Verify and deliver

Read back HTML source and generated files; test/open the actual page when runtime supports it, inspect representative viewport screenshots and verify media sizes. Distinguish created HTML, viewed/reviewed HTML, screenshots and public publication as separate effects. If a capture or publication path is missing, report the limitation without inventing its success.

No user-privileged credentials, unsolicited remote hosting, source-code changes or merge/branch operations are part of Show Off itself.
