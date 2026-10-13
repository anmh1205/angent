from pathlib import Path

root=Path(__file__).resolve().parents[1]
interfaces=(root/"skills/angent/references/interface-contracts.md").read_text(encoding="utf-8")
required=[
    "TaskModel","StateDelta","EvidenceQuery","EvidenceDelta","ActionNode",
    "ObservationDelta","SolutionModel","QualityVerdict","PromotedMechanism","Frontier",
]
for marker in required:
    assert marker in interfaces,marker

execution=(root/"skills/angent-execution/SKILL.md").read_text(encoding="utf-8")
author=(root/"skills/angent-authoring/SKILL.md").read_text(encoding="utf-8")
learning=(root/"skills/angent-learning/SKILL.md").read_text(encoding="utf-8")
continuity=(root/"skills/angent-continuity/SKILL.md").read_text(encoding="utf-8")

assert "does not own strategic reasoning" in execution
assert "does not solve unresolved technical reasoning" in author
assert "Do not paste user wording" in learning
assert "Continuity owns persistence, not task strategy" in continuity

print("PASS ANGENT owner boundaries and hand-off contracts")
