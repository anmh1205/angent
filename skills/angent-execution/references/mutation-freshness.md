# Mutation freshness

A mutation derived from inspected existing state is valid only while the assumptions that produced that delta still match the live target closely enough.

This is a semantic read→modify→write invariant, not a transaction engine.

## Mutation basis

When stale overwrite is plausible and consequential, preserve enough basis to know what the candidate was derived from:

- canonical target identity;
- observed version/revision/digest or another provider-native change token when available;
- relevant baseline subset/pointer;
- intended semantic delta;
- dependency assumptions;
- provider precondition mechanism when available;
- refresh/reconsideration condition.

Do not create a heavyweight basis object for trivial or inherently safe operations.

## Before write

For a mutation of existing canonical state:

1. resolve the actual target;
2. determine whether the candidate depends on an earlier snapshot/version;
3. when the provider supports a conditional write or expected-version token, use it;
4. otherwise refresh enough live state immediately before the effect when meaningful drift is plausible;
5. execute only while the mutation basis remains compatible.

Examples of provider mechanics include expected SHA/revision, ETag/If-Match-style preconditions, update-version fields, or equivalent compare-and-swap behavior. ANGENT defines the semantics; the harness/provider implements the mechanism.

## If the target changed

Do not blindly retry the same full replacement.

Classify the drift by dependency:

- **irrelevant/disjoint** — concurrent change does not affect the candidate's assumptions; rebase/apply the intended delta onto current state and revalidate affected checks;
- **overlapping/semantic conflict** — concurrent change touches the same fact, section, object, invariant or dependency; return to Reasoning before mutation;
- **already satisfied** — another actor already produced the requested endpoint; verify and avoid duplicate/redundant write;
- **unknown/insufficient comparison** — fail closed for the dependent mutation until enough state is recovered.

Preserve unrelated concurrent work.

## Conflict is evidence

A provider conflict/precondition failure establishes that the mutation basis is stale or incompatible with the live write boundary.

It does not automatically mean:
- the requested goal is impossible;
- the target is corrupted;
- the other writer is wrong;
- the old candidate should be force-applied.

Refresh, reconcile, and replan only the affected dependency closure.

## When a strict basis is unnecessary

Do not add ceremony when the operation is known to be safe without it, for example:
- creating a new uniquely identified object;
- append/commutative operations whose semantics preserve concurrent contributions;
- provider operations that already merge safely under known semantics;
- low-consequence writes where live drift cannot materially change correctness.

The burden scales with overwrite risk and consequence.

## Wait/resume boundary

A long wait, interruption, handoff, or other branch mutation can stale a mutation basis.

Before dependent replay/commit, integrate this with Continuity resume compatibility and current authority/observation checks.

## Completion

A successful transport response to a stale write is not a reliability win.

The requested semantic delta must be present on the current canonical target while unrelated concurrent changes remain preserved.
