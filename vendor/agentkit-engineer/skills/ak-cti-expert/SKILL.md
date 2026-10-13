---
name: ak-cti-expert
description: Conduct authorized cyber-threat-intelligence and public-source OSINT cases through acquire, enrich, assess and deliver phases with evidence provenance and privacy boundaries.
metadata: {port: angent-fallback, mode: adapted}
---

# CTI Expert — Portable Fallback

Use for defensive threat intelligence, organization-owned exposure review, vulnerability intelligence and lawful public-source investigations.

Do not use this Skill to stalk private individuals, obtain credentials, bypass access controls or perform intrusive access.

## Load progressively

- `references/entity-provenance.md` — identity/entity resolution and source confidence.
- `references/case-lifecycle.md` — acquire → enrich → assess → deliver.
- `references/case-state.md` — durable findings, timeline and resume semantics.

## Case lifecycle

### Acquire

Collect only evidence relevant to the authorized intelligence question.

Prefer public/official/organization-owned sources.

Record source URL/system, observation time and collection limitation.

### Enrich

Expand only from evidence-backed leads.

Correlate domains, infrastructure, identifiers, vulnerabilities or organizations conservatively.

Do not turn similarity into identity.

### Assess

Evaluate:
- reliability/provenance;
- confidence;
- temporal freshness;
- alternative explanations;
- exposure/impact;
- collection gaps.

For vulnerability intelligence bind claims to affected version/product and source.

### Deliver

Produce the smallest intelligence product needed:
- short brief;
- detailed report;
- timeline;
- IOC/exposure list;
- defensive recommendations;
- machine-readable findings when requested.

Separate observed fact, inference and unknown.

## Tool routing

Use the strongest authorized collection surface available:
- current web search/fetch;
- browser automation for JavaScript-heavy public pages;
- official APIs/feeds if already available;
- local files/evidence supplied by the user.

A missing collection tool is a coverage gap, not permission to bypass it.

## Privacy and security

Minimize personal data.

Never persist secrets, credentials or unrelated sensitive personal information into case state/reports.

Do not perform breach credential retrieval, invasive account enumeration or covert monitoring.

## Output

State:
- scope/question;
- key findings with provenance/confidence;
- assessed relationships;
- timeline when material;
- gaps/blind spots;
- defensive actions;
- what remains unverified.
