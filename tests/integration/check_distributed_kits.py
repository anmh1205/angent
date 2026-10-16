#!/usr/bin/env python3
"""Black-box smoke: run BA/Figma scripts FROM each freshly built release ZIP.

Unlike source-to-package byte checks, this verifies that the distributed kits
run from only extracted contents with Python's standard library.
The -E runtime ignores PYTHONPATH/PYTHONHOME but preserves the script import directory,
matching how a bundled Python CLI is normally invoked. It does
not require or pretend to exercise production APIs, cloud providers or Figma.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import zipfile

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"scripts"))
from build_packages import build,PACKAGES

SCREEN="extensions/angent-ba/examples/authentication-screen-model.json"
FLEET="extensions/angent-ba/examples/rental-fleet-traceability.json"
D2="extensions/angent-ba/examples/d2-erd.json"
BRUNO="extensions/angent-ba/examples/synthetic-fleet-api-tests.json"
OPENAPI="extensions/angent-ba/examples/synthetic-fleet-openapi.json"
FIGMA="extensions/angent-figma/examples/rental-fleet-activity.json"
SRS="extensions/angent-ba/examples/docs/atlas-re/srs/atlas-re-spec.md"


def run(package:Path,script:str,args:list[str])->dict:
    file=package/script
    if not file.is_file():
        raise ValueError("Missing distributed executable: "+script)
    result=subprocess.run(
        [sys.executable,"-E",str(file)]+args,
        cwd=package,capture_output=True,text=True,timeout=45,errors="replace",
    )
    # Most CLI tools print compact JSON, but a few print an indented object.
    try:
        data=json.loads(result.stdout.strip())
    except ValueError:
        raise ValueError("Executable did not return JSON: "+script+" "+
                         result.stdout[-500:]+result.stderr[-500:])
    # The public Reqwise candidate tool returns its MCP envelope, not an ok flag.
    is_reqwise=(script.endswith("/to_reqwise_payload.py") and
                data.get("tool")=="figma_diagram" and data.get("writes_performed") is False)
    if result.returncode!=0 or (data.get("ok") is not True and not is_reqwise):
        raise ValueError("Distributed executable failed: "+script+" "+
                         str(data)[:850]+" stderr="+result.stderr[-350:])
    return data


def check(target:Path,level:str)->dict:
    out=target/"_smoke_output"
    out.mkdir()
    html=out/"auth.html"
    wire=run(target,"extensions/angent-ba/scripts/build_wireframe.py",
             [str(target/SCREEN),"--mode","prototype","--output",str(html)])
    if "Mock response" not in html.read_text(encoding="utf8"):
        raise ValueError("Offline prototype has lost the mock-disclosure selector")
    d2=out/"model.d2"
    generated=run(target,"extensions/angent-ba/scripts/build_d2.py",
                  [str(target/D2),"--output",str(d2)])
    if "shape: sql_table" not in d2.read_text(encoding="utf8"):
        raise ValueError("Distributed D2 ERD has lost table semantics")
    bruno=out/"bruno"
    collection=run(target,"extensions/angent-ba/scripts/build_bruno.py",
                   [str(target/BRUNO),"--openapi",str(target/OPENAPI),
                    "--evidence-graph",str(target/FLEET),"--output",str(bruno)])
    reqs=sorted((bruno/"requests").glob("*.bru"))
    if len(reqs)!=4 or not all("tests {" in x.read_text(encoding="utf8") for x in reqs):
        raise ValueError("Distributed Bruno collection lacks executable request assertions")
    if collection.get("contract_check")!="checked-subset":
        raise ValueError("Distributed API contract validation was not executed")
    figma=run(target,"extensions/angent-figma/scripts/to_reqwise_payload.py",
              [str(target/FIGMA),"--evidence-graph",str(target/FLEET)])
    if figma.get("writes_performed") is not False or figma.get("tool")!="figma_diagram":
        raise ValueError("Figma packaged candidate must be a validated dry-run")
    result={"target":level,"prototype":wire.get("ok"),"d2":generated.get("ok"),
            "bruno_requests":len(reqs),"figma_candidate":"dry-run",
            "real_provider_writes":0}
    if level in ("local-agent","openai-plugin"):
        nextdir=out/"next"
        nextreport=run(target,"extensions/angent-ba/scripts/build_next_prototype.py",
                       [str(target/SCREEN),"--output",str(nextdir)])
        if nextreport.get("compile_status")!="not-run" or not (nextdir/"app/[screen]/page.jsx").is_file():
            raise ValueError("Next candidate missing or falsely marked built")
        figma_out=out/"editable"
        candidate=run(target,"extensions/angent-ba/scripts/build_figma_screens.py",
                      [str(target/SCREEN),"--output",str(figma_out)])
        if candidate.get("provider_writes")!=0 or not (figma_out/"figma-write.js").is_file():
            raise ValueError("Editable Figma screen candidate missing or falsely marked written")
        document=out/"srs-pack.md"
        exported=run(target,"extensions/angent-ba/scripts/build_export.py",
                     [SRS,"--root",str(target),"--output",str(document),
                      "--format","md","--title","Atlas BA review"])
        if exported.get("status")!="actual-output-created" or not document.is_file():
            raise ValueError("Reviewed Markdown export not actually generated")
        text=document.read_text(encoding="utf8")
        if "SHA-256" not in text or "FR-atlas-re" not in text:
            raise ValueError("Distributed export lost documented source IDs")
        result.update({"next_files":nextreport.get("files"),"editable_figma_writes":0,
                       "export_format":"md"})
    return result


def main()->int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--packages",nargs="+",choices=[p for p in PACKAGES if p!="gemini-web"],
                        default=[p for p in PACKAGES if p!="gemini-web"])
    args=parser.parse_args()
    try:
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)
            build(ROOT,root/"packages",root/"dist")
            reports=[]
            for name in args.packages:
                archive=root/"dist"/("angent-"+name+".zip")
                if not archive.is_file():raise ValueError("Release ZIP missing "+name)
                target=root/("unpacked-"+name)
                target.mkdir()
                with zipfile.ZipFile(archive) as zipfile_in:
                    for info in zipfile_in.infolist():
                        path=Path(info.filename)
                        if path.is_absolute() or ".." in path.parts or "\\" in info.filename:
                            raise ValueError("Untrusted release ZIP member: "+info.filename)
                    zipfile_in.extractall(target)
                reports.append(check(target,name))
        result={"ok":True,"independently_extracted":len(reports),
                "packages":reports,"network_requests":0,
                "external_provider_writes":0,
                "production_auth_or_figma_verified":False}
    except (ValueError,OSError,subprocess.TimeoutExpired,zipfile.BadZipFile) as exc:
        result={"ok":False,"error":str(exc)}
    print(json.dumps(result,ensure_ascii=False))
    return 0 if result["ok"] else 1


if __name__=="__main__":
    raise SystemExit(main())
