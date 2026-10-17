# Separate status dimensions for BA artifacts and shipped behavior

**Provenance:** Adapted from MIT Dev BA Kit / rules/status-lifecycle.md (Edward Ngo, 2026), https://github.com/nv-minh/dev-ba-kit. Status definitions must follow the actual stakeholder process and provider workflow.

## Distinct, non-equivalent dimensions

- **Document readiness:** draft, under review, approved, superseded, archived or the organization's accepted labels.
- **Decision validity:** unapproved hypothesis, accepted business decision, explicitly deferred, revoked or unknown.
- **Implementation:** not started, in progress, merged into a specific branch, verified against a real test environment.
- **Delivery:** deployed to a named environment, staged, enabled to users, rolled back or unknown.
- **Test evidence:** not specified, specified but not run, executed-pass, executed-fail, blocked or not applicable.

These fields must not be collapsed into one status. An approved SRS can describe an unimplemented feature; an issue marked Done may mean a task was merged but not deployed; a generated prototype may be runnable only as a simulation.

## Changing a status

Require an actual event or accepted decision, source/owner and revision. An editor setting frontmatter to approved does not establish an authorized stakeholder approval. A GitHub PR merge proves repository integration, not actual production rollout.

When the provider has its own workflow transitions, retrieve the allowed transitions before changing a status. Do not invent labels or auto-transition related Jira/Confluence pages because another status changed.

## Review recovery

If a review uncovers a contradictory BR or a real regression, preserve the previous accepted revision and record the new decision. Do not silently erase history or downgrade a shipped claim based only on a dated source file.

## Presentation

A concise table with requirements approval, implementation commit, tests and deployment is often more informative than a single green badge. Unknown observations remain unknown.

The status model informs BA reasoning; ANGENT Root/Execution own whether any provider mutation is in user scope.
