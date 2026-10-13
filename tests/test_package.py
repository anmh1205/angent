from pathlib import Path
import json, re

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

refs={p.name for p in (root/"skills/angent/references").glob("*.md")}
required_refs={
    "task-model.md","problem-model.md","system-model.md","hypothesis-reasoning.md",
    "decision-model.md","adaptive-planning.md","evidence-model.md","interface-contracts.md",
    "reader-state.md","concept-admission.md","explanation-composition.md","representation.md",
    "language-vi.md","quality-rubric.md","learning-loop.md","continuity-protocol.md",
    "core-fixtures.md",
}
assert required_refs<=refs,required_refs-refs

all_md=list(root.rglob("*.md"))
for p in all_md:
    text=p.read_text(encoding="utf-8")
    for name in re.findall(r"`([A-Za-z0-9._-]+\.md)`",text):
        if name in required_refs:
            assert (root/"skills/angent/references"/name).exists(),(p,name)

print("PASS ANGENT 1.0.0 package identity and canonical reference graph")
