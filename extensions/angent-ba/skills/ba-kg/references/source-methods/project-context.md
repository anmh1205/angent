# Relevant project context without a second memory system

**Provenance:** Adapted from MIT Dev BA Kit / rules/project-context.md (Edward Ngo, 2026), https://github.com/nv-minh/dev-ba-kit. ANGENT Root already handles task understanding and context continuity; this method supplies domain-specific evidence on demand.

## Two distinct discovery tasks

For an uncertain product idea, use opportunity discovery: buyer jobs, present substitutes, commercial feasibility, current market sources, falsifiable experiments and go/no-go decision. For an existing repository, use project discovery: actual actors, accepted product rules, code architecture and source revision. Do not use a source-code scan as a substitute for customer validation.

## What matters in a project profile

Capture paying customer versus user, business actors, permissions, meaningful glossary collisions, non-obvious domain rules, current integration boundaries, proposed versus deployed capabilities and unresolved decisions. Record exact sources for consequential claims. Avoid restating generic README facts when they do not help the current request.

A short overview plus optional links to accepted detailed documents is sufficient. There is no fixed mandatory location, always-loaded file, line limit, checksum or expiry-by-commit counter.

## Refresh policy

Retrieve or consult fresh information when the answer depends on live code, Jira issues, release state or changed stakeholder decisions. Compare source revisions; avoid carrying old statements as present facts. Unchanged, still relevant accepted business rules need not be rewritten on every call.

## Example

A fleet tracker may include GPS and CAN telemetry code while management rules about who may immobilize a vehicle remain undecided. Capture hardware observations and product policy separately. Escalate the unresolved control policy before claiming operator authority.

If asked to save a durable profile, adapt the existing project document with an authorized scoped diff. Do not interfere with the host's own memory or create a competing hidden store.
