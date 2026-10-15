# Installed routing vs external skill discovery

This reference retains the two separate stable Engineer 2.19.0 workflows without bundling the Skills CLI or assuming package install rights.

## Installed Skill routing

If the user names a Skill, use it when available; otherwise name the capability boundary. For unnamed tasks, route to one primary domain owner and load only supporting roles for materially distinct steps. Relevant distinctions:

- UI implementation: frontend-development; reproducing mockups/screens: frontend-design; styling tokens/components: ui-styling; UX/product critique: ui-ux-pro-max.
- Code analysis: scout for bounded search, GKG for indexed go-to-definition/usages, Graphify for a persistent queryable relation graph, Repomix for a context snapshot.
- Browser testing: web-testing or agent-browser depending on requested actual browser effect; privileged profile work: chrome-profile with its explicit authorization.
- Document/diagram work: docs for owned project documentation; Mermaid v11 for Markdown-native graph syntax; Tech Graph for precise publish-ready SVG/PNG; preview for rendered viewing/presentation.
- Implementation vs decisions: advise for user-interview reframing; brainstorm for options; plan for implementation phases; cook for authorized code execution; test for tests; security/security-scan for their distinct review scopes.
- Project tracking: project-management; multi-plan view: plans-kanban; Git history effects: git/worktree/ship with explicit distinct authority.

This is a semantic hint list, not an assertion that each corresponding Skill is currently installed/usable. Runtime discovery and project instructions take priority.

## External Skills CLI

The upstream Skills CLI is an **independent** tool from AgentKit native `ak`. Source-version example operations are:
~~~bash
npx skills find react performance
npx skills add owner/repository@skill
npx skills check
npx skills update
~~~
Find/check are discovery operations but may access external services; add/update changes local skill state and requires authorization. Avoid implicit global `-g`, auto-confirm `-y` or fetch-and-execute package installation. Inspect current CLI help, expected changes, repository provenance, version pinning and installation scope before invoking any mutation.

For recommendations, communicate source URL/identity, applicability, dependencies/permissions, risks and the command the user can review. Installed/available is a stronger claim than discovered/listed. If a registry or CLI is unavailable, disclose that limitation rather than inventing result names.
