from pathlib import Path

root=Path(__file__).resolve().parents[1]
reason=(root/"skills/angent-reasoning/SKILL.md").read_text(encoding="utf-8").lower()
research=(root/"skills/angent-research/SKILL.md").read_text(encoding="utf-8").lower()
execution=(root/"skills/angent-execution/SKILL.md").read_text(encoding="utf-8").lower()
quality=(root/"skills/angent-quality/SKILL.md").read_text(encoding="utf-8").lower()
root_skill=(root/"skills/angent/SKILL.md").read_text(encoding="utf-8").lower()

for marker in [
    "problem/system model","hypotheses","decision",
    "information value","decision sensitivity","plans are provisional",
]:
    assert marker in reason, marker

for ref in [
    "references/core-models.md",
    "references/abstraction-and-invariants.md",
    "references/specialist-synthesis.md",
]:
    assert ref in reason, ref

core=(root/"skills/angent-reasoning/references/core-models.md").read_text(encoding="utf-8").lower()
for marker in ["problem model","system model","hypothesis model","decision model","adaptive plan"]:
    assert marker in core, marker

assert "evidence delta" in research
assert "observation delta" in execution
assert "solution integrity" in quality
assert "reasoning owns decision state" in root_skill

print("PASS ANGENT Reasoning cognitive control and evidence/action feedback loop")
