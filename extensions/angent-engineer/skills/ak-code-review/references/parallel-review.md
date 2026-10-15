# Parallel review

Multiple reviewers are useful when the review can be partitioned into independent scopes.

## Good partitions

- backend vs frontend;
- independent packages/services;
- security-specific pass plus correctness pass when both are substantial;
- separate migration/data path vs application behavior.

## Poor partitions

- several reviewers reading the same diff with no distinct question;
- scopes that all depend on one unresolved requirement;
- parallel reviewers that will produce duplicate findings and no synthesis owner.

## Worker brief

Give each reviewer:
- exact scope;
- requirements/AGENTS.md relevant to that scope;
- specific risk/question;
- expected finding format;
- no-write rule unless explicitly authorized.

## Synthesis

Join findings before fixes.

Deduplicate shared root causes and distinguish genuinely independent confirmation from repeated reasoning over the same source.

If the harness has no safe delegation, perform the passes sequentially.
