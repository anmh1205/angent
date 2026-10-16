#!/usr/bin/env python3
"""Run a generated Playwright case file against the actual offline HTML prototype."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"extensions/angent-ba/scripts"))
from build_playwright import generate_files
from build_wireframe import render

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--chrome",type=Path)
    args=p.parse_args()
    try:
        original=json.loads((ROOT/"extensions/angent-ba/examples/authentication-screen-model.json").read_text(encoding="utf8"))
        with tempfile.TemporaryDirectory() as tmp:
            base=Path(tmp)
            prototype=base/"prototype.html"
            prototype.write_text(render(original,"prototype"),encoding="utf8")
            outputs=generate_files(original)
            runner=base/"test_prototype.py"
            runner.write_text(outputs["test_prototype.py"],encoding="utf8")
            command=[sys.executable,str(runner),"--prototype",str(prototype)]
            if args.chrome:
                command.extend(["--chrome",str(args.chrome)])
            result=subprocess.run(command,capture_output=True,text=True,errors="replace",timeout=150)
            outputs=result.stdout.strip().splitlines()
            outcome=json.loads(outputs[-1]) if outputs else {}
            actual=outcome.get("cases")
            good=(result.returncode==0 and outcome.get("ok") and actual==7
                  and outcome.get("passed")==7 and outcome.get("external_requests")==[])
            print(json.dumps({"ok":good,"exit":result.returncode,"cases":actual,
                              "passed":outcome.get("passed"),"failures":outcome.get("failed"),
                              "stderr":result.stderr[-1200:],"scoped_to":"offline authentication mock"},
                             ensure_ascii=False))
            return 0 if good else 1
    except (OSError,ValueError,subprocess.TimeoutExpired) as exc:
        print(json.dumps({"ok":False,"error":str(exc)}))
        return 1

if __name__=="__main__":
    raise SystemExit(main())
