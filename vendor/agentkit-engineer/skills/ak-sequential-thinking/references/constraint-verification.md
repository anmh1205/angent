# Constraint verification

For hard constraints such as:
- exact item/word/character counts;
- banned tokens;
- strict JSON/schema;
- required ordering;
- formatting grammar;
- mathematical invariants;

verify mechanically when possible.

Do not rely on “looks correct”.

When a constraint conflicts with the requested semantic outcome, surface the conflict rather than silently breaking one.
