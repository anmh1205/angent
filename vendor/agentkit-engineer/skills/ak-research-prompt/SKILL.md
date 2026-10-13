---
name: ak-research-prompt
description: Produce a self-contained research brief that another human or AI researcher can execute without hidden conversation context.
license: MIT
metadata: {port: angent-fallback, mode: portable}
---

# Research Prompt — Portable Fallback

A good research brief specifies the decision it must inform.

## Include

- background needed to understand the question;
- exact research questions;
- decision/acceptance criteria;
- version/platform/time boundaries;
- preferred source roles;
- known hypotheses or competing options;
- required evidence/experiments;
- exclusions;
- desired output format;
- how uncertainty/conflict should be represented.

Do not include irrelevant transcript history.

A successor should be able to execute the brief without asking what the original task meant.
