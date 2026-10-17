# Resolve consequential open questions without forced interview loops

**Provenance:** Adapted from MIT Dev BA Kit / rules/resolve-oqs.md (Edward Ngo, 2026), https://github.com/nv-minh/dev-ba-kit. The method is portable and does not require a post-write hook.

## Collect questions with real context

Inspect the current and upstream accepted documents for explicit unresolved issues. Identify each question's source, affected requirement IDs, owner, decision deadline if genuine and consequence of leaving it open. Include conflicts found during research when they materially affect behavior.

Deduplicate equivalent questions without erasing source lineage. An unanswered question and a consciously deferred decision are different states.

## Prioritize by consequence

Clarify immediately when uncertainty would make a business promise, unsafe device action, personal-data policy, permission model, expensive integration or irreversible provider edit incorrect. For a cosmetic variation or optional future feature, retain an explicit assumption/deferred decision and continue the authorized work.

Ask only the smallest set of independent questions required for the next safe step. Do not force the user to answer every open question before an exploratory draft or ask the same question again if a known decision already exists.

## Record resolution

When an authorized stakeholder supplies a decision, preserve its actual wording, source/date, scope, affected FR/BR/AC and alternatives rejected if important. Do not silently label the question approved because a draft contains a suggested value.

When a question is deferred, record the condition and consequence of deferral, along with the next review trigger. Do not fabricate an answer to make the next diagram appear complete.

## Handoff

The downstream specialist should see which decisions are accepted, proposed, uncertain or blocked. A summary may include an exact decision table in existing documentation; no special global question database is required.

## Example

A rental operator might want to remotely stop a vehicle. The policy needs safety conditions, legal authorization, actor roles and release gates; a generic timeout value cannot resolve that question. A mock UI can be drafted, but live control must remain blocked pending an approved and tested policy.
