# Collaboration state

Collaboration state captures the task-relevant way ANGENT should work with the user. It exists because two tasks with the same artifact and endpoint may require different collaboration behavior.

It is semantic state, not a new owner, persistent profile, personality model, or permission system.

## What belongs here

Carry only dimensions that can change the current work:

- **interaction mode** — for example answer-only, research/report-before-edit, audit-only, explanation-first, autonomous end-to-end, verify-and-fix, or another mode evidenced by the task;
- **initiative expectation** — how far ANGENT should proceed without routine confirmation when authority is already clear;
- **evidence expectation** — what degree or kind of grounding/verification the user currently expects;
- **explanation expectation** — concise decision support, deep teaching, implementation-oriented reasoning, or another relevant communication job;
- **progress/checkpoint expectation** — when visible updates or durable state matter;
- **working-method mechanisms** — promoted Learning mechanisms about how this class of work succeeds or fails; when one materially changes current behavior, keep its pointer plus the applicability basis/effect needed to distinguish retrieval from actual activation;
- **task-scoped exceptions** — temporary deviations from broader patterns;
- **provenance and confidence** — whether each element is explicit, accepted from earlier task state, or inferred.

Use only the fields that matter.

## What does not belong here

Do not store:

- a broad personality sketch;
- keyword-level style likes/dislikes detached from mechanism;
- every repeated user phrase;
- project facts that belong to project memory;
- active obligations that belong to Contract;
- permissions or authority that the current instruction did not grant;
- full historical transcripts.

A pattern such as “use Mermaid often” is weak collaboration state. A mechanism such as “for a multi-stage technical relation, prefer a representation that exposes the relation instead of adding a diagram by quota” belongs to Learning and may be activated through collaboration state when applicable.

## Precedence

Use this order:

1. newest explicit task instruction;
2. still-active task-specific collaboration decisions;
3. applicable promoted working-method mechanisms;
4. cautious inference from repeated evidence.

An inferred mode must yield immediately to a conflicting current instruction.

## Interaction mode is not authority

“Autonomous end-to-end” can mean continue through ordinary reversible steps without asking repeatedly. It does not authorize a destructive or external effect outside the Contract.

Likewise, “audit-only” constrains task behavior even when the harness technically supports writes.

## Durability

Task-scoped collaboration state may be referenced by Continuity when resume correctness depends on it.

Stable cross-task working methods are promoted by Learning as causal mechanisms, not copied wholesale into a permanent user profile.

## Resume

On resume, reconstruct collaboration state from current instruction first, then durable task state and applicable Learning. Do not blindly restore a historical mode when the new turn changes how the user wants to work.
