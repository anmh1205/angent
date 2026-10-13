from pathlib import Path
import json
import subprocess
import sys

root=Path(__file__).resolve().parents[1]
vendor=root/"vendor/agentkit-engineer"
assert (vendor/"README.md").exists()
assert (vendor/"NATIVE_AGENTKIT.md").exists()
assert not (vendor/"upstream").exists()
assert not (vendor/"UPSTREAM.md").exists()

fallback_manifest=json.loads((vendor/"plugin.json").read_text(encoding="utf-8"))
assert fallback_manifest["$schema"]=="https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
assert fallback_manifest["name"]=="angent-engineer-fallback"

codex_manifest=json.loads((vendor/".codex-plugin/plugin.json").read_text(encoding="utf-8"))
assert codex_manifest["name"]=="angent-engineer-fallback"
assert codex_manifest["version"]=="1.0.0"
assert codex_manifest["skills"]=="./skills/"

selector=vendor/"scripts/select_engineer.py"
assert selector.exists()

def select(native_usable):
    proc=subprocess.run(
        [
            sys.executable,
            str(selector),
            "--native-usable",
            native_usable,
            "--doctor",
            "none",
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=True,
    )
    return json.loads(proc.stdout)

native_selection=select("yes")
assert native_selection["mode"]=="native"
assert native_selection["policy"]["load_both"] is False

fallback_selection=select("no")
assert fallback_selection["mode"]=="fallback"
assert fallback_selection["fallback"]["plugin_manifest_valid"] is True
assert fallback_selection["fallback"]["skills"]==102
assert fallback_selection["fallback"]["agent_roles"]==16
assert fallback_selection["fallback"]["ready"] is True

unknown_selection=select("unknown")
assert unknown_selection["mode"]=="fallback"
assert unknown_selection["reason"]=="native_engineer_usability_unproven"

for skill in ["ak-scout","ak-test","ak-handoff","ak-debug","ak-code-review"]:
    portable=vendor/"skills"/skill/"SKILL.md"
    assert portable.exists(),skill

    portable_text=portable.read_text(encoding="utf-8")

    assert "license: MIT" in portable_text
    assert "port: angent-fallback" in portable_text
    assert "[Reading " not in portable_text
    assert "[executed on device:" not in portable_text

# Fallback content must not hard-require old Claude/AgentKit runtime paths.
scout=(vendor/"skills/ak-scout/SKILL.md").read_text(encoding="utf-8").lower()
test=(vendor/"skills/ak-test/SKILL.md").read_text(encoding="utf-8").lower()
handoff=(vendor/"skills/ak-handoff/SKILL.md").read_text(encoding="utf-8").lower()

debug=(vendor/"skills/ak-debug/SKILL.md").read_text(encoding="utf-8").lower()
review=(vendor/"skills/ak-code-review/SKILL.md").read_text(encoding="utf-8").lower()

for text in [scout,test,handoff,debug,review]:
    assert ".claude/" not in text
    assert ".agentkit/" not in text

assert "claude code:" not in scout
assert "ak:agent-browser" not in test
assert "/ak:handoff" not in handoff
assert "angent continuity" in handoff
assert "root cause" in debug
assert "independent technical judgment" in review

native=(vendor/"NATIVE_AGENTKIT.md").read_text(encoding="utf-8").lower()
assert "agentkit.best" in native
assert "does not bundle or mirror native agentkit engineer source" in native

print("PASS native AgentKit guidance and portable fallback separation")
