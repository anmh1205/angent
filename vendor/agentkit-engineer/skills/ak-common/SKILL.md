---
name: ak-common
description: Shared fallback conventions for Engineer Skills; internal-only support, not a user workflow.
metadata: {port: angent-fallback, mode: adapted}
---

# Common — Portable Fallback

Shared rules for fallback Engineer Skills:

- read applicable AGENTS.md before project-specific work;
- preserve ANGENT Contract and Reasoning ownership;
- use native harness capability instead of hard-coded tool names when possible;
- degrade explicitly when a capability is absent;
- use Continuity for long-running work and ambiguous effects;
- prefer project-native commands/configuration;
- do not claim completion from intermediate tool success;
- do not expose secrets in reports/handoffs;
- return evidence/artifact pointers instead of full transcripts.

Individual Skills may add stricter domain rules.
