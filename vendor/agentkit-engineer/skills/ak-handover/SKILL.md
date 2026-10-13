---
name: ak-handover
description: Capture a portable handoff and dispatch one bounded continuation job to a selected agent/runtime, with sequential role fallback when delegation is unavailable.
license: MIT
metadata: {port: angent-fallback, mode: adapted}
---

# Handover — Portable Fallback

Handover composes **Handoff + one bounded dispatch**.

It is not a general orchestration loop.

## Inputs

Require:
- current Continuity frontier or validated handoff artifact;
- selected role/agent intent;
- one bounded next job;
- scope / writable ownership;
- acceptance evidence;
- allowed effects;
- stop/replan condition.

## Workflow

1. Create or refresh the Handoff view from ANGENT Continuity.
2. Validate that referenced branch/files/provider/artifacts still exist when freshness matters.
3. Redact secrets and unrelated private data.
4. Discover whether the requested role/runtime is actually available now.
5. Build a small job contract from the handoff rather than copying the entire transcript.
6. Confirm write/effect authority before dispatch.
7. If delegation is available, dispatch exactly the bounded job.
8. If delegation is unavailable but the main agent can safely perform the same role, continue sequentially with the same contract.
9. Reconcile returned evidence/effects into the parent Continuity frontier.

## Failure handling

- runtime unavailable → do not pretend dispatch happened; use a semantically equivalent permitted route or report the gap;
- handoff stale → refresh/reconcile before execution;
- response lost after a consequential effect → inspect authoritative state before retrying;
- worker blocked → preserve its evidence and return the blocker rather than repeatedly resending the same job.

Do not silently switch to a more privileged runtime or broader write scope.

## Boundaries

Do not launch a broad autonomous mission from Handover.

A handoff never grants new authorization.

Handover ends after one bounded continuation result has been reconciled.
