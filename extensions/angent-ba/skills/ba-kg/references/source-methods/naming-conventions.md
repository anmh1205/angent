# Stable artifact identity and source-link conventions

**Provenance:** Adapted from MIT Dev BA Kit / rules/naming-conventions.md (Edward Ngo, 2026), https://github.com/nv-minh/dev-ba-kit. Existing project naming and accepted IDs override illustrative defaults.

## Identity versus filename

A source requirement ID, a project filename, a Jira issue key and a Figma node ID identify different things. Maintain their explicit mapping when needed. Renaming a Markdown file is not a reason to change a stable FR/BR/TC identifier; conversely, a same-named screen across features is not guaranteed to be the same design node.

For new project-local file slugs, prefer lowercase ASCII kebab-case when there is no established naming standard. Check collisions on case-insensitive filesystems and reserved names before writing. Do not automatically rewrite user repositories to match this suggestion.

## Source-aligned identifier families

- UN identifies a user need; BO an objective; CAP a product capability.
- FR, NFR and BR identify behavior, quality and business policy; E identifies an error contract.
- UC and US refer to actor goals and deliverable slices; AC defines observable acceptance.
- CHK is a coverage question; TC is a concrete test case. Its source check may be present even if the test has never run.
- CR is a change decision/record, not an implicit requirement approval.

The specific suffix pattern belongs to the existing product. Avoid reusing an ID for a different semantic statement. Document superseded IDs when the decision truly changes; do not destroy historical references.

## Actual links

Use relative Markdown links only when the target is a real project file; use stable IDs in content tables and provider URLs only when retrieved from actual systems. Wikilinks are acceptable if the project's renderer supports them, but ANGENT's portable Markdown output cannot assume an Obsidian resolver.

On source-to-code mapping, pin full repository commit and path/line witness before describing observed implementation. On BA-to-Figma mapping, keep screen ID and real Figma frame/node ID distinct.

## Scope-sensitive folder names

Project-wide strategy, feature SRS, API contracts and test evidence may have different locations. Prefer the user's established layout. ANGENT does not require fixed product/srs/test folders, a special root changelog file, a shadow knowledge graph or automatic version checkpoints.

## Acceptance

The same accepted ID should mean the same thing across the SRS, graph, test source, story index and provider mapping; unresolved or duplicated links must be visible. A matching filename is not sufficient semantic proof.
