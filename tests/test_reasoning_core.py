from pathlib import Path

root=Path(__file__).resolve().parents[1]
reason=(root/"skills/angent-reasoning/SKILL.md").read_text(encoding="utf-8").lower()
research=(root/"skills/angent-research/SKILL.md").read_text(encoding="utf-8").lower()
execution=(root/"skills/angent-execution/SKILL.md").read_text(encoding="utf-8").lower()
quality=(root/"skills/angent-quality/SKILL.md").read_text(encoding="utf-8").lower()
root_skill=(root/"skills/angent/SKILL.md").read_text(encoding="utf-8").lower()

for marker in [
    "problem/system model","hypothesis","causal","decision",
    "planning","replanning","information value"
]:
    assert marker in reason,marker

assert "evidence delta" in research
assert "observation delta" in execution
assert "solution integrity" in quality
assert "reasoning owns the decision state" in root_skill

for ref in [
    "problem-model.md","system-model.md","hypothesis-reasoning.md",
    "decision-model.md","adaptive-planning.md"
]:
    assert ref in reason,ref

print("PASS first-class ANGENT Reasoning ownership and evidence/action feedback loop")
