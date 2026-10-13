from pathlib import Path
import json

root=Path(__file__).resolve().parents[1]
main=json.loads((root/"plugin.json").read_text(encoding="utf-8"))
codex=json.loads((root/".codex-plugin/plugin.json").read_text(encoding="utf-8"))

assert main["name"]=="angent"
assert main["version"]=="1.0.0"
assert codex["name"]=="angent"
assert codex["version"]=="1.0.0"
assert main["description"]==codex["description"]

expected_skills={
    "angent","angent-contract","angent-context","angent-reasoning","angent-research",
    "angent-execution","angent-quality","angent-authoring","angent-format",
    "angent-learning","angent-continuity","angent-shell",
}
actual={p.parent.name for p in (root/"skills").glob("*/SKILL.md")}
assert actual==expected_skills,(actual^expected_skills)

assert (root/"AGENTS.md").exists()

owner_refs={
    "angent-contract":["task-model.md","authority-and-success.md"],
    "angent-context":["context-assembly.md","memory-loop.md","instruction-precedence.md"],
    "angent-reasoning":["core-models.md","abstraction-and-invariants.md","specialist-synthesis.md"],
    "angent-research":["evidence-model.md","source-conflict.md","stopping-rule.md"],
    "angent-execution":["action-semantics.md","effect-safety.md","engineer-routing.md","engineer-selection.md"],
    "angent-authoring":["reader-state.md","composition-and-representation.md","technical-exposition.md","long-form-consistency.md","headings-and-boundaries.md","surface-profiles.md","language-vi.md"],
    "angent-quality":["quality-rubric.md","coverage-and-endpoints.md","authoring-calibration.md"],
    "angent-format":["render-fidelity.md"],
    "angent-learning":["experience-loop.md","memory-boundary.md"],
    "angent-continuity":["active-work-frontier.md","continuity-protocol.md","resume-reconciliation.md"],
}
for skill,refs in owner_refs.items():
    base=root/"skills"/skill/"references"
    for ref in refs:
        assert (base/ref).exists(),(skill,ref)

# Cross-cutting root references remain during migration.
for ref in ["interface-contracts.md","core-fixtures.md","harness-contract.md"]:
    assert (root/"skills/angent/references"/ref).exists(),ref

print("PASS ANGENT 1.0.0 package identity and owner-local reference architecture")
