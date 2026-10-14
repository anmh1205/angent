---
name: ak-research-prompt
description: Author a standalone decision-ready research assignment, not research findings, with source and uncertainty requirements.
license: MIT
metadata: {port: angent-fallback, mode: adapted}
---

# Research Prompt — Portable Fallback

This skill writes a brief for another researcher. If the user wants actual findings now, route to the research workflow.

## Contract

1. Recover project context, audience, decision, timeline when supplied, prior facts and constraints; avoid hidden dependence on the originating chat.
2. Express one controlling question and three to six scoped subquestions, without unrelated missions.
3. Require primary sources first (official docs, repository code, release notes, standards, papers, filings), and treat forums as weak corroboration.
4. Distinguish confirmed facts, inference, uncertainty and conflicting sources; include a gap round for contradictions and single-source claims.
5. Require each finding to include a precise claim, source URL/path, version/date applicability and one-line decision relevance; request one consolidated Markdown result.
6. When invoked in the upstream-compatible research-prompt mode, return exactly one self-contained paragraph without heading or separate deliverable. Honor a user's explicitly requested alternate brief structure.

Do not invent evidence or embed inaccessible private links, credentials or unnecessary personal data.
