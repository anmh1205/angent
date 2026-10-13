# Context degradation

When an agent gets worse over a long task, distinguish causes.

Possible mechanisms:
- stale instruction still competing with newer state;
- duplicated sources of truth;
- important constraints buried among low-value history;
- lossy compaction removed decisive detail;
- memory injected outside its valid scope;
- contradictory tool/Skill descriptions;
- too many unrelated artifacts loaded together;
- specialist work returned verbose transcripts instead of evidence/artifacts.

## Diagnosis

Use controlled comparison where practical:
- minimal current context vs full history;
- with vs without suspected memory;
- authoritative artifact only vs summaries;
- isolated specialist vs shared full context.

Fix the causal source instead of simply shortening everything.
