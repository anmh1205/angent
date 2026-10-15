# Judgment for engineering journals

A journal exists so someone later can reconstruct **what was actually tried and learned** without mistaking the entry for current operational truth. The most valuable content is causal context and supporting evidence, not a transcript or a count of terminal commands.

## Select what deserves history

An incident, difficult root-cause discovery, consequential deployment decision, failed approach with a reusable constraint, or a major verified milestone can justify an entry. Routine progress generally belongs in the work tracker, a final answer or Continuity state. Explicit journal requests override this threshold.

Ask what would otherwise be lost: the initial symptom, assumptions that shaped the attempt, alternative hypotheses ruled out, a surprising observation, the deciding evidence and the unresolved consequence.

## Write from evidence

Narrate the relation between the problem, intervention and observation. Keep **facts** (logs, tests, patches, observed provider states) separate from **interpretation** (suspected mechanism or decision rationale). Link to stable commits, issues, checks and dates; if a source may change, record its revision. Describe rollback, mitigation and uncertainty rather than silently rewriting a failed attempt into a success.

Prefer a coherent technical narrative that another engineer can follow. A short entry can be complete; do not fill invented headings when the event does not support them. Remove secrets and irrelevant personal data.

## Persist, revisit, and learn

Use the existing project's journal location/document owner. If an authorized write is meaningful, use the host's actual editor/provider, avoid collisions or duplicate uncertain submissions, then read back. For retrieval, inspect the relevant historical entry and independently refresh any claim used to decide current work.

A journal is not an active-work checklist, an instruction source, a project-wide policy or a promoted lesson. If repeated incidents imply a working-method defect, ANGENT Learning may investigate and promote a supported causal principle separately.

## Calibration cases

- **Failed release:** record observed regression, affected version, attempted rollback and verified/unknown recovery status.
- **Routine one-line test fix:** a commit and test result may suffice without an additional journal.
- **Ambiguous external write:** record attempt and pending reconciliation, not a confirmed success.
- **Old journal citing an outdated API:** treat it as historical evidence and check the live API before acting.
