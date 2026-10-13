from pathlib import Path
import json
import re

root=Path(__file__).resolve().parents[1]
schema="https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
allowed={
    "$schema","name","version","description","author","homepage",
    "repository","license","keywords","extensions",
}
name_re=re.compile(r"^[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?$")

for path in [root/"plugin.json",root/"vendor/agentkit-engineer/plugin.json"]:
    data=json.loads(path.read_text(encoding="utf-8"))
    assert not (set(data)-allowed),(path,set(data)-allowed)
    assert data["$schema"]==schema,path
    name=data["name"]
    assert 1<=len(name)<=64,(path,name)
    assert name_re.fullmatch(name),(path,name)
    assert "--" not in name and ".." not in name,(path,name)
    for key in ("version","description","homepage","repository","license"):
        if key in data:
            assert isinstance(data[key],str),(path,key)
    if "author" in data:
        assert isinstance(data["author"],dict),path
        assert not (set(data["author"])-{"name","email","url"}),path
        assert all(isinstance(v,str) for v in data["author"].values()),path
    if "keywords" in data:
        assert isinstance(data["keywords"],list),path
        assert all(isinstance(v,str) for v in data["keywords"]),path
    if "extensions" in data:
        assert isinstance(data["extensions"],dict),path

for path in [root/".codex-plugin/plugin.json",root/"vendor/agentkit-engineer/.codex-plugin/plugin.json"]:
    data=json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(data.get("name"),str) and data["name"],path
    if "skills" in data:
        value=data["skills"]
        assert isinstance(value,str) and value.startswith("./") and ".." not in value,path

print("PASS portable and ChatGPT/Codex plugin manifest conformance")
