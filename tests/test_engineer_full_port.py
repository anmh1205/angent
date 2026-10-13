from pathlib import Path
import re

root=Path(__file__).resolve().parents[1]
vendor=root/"vendor/agentkit-engineer"

expected_skills=["ak-advise","ak-agent-browser","ak-agentize","ak-agentkit","ak-ai-artist","ak-ai-multimodal","ak-ak","ak-ask","ak-autoresearch","ak-backend-development","ak-better-auth","ak-bootstrap","ak-brainstorm","ak-chrome-profile","ak-code-review","ak-codex-goal","ak-coding-level","ak-common","ak-context-engineering","ak-cook","ak-copywriting","ak-cti-expert","ak-databases","ak-debug","ak-deep-swe","ak-deploy","ak-design","ak-devops","ak-docs","ak-docs-seeker","ak-document-skills","ak-excalidraw","ak-fable-thinking","ak-find-skills","ak-fix","ak-folder-context","ak-frontend-design","ak-frontend-development","ak-git","ak-github","ak-gkg","ak-goal-warmup","ak-google-adk-python","ak-graphify","ak-handoff","ak-handover","ak-help","ak-html-video","ak-hyperframes","ak-interview-docs","ak-issue-to-plan","ak-journal","ak-llms","ak-loop","ak-markdown-novel-viewer","ak-mcp-builder","ak-media-processing","ak-mermaidjs-v11","ak-mintlify","ak-mobile-development","ak-orchestrate","ak-payment-integration","ak-plan","ak-plans-kanban","ak-predict","ak-preview","ak-problem-solving","ak-project-management","ak-project-organization","ak-react-best-practices","ak-remotion","ak-repomix","ak-research","ak-research-prompt","ak-retro","ak-review-pr","ak-scenario","ak-scout","ak-security","ak-security-scan","ak-sequential-thinking","ak-shader","ak-ship","ak-shopify","ak-show-off","ak-skill-creator","ak-stitch","ak-tanstack","ak-team","ak-tech-graph","ak-test","ak-threejs","ak-ui-styling","ak-ui-ux-pro-max","ak-use-mcp","ak-vibe","ak-watzup","ak-web-design-guidelines","ak-web-frameworks","ak-web-testing","ak-worktree","ak-xia"]
expected_agents=["advisor","brainstormer","code-reviewer","code-simplifier","debugger","docs-manager","explore","fullstack-developer","git-manager","journal-writer","kongming","planner","project-manager","researcher","tester","ui-ux-designer"]

actual_skills=sorted(p.parent.name for p in (vendor/"skills").glob("*/SKILL.md"))
actual_agents=sorted(p.stem for p in (vendor/"agents").glob("*.md") if p.name!="README.md")

assert actual_skills==expected_skills,(set(actual_skills)^set(expected_skills))
assert actual_agents==expected_agents,(set(actual_agents)^set(expected_agents))

assert not (vendor/"upstream").exists()
assert not (vendor/"UPSTREAM.md").exists()

manifest=(vendor/"PORTING_MANIFEST.md").read_text(encoding="utf-8")
rows=[line for line in manifest.splitlines() if line.startswith("| `ak-")]
assert len(rows)==102,len(rows)
assert all("| IMPLEMENTED |" in line for line in rows)
assert not any("| TARGETED |" in line for line in rows)

for skill in expected_skills:
    text=(vendor/"skills"/skill/"SKILL.md").read_text(encoding="utf-8")
    lower=text.lower()
    assert text.startswith("---\n"),skill
    assert "name:" in text.split("---",2)[1],skill
    assert "description:" in text.split("---",2)[1],skill
    assert "port: angent-fallback" in lower,skill
    assert "[reading " not in lower,skill
    assert "[executed on device:" not in lower,skill
    assert ".claude/" not in lower,skill
    assert ".agentkit/" not in lower,skill
    assert "claude.md" not in lower,skill

for agent in expected_agents:
    text=(vendor/"agents"/f"{agent}.md").read_text(encoding="utf-8")
    assert text.startswith("---\n"),agent
    assert "name:" in text.split("---",2)[1],agent
    assert "description:" in text.split("---",2)[1],agent

# Degraded fallback Skills must state degraded mode in metadata.
for line in rows:
    if "DEGRADED fallback implemented" in line:
        skill=re.search(r"`([^\`]+)`",line).group(1)
        text=(vendor/"skills"/skill/"SKILL.md").read_text(encoding="utf-8").lower()
        assert "mode: degraded" in text,skill

print("PASS Engineer full-port inventory: 102 Skills + 16 Agents")
