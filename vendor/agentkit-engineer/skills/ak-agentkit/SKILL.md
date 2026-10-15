---
name: ak-agentkit
description: Route a multi-step or ambiguous engineering request to the smallest useful combination of Engineer Skills and Agents.
metadata: {port: angent-fallback, mode: adapted}
---

# Engineer Router — Portable Fallback

This Skill provides Engineer routing when native AgentKit is unavailable.

It does not replace ANGENT Root or Reasoning.

Read `references/routing-protocol.md` for selection/delegation. For tasks described using AgentKit command vocabulary, read `references/outcome-routing.md`: identify the useful **decision or work capability** before choosing a Skill. Do not replicate the command tree or create wrapper programs.

## Core rule

Use the **smallest workflow that preserves quality**.

Do not build a chain merely because several Skills exist.

## Typical routes

- unclear ownership → Scout → Plan or Debug;
- bug → Scout if needed → Debug → Fix/Cook → Test → Code Review;
- feature → Research/Brainstorm if needed → Plan → Cook → Test → Code Review;
- PR → Review PR / Code Review;
- long continuation → Continuity/Handoff;
- independent parallel jobs → Orchestrate or Team only when parallelism/isolation is worth its coordination cost.

## Using the selected Skill

A Skill communicates what the agent should notice, decide and verify; it is not a terminal command or a process. Read the smallest relevant Skill/reference, apply its working method to the actual project evidence and act using the tools the current harness genuinely exposes. A command name may signal an intent, but it does not prescribe the runtime, file layout or tool chain. When a task needs executable or durable effects, authorize and verify those effects separately. Do not claim a worker, event stream or adapter exists merely because a Skill describes the workflow.

## Native boundary

If native AgentKit Engineer is actually usable in the active environment, prefer it instead of loading the fallback library.

## Output

Return the selected route only when route visibility helps the user or downstream workflow. Do not add routing narration to trivial tasks.
