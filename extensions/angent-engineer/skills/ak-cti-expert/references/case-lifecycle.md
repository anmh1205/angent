# CTI case lifecycle

## Acquire

Start from the intelligence question.

Collect evidence that can change the assessment.

Avoid broad personal-data harvesting.

## Enrich

Useful enrichment can include:
- infrastructure relationships;
- certificate/DNS history;
- public vulnerability/advisory context;
- organization-controlled repository exposure;
- public incident/ransomware/threat reports;
- user-supplied image/document metadata when authorized.

Every enrichment edge should preserve provenance.

## Assess

For each finding:
- what was observed;
- source reliability;
- confidence;
- freshness;
- affected asset/entity;
- potential impact;
- alternative explanation;
- verification needed.

Prioritize evidence quality over a synthetic numeric score.

## Deliver

Choose representation based on the consumer:
- operational defenders → actionable findings + mitigation;
- executives → impact/priority/gaps;
- investigators → evidence trail + timeline;
- automation → structured IOC/finding records.

Do not present inference as legal attribution.
