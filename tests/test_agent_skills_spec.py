from pathlib import Path
import re

root=Path(__file__).resolve().parents[1]
allowed={"name","description","license","compatibility","metadata","allowed-tools"}
name_pattern=re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

skill_files=list((root/"skills").glob("*/SKILL.md"))+list((root/"vendor/agentkit-engineer/skills").glob("*/SKILL.md"))
assert len(skill_files)==114,len(skill_files)

for path in skill_files:
    text=path.read_text(encoding="utf-8")
    match=re.match(r"^---\s*\n([\s\S]*?)\n---",text)
    assert match,path
    frontmatter=match.group(1)
    keys=[]
    name=None
    description_seen=False
    for line in frontmatter.splitlines():
        item=re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$",line)
        if not item:
            continue
        key,value=item.groups()
        keys.append(key)
        if key=="name":
            name=value.strip().strip('"').strip("'")
        elif key=="description":
            description_seen=True
    extras=set(keys)-allowed
    assert not extras,(path,extras)
    assert name==path.parent.name,(path,name,path.parent.name)
    assert name_pattern.fullmatch(name),(path,name)
    assert description_seen,path

for path in (root/"vendor/agentkit-engineer/skills").rglob("*.md"):
    text=path.read_text(encoding="utf-8")
    assert not re.search(r"\bak:[a-z0-9-]+",text),(path,"legacy fallback Skill identity")

print("PASS Agent Skills portable frontmatter/name conformance for 114 Skills")
