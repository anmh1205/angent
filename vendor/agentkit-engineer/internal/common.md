# Engineer fallback common conventions

Internal support only; this file is not a discoverable Skill.

Fallback Engineer workflows share these conventions:

- read applicable AGENTS.md before project-specific work;
- preserve ANGENT Contract and Reasoning ownership;
- use the active harness capability instead of hard-coded provider/tool names when possible;
- degrade explicitly or block when a required capability is absent;
- use Continuity for long-running work and ambiguous effects;
- prefer project-native commands, stack and configuration;
- bind consequential effects to current authority;
- do not claim completion from intermediate tool success;
- do not expose secrets in reports or handoffs;
- return evidence/artifact pointers instead of full transcripts.

Individual Skills may impose stricter domain rules.

This internal convention file is intentionally outside `skills/` so it cannot be discovered as a user workflow.
