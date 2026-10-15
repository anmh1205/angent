# Documentation audit

Check:
- setup/install commands against actual config;
- architecture claims against source layout and interfaces;
- environment/config names;
- current deployment/runtime assumptions;
- dead links;
- duplicate authoritative instructions;
- AGENTS.md scope and stale conventions;
- examples that no longer compile/run;
- undocumented breaking behavior.

Classify documentation as current, stale, conflicting, missing or illustrative.

Prefer correction at the authoritative source over copying the same fix into many documents. But **do not delete necessary explanation merely because its technical facts can be discovered in code**: source is evidence; teaching the reader how components relate, why a boundary exists and how failures propagate is a different task. Distinguish redundant mutable facts from useful verified examples, stable conceptual models and operator procedures. Evaluate the resulting reader understanding, not just the number of references or removed paragraphs.
