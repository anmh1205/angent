#!/usr/bin/env python3
"""Check packaging and skill references, not model behavior."""

import json
from pathlib import Path
import re
import subprocess
import struct

ROOT = Path(__file__).resolve().parents[1]
primary = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
codex = json.loads((ROOT / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))

assert primary["name"] == codex["name"], "plugin names differ"
assert primary["version"] == codex["version"], "plugin versions differ"
assert primary["extensions"]["com.openai"]["interface"]["defaultPrompt"] == codex["interface"]["defaultPrompt"], "bootstrap prompts differ"

primary_ui = primary["extensions"]["com.openai"]["interface"]
codex_ui = codex["interface"]
for key in ("brandColor", "logo", "composerIcon"):
    assert primary_ui.get(key) == codex_ui.get(key), f"OpenAI interface {key} differs"
for key in ("logo", "composerIcon"):
    path = primary_ui[key]
    assert path.startswith("./assets/"), f"invalid {key} path"
    png = ROOT / path[2:]
    assert png.is_file(), f"missing {key}: {png}"
    data = png.read_bytes()
    assert data[:8] == b"\x89PNG\r\n\x1a\n", f"{key} is not PNG"
    width, height = struct.unpack(">II", data[16:24])
    assert width == height and 48 <= width <= 4096, f"{key} dimensions invalid"
assert all(len(s) <= 128 for s in primary_ui["defaultPrompt"]), "starter prompt exceeds UI limit"
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
