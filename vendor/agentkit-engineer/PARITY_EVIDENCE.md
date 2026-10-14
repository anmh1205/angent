# Engineer fallback parity evidence — stable 2026-10-14

This record supports the portable fallback parity claim for the stable AgentKit Engineer surface.

It records observable catalog/package evidence and semantic calibration. It is not a claim of byte-for-byte upstream or runtime-mechanics parity.

## Source boundary

Official stable sources inspected:

- https://docs.agentkit.best/en/stable/kits/engineer
- https://docs.agentkit.best/en/stable/kits/engineer/skills
- https://docs.agentkit.best/en/stable/kits/engineer/agents
- individual stable Skill guides for changed/high-risk workflows.

Observed stable package composition:

- 103 documented public Skill identities;
- 16 Agent roles;
- retired pages are routing references, not packaged public identities.

Machine-readable expected identity state is `STABLE_CATALOG.json`.

## Baseline

Canonical base:

- repository: `anmh1205/angent`
- base commit: `624983004cf24a3994dada8f073e82a9457494d0`
- previous fallback public Skill directories: 102
- missing current public identities: 8
- extra public-discovery identities relative to current stable: 7
  - six retired routes;
  - `ak-common` internal support.

The old selector accepted fallback readiness from count equality (102 Skills / 16 roles), so a same-count identity substitution could pass.

## Candidate

Branch: `engineer-stable-parity-refresh`.

Structural migration:

- add 8 current public Skills;
- remove six retired routes from public discovery;
- move common conventions outside public discovery;
- exact result: 103 public Skills + 16 role files.

Retired-route guidance is preserved in `COMPATIBILITY.md`; it is not exposed as a runnable current Skill.

## Positive mechanical validation

On SERVER with AgentKit CLI `ak 2.19.0`, the fallback selector was run read-only with native usability explicitly set to `no` and doctor disabled.

Observed fallback result:

```text
plugin_manifest_valid = true
catalog_valid = true
skills = 103
agent_roles = 16
expected_skills = 103
expected_agent_roles = 16
missing_skills = []
extra_skills = []
missing_agent_roles = []
extra_agent_roles = []
ready = true
mode = fallback
```

A separate frontmatter/discovery check observed:

```text
skill_dirs = 103
bad name/directory mappings = []
duplicate names = []
retired public leaks = []
```

The selector compiled successfully and committed diff hygiene passed in the same validation run.

## Negative same-count validation

To test the failure mode that count-only readiness could not detect, a temporary local checkout renamed public identity:

```text
ak-bro → ak-bro-wrong
```

The number of public Skill directories remained 103.

Observed selector result:

```text
skills = 103
missing_skills = ["ak-bro"]
extra_skills = ["ak-bro-wrong"]
ready = false
mode = blocked
process exit from selector = 1
```

The checkout was reset/cleaned after the test.

This establishes that readiness depends on exact identity sets rather than count equality.

## Semantic calibration

### Native-first selection

PASS property:

- native is selected only when the active harness establishes current usability;
- CLI/cache/docs presence alone does not prove active native Engineer;
- native and full fallback catalogs are not exposed together by default.

### Team lifecycle

Stable behavior requires live team creation/shared work/messaging/wait/shutdown/cleanup.

Fallback property:

- `ak-team` verifies those load-bearing capabilities;
- missing lifecycle causes a hard stop for Team;
- ordinary subagents, sequential roles, or an Orchestrate graph are not silently relabeled as Team.

### Orchestrate

Fallback property:

- preserves dependency-aware job graph, live route verification, writer isolation, bounded evidence, and arbitration;
- does not fabricate native process-supervisor durability, background execution, sandboxing, or parallelism;
- sequential degradation is allowed only when overlap/runtime diversity/detached durability are not load-bearing.

### Bootstrap

Research caught and corrected an audit error before acceptance: current stable still exposes `auto`, `full`, `fast`, and `parallel` modes.

Fallback property:

- preserves those mode meanings and their verification/authority gates;
- does not treat a mode flag as authority for credentials, spend, publication, Git delivery, destructive effects, or deployment.

### High-risk workflows

Current stable semantics were rechecked for:

- `ak-cook` — implementation modes plus mandatory review and bounded authority;
- `ak-test` — validation, suite creation/optimization/audit, UI evidence and attribution;
- `ak-code-review` — independent risk review and stronger multi-reviewer strategies without silent degradation;
- `ak-security` — comprehensive/fast/red-team/fix boundaries, secret redaction and fix authority;
- `ak-find-skills` — local routing separated from external package discovery/installation approval;
- `ak-autoresearch` — router to measurable specialist workflows rather than a universal autonomous loop.

## Validity boundary

This evidence establishes:

- current stable public identity coverage at the recorded source date;
- exact fallback package identity readiness;
- selected workflow-semantic calibration for changed/high-risk workflows.

It does **not** establish:

- native AgentKit usability in every harness;
- byte-for-byte source parity;
- identical runtime mechanics across Claude/Codex/Cursor/other harnesses;
- complete behavioral equivalence for all future upstream changes.

Re-run catalog/source reconciliation when the stable package changes.
