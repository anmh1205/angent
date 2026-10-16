#!/usr/bin/env python3
"""Actually print BA Markdown to PDF in Chromium, then verify readable PDF pages.

Optional packages: playwright, pypdf, pandoc and a real local Chromium.
This is a repository regression, not a distributed skill executable.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys
import tempfile

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"extensions/angent-ba/scripts"))
from build_export import export


def check(chrome:str,pandoc:str)->dict:
    try:
        from pypdf import PdfReader
    except ImportError as exc:
        raise ValueError("pypdf required to check real rendered PDF pages") from exc
    docs=["docs/atlas-re/atlas-re-urd.md",
          "docs/atlas-re/atlas-re-brd.md",
          "docs/atlas-re/atlas-re-prd.md"]
    data,source=export(ROOT/"extensions/angent-ba/examples",docs,
                       "Atlas decision review","pdf",pandoc=pandoc,
                       pdf_engine="chromium",chrome=chrome)
    if not data.startswith(b"%PDF-"):
        raise ValueError("Expected real PDF binary")
    with tempfile.TemporaryDirectory() as tmp:
        file=Path(tmp)/"review.pdf"
        file.write_bytes(data)
        reader=PdfReader(str(file),strict=True)
        text="\n".join(page.extract_text() or "" for page in reader.pages)
        if len(reader.pages)<3:
            raise ValueError("Incomplete PDF pages: "+str(len(reader.pages)))
        for essential in ("Atlas decision review","Business Objectives","Capabilities"):
            if essential not in text:
                raise ValueError("Missing actual PDF text: "+essential)
        if len(text)<1000:
            raise ValueError("Suspiciously empty PDF extracted text")
        return {"ok":True,"engine":"real Chromium + Pandoc HTML",
                "page_count":len(reader.pages),"text_characters":len(text),
                "source_files":len(source),"pdf_bytes":len(data),
                "external_provider_writes":0,"production_documents":False}

def main()->int:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--chrome",required=True)
    ap.add_argument("--pandoc",default="pandoc")
    args=ap.parse_args()
    try:
        result=check(args.chrome,args.pandoc)
    except (ValueError,OSError,TypeError) as exc:
        result={"ok":False,"error":str(exc)}
    print(json.dumps(result,ensure_ascii=False))
    return 0 if result["ok"] else 1

if __name__=="__main__":
    raise SystemExit(main())
