---
name: ak-interview-docs
description: Elicit user-owned project vision and structured decisions through incremental, evidence-preserving document updates.
license: MIT
metadata: {port: angent-fallback, mode: adapted}
---

# Interview Docs — Portable Fallback

Use when user knowledge and explicit decisions—not code inspection or assistant proposals—are the document's authority. Use `ak-docs` for code-derived documentation and `ak-brainstorm` for generating options.

## Mode and ownership

- **Vision/decision:** inspect existing README and decision documents; record vision in its owner and only accepted decisions in project-approved ADR/decision format.
- **Structured document:** inspect nearby artifacts; build one user-authored principles, strategy, review or similar document without imposing rank or priority on unordered lists.
- If modes would change ownership, clarify only the material ambiguity. Do not create a new docs tree by default.

## Interview and write cycle

1. Recover prior answers and current docs; never repeat settled questions.
2. Ask focused questions singly for scoped documents, or in manageable groups for broad vision when the user permits. Avoid generic surveys.
3. Separate accepted decisions, tentative preferences and suggestions; preserve the user's language and intended order.
4. After each answer or complete decision, re-read the affected section and patch only authorized content, then read back before dependent questioning.
5. Keep unanswered topics explicit; do not invent content, constraints, architecture or priorities.
6. Continue until the user ends the interview. Preserve existing edits and never persist credentials or private data.

An interview is not an excuse to block an already-specified writing task with redundant questions.
