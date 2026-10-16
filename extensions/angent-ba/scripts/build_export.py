#!/usr/bin/env python3
"""Export a reviewed, explicit set of BA Markdown documents to MD/HTML/DOCX/PDF.

No implicit vault scan, no external image/font downloads, no fallback masquerading
as an output of a different type. PDF may require separate TeX installation.
"""
from __future__ import annotations
import argparse
import hashlib
import html
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
from zipfile import ZipFile,is_zipfile

PATHNAME=re.compile(r"^[A-Za-z0-9_./-]+\.md$")
FORMATS={"md":".md","html":".html","docx":".docx","pdf":".pdf"}


def gather(root:Path,paths:list[str],title:str)->tuple[str,list[dict]]:
    root=root.resolve()
    if not isinstance(title,str) or not title.strip() or len(title)>160 or "\n" in title:
        raise ValueError("Invalid package title")
    if not paths or len(paths)>80 or len(set(paths))!=len(paths):
        raise ValueError("Provide 1–80 explicit, nonduplicated Markdown source files")
    files=[]
    total=0
    for raw in paths:
        if not isinstance(raw,str) or not PATHNAME.fullmatch(raw) or raw.startswith(("/", "./")):
            raise ValueError("Invalid Markdown source path: "+str(raw))
        target=(root/raw).resolve()
        if not target.is_relative_to(root) or not target.is_file():
            raise ValueError("Source does not exist or escapes root: "+raw)
        body=target.read_text(encoding="utf8")
        total+=len(body.encode("utf8"))
        if total>3_000_000:
            raise ValueError("Output source exceeds 3MB safety bound")
        files.append({"path":raw,"sha256":hashlib.sha256(body.encode("utf8")).hexdigest(),
                      "body":body.strip()})
    lines=["# "+title.strip(),"","## Contents and source revisions",""]
    for index,item in enumerate(files,1):
        lines.append(f"{index}. {item['path']} (SHA-256 {item['sha256'][:16]})")
    lines.extend(["","---",""])
    for index,item in enumerate(files,1):
        lines.extend([f"## Document {index}: {item['path']}","",item["body"],"","---",""])
    manifest=[{"path":x["path"],"sha256":x["sha256"]} for x in files]
    return "\n".join(lines),manifest


def _pandoc(command:str,markdown:str,fmt:str,title:str)->bytes:
    cli=shutil.which(command)
    if cli is None:
        raise ValueError("Pandoc not installed; cannot produce "+fmt.upper())
    options=[cli,"--sandbox","--from=markdown-raw_html-raw_tex","--standalone",
             "--metadata=title:"+title]
    if fmt=="html":
        args=options+["--to=html5"]
        result=subprocess.run(args,input=markdown,text=True,capture_output=True,errors="replace",timeout=120)
        if result.returncode:
            raise ValueError("Pandoc HTML failed: "+result.stderr[-1500:])
        output=result.stdout
        # No active resources or script execution in the stakeholder preview.
        csp="default-src 'none'; style-src 'unsafe-inline'; img-src 'none'; font-src 'none'; form-action 'none'; base-uri 'none'"
        meta='<meta http-equiv="Content-Security-Policy" content="'+html.escape(csp,quote=True)+'">'
        if "</head>" not in output.lower():
            raise ValueError("Pandoc output has no HTML head")
        output=output.replace("</head>",meta+"</head>",1)
        if re.search(r"<\s*script\b",output,re.I):
            raise ValueError("HTML export contains script; refusing unsafe output")
        return output.encode("utf8")
    with tempfile.TemporaryDirectory() as tmp:
        target=Path(tmp)/("package."+fmt)
        args=options+["--to="+fmt,"--output="+str(target)]
        result=subprocess.run(args,input=markdown,text=True,capture_output=True,errors="replace",timeout=180)
        if result.returncode or not target.is_file():
            raise ValueError("Pandoc "+fmt.upper()+" failed; check engine: "+result.stderr[-1700:])
        contents=target.read_bytes()
        if fmt=="pdf" and not contents.startswith(b"%PDF"):
            raise ValueError("Output is not a PDF")
        if fmt=="docx":
            if not is_zipfile(target):
                raise ValueError("Output is not an OOXML Word archive")
            with ZipFile(target) as archive:
                if "word/document.xml" not in archive.namelist():
                    raise ValueError("DOCX lacks document.xml")
        return contents


def export(root:Path,paths:list[str],title:str,fmt:str,pandoc:str="pandoc")->tuple[bytes,list[dict]]:
    if fmt not in FORMATS:raise ValueError("Unsupported export format")
    markdown,manifest=gather(root,paths,title)
    if fmt=="md":
        payload=markdown.encode("utf8")
    else:
        payload=_pandoc(pandoc,markdown,fmt,title)
    if len(payload)<100:
        raise ValueError("Generated output is unexpectedly empty")
    return payload,manifest


def main()->int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("docs",nargs="+",help="Explicit source paths within --root")
    parser.add_argument("--root",required=True,type=Path)
    parser.add_argument("--output",required=True,type=Path)
    parser.add_argument("--format",required=True,choices=sorted(FORMATS))
    parser.add_argument("--title",required=True)
    parser.add_argument("--pandoc",default="pandoc")
    args=parser.parse_args()
    try:
        if args.output.suffix.lower()!=FORMATS[args.format]:
            raise ValueError("Output suffix must match requested format")
        if args.output.exists():
            raise ValueError("Refusing to overwrite existing stakeholder export")
        result,manifest=export(args.root,args.docs,args.title,args.format,args.pandoc)
        args.output.parent.mkdir(parents=True,exist_ok=True)
        with args.output.open("xb") as stream:
            stream.write(result)
        report={"ok":True,"format":args.format,"output":str(args.output),
                "source_docs":manifest,"bytes":len(result),"source_files_modified":0,
                "external_provider_writes":0,"status":"actual-output-created"}
    except (OSError,ValueError,TypeError,subprocess.TimeoutExpired) as exc:
        report={"ok":False,"error":str(exc),"status":"not-created"}
    print(json.dumps(report,ensure_ascii=False))
    return 0 if report["ok"] else 1
if __name__=="__main__":
    raise SystemExit(main())
