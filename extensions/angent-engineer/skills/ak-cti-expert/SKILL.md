---
name: ak-cti-expert
description: Conduct authorized defensive CTI and OSINT investigations through AEAD case lifecycle, documented collection gaps and source-backed intelligence reporting.
metadata: {port: angent-fallback, mode: degraded}
---

# CTI Expert — Portable Fallback

Stable Engineer 2.19.0 CTI Expert is a broad source-backed **Acquire → Enrich → Assess → Deliver (AEAD)** investigation workflow. The upstream bundle includes over a hundred specialized support documents and commands for domains, threat feeds, public incidents, infrastructure, forensics and entity relations. This fallback retains case reasoning and risk boundaries, **not** full bundled collection/automation coverage.

Read `references/entity-provenance.md`, `references/case-lifecycle.md` and `references/case-state.md`. Resolve actual sources, permissions and jurisdiction before active collection.

## Case intake and evidence

Define a legitimate defensive scope: organization-owned exposure, public threat indicators, security advisories, published breach reporting, malware campaigns, vulnerable software versions or authorized incident artifacts. Record case ID, target class, collection window, user authorization, retention/handling constraints and decision question.

**Acquire** only permitted evidence using official security feeds, public records, advisory sources or authorized connector/browser access. Typical categories are DNS/certificate history, CVEs and affected versions, hosting/domain metadata, published hashes/IOCs, code/repo exposure and incidents. Upstream `/case`, `/sweep`, `/query` and targeted subcommands describe workflow intents, not callable portable commands.

**Enrich** relevant links with clear entity type, relation, observed timestamp and confidence. Two accounts/domains sharing a string does not establish a person/organization match. Avoid mass collection of private people, credentials, leaked datasets, direct targeted enumeration or covert tracking.

**Assess** reliability, independent corroboration, temporal validity, alternate explanations, true exploitability/context and severity. Explicitly distinguish observed vulnerability from exploitable deployment. Missing a JavaScript-heavy page/browser/paid feed is a coverage gap, not proof that no evidence exists.

**Deliver** a bounded brief, IOC sheet, timeline, exposure assessment or actionable defensive report. Each material claim links to source, capture time and confidence; redact secrets and unnecessary identifiers. Keep raw evidence under approved access/retention policy. Document gaps, false-positive checks, detection/remediation candidates and what follow-up evidence would change the finding.

## Mode and authority

A user-supplied `--yolo` shortcut may reduce benign interview overhead in the native workflow; it does **not** authorize intrusive scanning, mass personal-data aggregation, credential access or security boundary circumvention. No command inferred from the original CTI catalog becomes automatically executable in this portable skill.

When the user requests a persistent workspace/export, use a real authorized file tool and verify output. Do not claim a DOCX or rendered case report was generated just because the native workflow normally produces one.

**Capability:** VERIFIED_DEGRADED — primary defensive reasoning and provenance survive, but specialist collector/runtime/reference parity has not been established.
