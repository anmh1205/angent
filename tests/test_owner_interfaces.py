from pathlib import Path

root=Path(__file__).resolve().parents[1]
interfaces=(root/"skills/angent/references/interface-contracts.md").read_text(encoding="utf-8")

for marker in [
    "TaskModel","StateDelta","EvidenceQuery","EvidenceDelta","ActionNode",
    "ObservationDelta","SolutionModel","QualityVerdict","PromotedMechanism","Frontier",
]:
    assert marker in interfaces, marker

root_skill=(root/"skills/angent/SKILL.md").read_text(encoding="utf-8")
context=(root/"skills/angent-context/SKILL.md").read_text(encoding="utf-8")
execution=(root/"skills/angent-execution/SKILL.md").read_text(encoding="utf-8")
author=(root/"skills/angent-authoring/SKILL.md").read_text(encoding="utf-8")
learning=(root/"skills/angent-learning/SKILL.md").read_text(encoding="utf-8")
continuity=(root/"skills/angent-continuity/SKILL.md").read_text(encoding="utf-8")

assert "does not own strategic reasoning" in execution
assert "does not solve unresolved technical reasoning" in author
assert "Do not paste user wording" in learning
assert "Continuity owns persistence and resume semantics" in continuity
assert "AGENTS.md is the canonical project instruction surface" in context
assert "prefer native AgentKit Engineer" in root_skill
assert "vendor/agentkit-engineer/" in root_skill

print("PASS ANGENT owner boundaries, project instructions, and native/fallback routing")
