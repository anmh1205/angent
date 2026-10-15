# Floor and mechanical constraints

## Floor

Before answering a deceptively simple or high-rigor task, check:

1. **Goal** — what final state does the user actually need?
2. **Follow-through** — if they do exactly what you propose, does that final state hold?
3. **Unused detail** — is a seemingly small detail in the request actually load-bearing?

If the apparent easy answer fails one of these, increase reasoning depth.

## Mechanical constraint loop

For exact output constraints—strict JSON/schema, character/word counts, required/banned symbols, positional patterns:

1. turn the requirement into a concrete test;
2. draft;
3. verify mechanically with a tool/script when possible;
4. repair;
5. rerun the same test;
6. deliver the exact verified output without post-check editing.

Do not “verify” a surface constraint by casually rereading the text.
