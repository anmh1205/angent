from pathlib import Path
import json
import subprocess
import sys
import tempfile

root=Path(__file__).resolve().parents[1]
memory=root/"skills/angent-context/scripts/memory_store.py"
frontier=root/"skills/angent-continuity/scripts/frontier_store.py"

with tempfile.TemporaryDirectory() as tmp:
    tmp=Path(tmp)

    memory_path=tmp/"memory.json"

    read0=subprocess.run(
        [sys.executable,str(memory),"--scope","project","--store",str(memory_path),"read"],
        capture_output=True,text=True,encoding="utf-8",check=True,
    )
    assert json.loads(read0.stdout)["revision"]==0

    put1=subprocess.run(
        [
            sys.executable,str(memory),"--scope","project","--store",str(memory_path),
            "put","--topic","ui/preferences","--content","Prefer compact technical prose.",
            "--provenance","user-explicit","--expected-revision","0"
        ],
        capture_output=True,text=True,encoding="utf-8",check=True,
    )
    assert json.loads(put1.stdout)["revision"]==1

    conflict=subprocess.run(
        [
            sys.executable,str(memory),"--scope","project","--store",str(memory_path),
            "put","--topic","ui/preferences","--content","stale overwrite",
            "--expected-revision","0"
        ],
        capture_output=True,text=True,encoding="utf-8",
    )
    assert conflict.returncode==3
    assert json.loads(conflict.stdout)["error"]=="revision_conflict"

    get1=subprocess.run(
        [sys.executable,str(memory),"--scope","project","--store",str(memory_path),"get","--topic","ui/preferences"],
        capture_output=True,text=True,encoding="utf-8",check=True,
    )
    assert json.loads(get1.stdout)["entry"]["content"]=="Prefer compact technical prose."

    continuity_root=tmp/"continuity"
    f1={"outcome":"finish upgrade","verified_completed":[],"unfinished":"memory","next_safe_action":"continue"}
    save1=subprocess.run(
        [
            sys.executable,str(frontier),"--root",str(continuity_root),
            "save","--work-key","angent/test","--frontier-json",json.dumps(f1),
            "--expected-revision","0"
        ],
        capture_output=True,text=True,encoding="utf-8",check=True,
    )
    assert json.loads(save1.stdout)["revision"]==1

    f2={"outcome":"finish upgrade","verified_completed":["memory"],"unfinished":"cross-harness","next_safe_action":"test another harness"}
    save2=subprocess.run(
        [
            sys.executable,str(frontier),"--root",str(continuity_root),
            "save","--work-key","angent/test","--frontier-json",json.dumps(f2),
            "--expected-revision","1"
        ],
        capture_output=True,text=True,encoding="utf-8",check=True,
    )
    assert json.loads(save2.stdout)["revision"]==2

    stale=subprocess.run(
        [
            sys.executable,str(frontier),"--root",str(continuity_root),
            "save","--work-key","angent/test","--frontier-json",json.dumps(f1),
            "--expected-revision","1"
        ],
        capture_output=True,text=True,encoding="utf-8",
    )
    assert stale.returncode==3
    assert json.loads(stale.stdout)["error"]=="revision_conflict"

    loaded=subprocess.run(
        [sys.executable,str(frontier),"--root",str(continuity_root),"load","--work-key","angent/test"],
        capture_output=True,text=True,encoding="utf-8",check=True,
    )
    payload=json.loads(loaded.stdout)
    assert payload["revision"]==2
    assert payload["frontier"]["unfinished"]=="cross-harness"

print("PASS local memory CAS and revisioned Continuity persistence")
