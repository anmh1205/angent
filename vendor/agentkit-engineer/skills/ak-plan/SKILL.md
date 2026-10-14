---
name: ak-plan
description: Produce a durable implementation roadmap from an accepted outcome, with evidence-grounded phases, dependencies, risks, validation gates and explicit unresolved decisions.
license: MIT
metadata: {port: angent-fallback, mode: adapted, baseline: "AgentKit Engineer 2.19.0"}
---

# Plan — Portable Fallback

Use when a feature, refactor, repair, migration, or architecture change needs a roadmap before implementation.

Do not use Plan to hide an unresolved product/architecture decision. If the direction itself is still open, return to Brainstorm/Research/Reasoning first.

## Load progressively

- `references/scope-and-modes.md` — scope challenge, planning modes, TDD and parallel/two-approach semantics.
- `references/files-first-plan.md` — durable plan representation and execution handoff.
- `references/decomposition.md` — dependency/ownership/outcome decomposition.
- `references/plan-validation.md` — evidence verification, adversarial review and decision validation.
- `references/plan-reconciliation.md` — existing-plan overlap and whole-plan consistency.

## Delivery contract

Before planning, establish or reuse:
- outcome;
- requested scope and non-goals;
- hard constraints/invariants;
- acceptance criteria;
- relevant evidence/current-state observations;
- authority boundary for research or external projections;
- unresolved decisions that could change the architecture.

Requested scope is the baseline. Do not silently cut it in the name of YAGNI. Scope reduction requires an explicit user instruction or a task mode that clearly authorizes scope challenge.

## Operations

The portable fallback preserves four useful operations:

- **create** — produce a new implementation roadmap;
- **validate** — verify material plan claims and resolve genuine decision points;
- **red-team** — adversarially challenge assumptions, dependencies, failure modes, migration/rollback and verification;
- **archive** — mark a plan inactive/closed in the project's plan/index mechanism without deleting its durable files.

Runtime-specific CLI/index mechanics are optional. The plan artifact remains authoritative enough to understand and resume work. Read `references/cli-free-lifecycle.md` for the complete plan/status/phase/file mapping **without** `ak plan`; use host file/connector actions and verify actual persistence.

## Workflow

1. Read applicable `AGENTS.md`, current requirements, relevant source/tests and unfinished plans.
2. Run the scope challenge from `scope-and-modes.md` unless the task is genuinely trivial.
3. Choose planning depth from uncertainty, blast radius and coordination needs; explicit user mode wins.
4. Inspect/research only the evidence needed to design correctly. Use Scout for repository ownership/flow and Research for external/versioned facts.
5. Record current-state facts, accepted decisions and load-bearing assumptions separately.
6. Design the smallest architecture that satisfies the full accepted scope.
7. Decompose by dependency and coherent outcome, not by file count.
8. For each phase/work unit, include implementation intent, affected interfaces/state, verification and replan triggers.
9. For parallel work, prove ownership/dependency separation before marking phases concurrent.
10. Run adversarial review and plan validation when the selected mode requires them.
11. Reconcile any accepted validation change through every affected phase and perform a whole-plan consistency sweep.
12. Persist the roadmap as ordinary readable project artifacts and return the exact path/pointer.

Plan does not silently start implementation. Hand off to Cook only when the plan is accepted enough for the requested consequence level.

## Optional projections

HTML, GitHub issue/task, wiki, or other projections may be produced only when requested/authorized and supported by the active harness.

They are views. They do not replace the durable plan or create implementation/deployment authority.

## Completion

A plan is ready when:
- requested scope and non-goals are explicit;
- architecture/implementation direction is supported by current evidence;
- phases/dependencies/ownership are coherent;
- material assumptions and risks are visible;
- every meaningful phase has acceptance evidence;
- blocking validation failures are resolved;
- the whole-plan sweep finds no material contradiction;
- unresolved user-owned decisions remain visible instead of guessed.
