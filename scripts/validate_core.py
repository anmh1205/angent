#!/usr/bin/env python3
"""Check packaging and skill references, not model behavior."""

import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
primary = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
codex = json.loads((ROOT / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))

assert primary["name"] == codex["name"], "plugin names differ"
assert primary["version"] == codex["version"], "plugin versions differ"
assert primary["extensions"]["com.openai"]["interface"]["defaultPrompt"] == codex["interface"]["defaultPrompt"], "bootstrap prompts differ"
assert not subprocess.check_output(["git", "ls-files", "--", ".angent/"], cwd=ROOT), "live .angent/ state is tracked"

skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
assert skills, "no core skills found"
for skill in skills:
    contents = skill.read_text(encoding="utf-8")
    assert contents.startswith("---\n"), f"missing frontmatter: {skill}"
    match = re.search(r"^name:\s*(.+)$", contents, re.MULTILINE)
    assert match and match.group(1) == skill.parent.name, f"skill identity mismatch: {skill}"
    for reference in set(re.findall(r"(?<![\w/])references/[\w./-]+\.md", contents)):
        target = skill.parent / reference
        assert target.is_file(), f"missing {reference} referenced by {skill}"

print(f"Core structure valid ({len(skills)} skills; manifests consistent).")
