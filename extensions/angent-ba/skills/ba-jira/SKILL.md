---
name: ba-jira
description: ANGENT BA specialist for jira with source evidence, host authorization and real tool boundaries.
---

# Jira synchronization of accepted BA user stories
**Source:** Maintained adaptation of the MIT Dev BA Kit by Edward Ngo (2026), https://github.com/nv-minh/dev-ba-kit/blob/main/skills/jira/SKILL.md. ANGENT Root/Core retains final authority.



## What is authoritative

Requirements, business rules and accepted user stories are project product decisions; Jira is an execution and collaboration system. ANGENT Root owns intent, source selection and permissions. BA resolves the FR/BR/AC-to-US mapping. Execution performs actual provider writes; Quality reads them back.

## Source-driven workflow

1. Read the current accepted story index, US, AC and linked FR/BR with their source revision. Do not push unreviewed drafts or assume every story needs a Jira issue.
2. Discover the actual accessible Jira site/project, issue types, field requirements and permissions using the connected Atlassian provider. Never hardcode tenant IDs or invent keys.
3. Map each US to an existing issue using an authoritative Jira key or a stable US ID in issue metadata/description. Search provider issues first; a matching title alone does not establish identity.
4. Compare the existing Jira issue and accepted story line by line. Prepare a scoped create/update/no-op proposal with source IDs, actual issue keys, role/access restrictions, clear acceptance criteria and changed text only.
5. If stakeholder requirements and Jira disagree, preserve both witnesses, report their revisions and request a resolution rather than making Jira override the SRS.
6. Check current authorization and provider permissions before writing. An explicit user instruction to implement/sync an approved scope authorizes its relevant writes; do not add arbitrary ceremony, but never expand scope silently.
7. Execute only verified create/update actions. Before retrying uncertain writes, search/read Jira to avoid creating duplicate tickets. Never fabricate a successful key.
8. Read the provider result back: project, key, summary, AC, scope and status. Record confirmed versus uncertain effects. Where a project already maintains a story index, use the authorized file workflow to add returned keys without rewriting unrelated rows.
9. For pulling issue status, distinguish engineering progress from requirement approval. Resolve local status labels against the actual Jira workflow, never guess "In Progress" equals accepted.
10. Summarize counts and direct issue links, source revision, omissions, conflicts and remaining decisions.

## Idempotency and state

Use the existing story-index jira-key column or Jira issue metadata as a stable mapping; no hidden .claude/state/atlassian/sync-state.yaml, checkpoint or second sync database. Compare live issue versions before concurrent edits; fail safely if the provider lacks the ability to preserve changes or read back.

## Example

US-FLEET-012 may require a rental operator to see only authorized vehicles. Jira can carry approved FR/AC and implementation work, but an issue marked Done does not prove that all live authorization paths were tested. This is an illustrative story, not a real Jira key.

When Atlassian access is unavailable, return a reviewable issue mapping and report zero confirmed external writes.
