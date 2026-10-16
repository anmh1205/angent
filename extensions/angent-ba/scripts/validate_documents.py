#!/usr/bin/env python3
"""Read-only checker for completed BA Markdown documents."""
import argparse
import json
from pathlib import Path
import re

TEMPLATE = re.compile(r"\{\{[\w.-]+\}\}")
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:#[^|\]]+)?(?:\|[^\]]+)?\]\]")
ID_ROW = re.compile(r"^\|\s*((?:FR|NFR|BR|E|TC|AC)-[\w-]+)\s*\|", re.I)
VALID_STATES = {"draft","in-review","revisions","approved","shipped","captured","processed","proposed"}

# The source BA kit stores per-item content in body-only Markdown, with status
# and revisions in a sibling index. This is a bounded documented exception,
# not general permission to silently omit provenance on arbitrary files.
INDEXED_BODIES = {
    "usecases": (r"^uc-[a-z0-9][a-z0-9-]*\.md$", "*-usecase-index.md", "usecase-index"),
    "userstories": (r"^us-[a-z0-9][a-z0-9-]*\.md$", "*-story-index.md", "userstory-index"),
    "ascii-wireframe": (r"^(?!.*-wireframe-index\.md$)[a-z0-9][a-z0-9-]*\.md$",
                         "*-wireframe-index.md", "screen-index"),
}

def indexed_body(path, root):
    contract=INDEXED_BODIES.get(path.parent.name)
    if not contract or not re.fullmatch(contract[0], path.name, flags=re.I):
        return False
    index_files=[p for p in path.parent.glob(contract[1]) if p.is_file()
                 and p.resolve().is_relative_to(root.resolve())]
    if len(index_files)!=1:
        return False
    data=index_files[0].read_text(encoding="utf-8")
    if not data.startswith("---\n"):
        return False
    end=data.find("\n---\n",4)
    if end < 0:
        return False
    return any(re.fullmatch(r"type:\s*"+re.escape(contract[2])+r"\s*", line.strip())
               for line in data[4:end].splitlines())

def inspect(path, root):
    errors, warnings = [], []
    raw = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    if not raw.startswith("---\n"):
        if indexed_body(path, root):
            warnings.append("Index-managed content: approval, source status and index row membership need separate verification")
        else:
            errors.append("missing document frontmatter")
        content, front = raw, {}
    else:
        stop = raw.find("\n---\n", 4)
        if stop < 0:
            errors.append("unterminated document frontmatter")
            content, front = raw, {}
        else:
            content, front = raw[stop+5:], {}
            for line in raw[4:stop].splitlines():
                if line and not line[0].isspace() and ":" in line:
                    k,v=line.split(":",1)
                    front[k.strip()] = v.strip().strip('"')
    if not content.strip():
        errors.append("empty document")
    if TEMPLATE.search(raw):
        errors.append("unresolved template variables")
    if raw.count(chr(96)*3)%2:
        errors.append("unclosed code fence")
    if front.get("status") and front["status"] not in VALID_STATES:
        errors.append("invalid status")
    if front.get("updated") and not re.fullmatch(r"\d{4}-\d{2}-\d{2}",front["updated"]):
        errors.append("invalid date format")
    ids=[]
    for line in content.splitlines():
        m=ID_ROW.search(line)
        if m:ids.append(m.group(1))
    for ident in set(ids):
        if ids.count(ident)>1:errors.append("duplicate table row ID: "+ident)
    for value in LINK.findall(content)+WIKILINK.findall(content):
        if value.startswith(("http://","https://","mailto:","#")):continue
        if "://" in value or value.startswith(("javascript:","data:")):
            errors.append("unsafe link: "+value);continue
        # Fragment identifiers select headings inside the same physical file.
        # They must not be included in filesystem existence/path checks.
        local_path=value.split("#",1)[0]
        if not local_path:
            continue
        target=(root/local_path if local_path.startswith("docs/") else path.parent/local_path).resolve()
        if not target.is_relative_to(root.resolve()):
            errors.append("path traversal: "+value)
        elif not target.is_file():
            errors.append("broken local reference: "+value)
    if not any(line.lstrip().startswith("# ") for line in content.splitlines()):
        warnings.append("no main heading")
    return {"path":str(path),"ok":not errors,"errors":sorted(set(errors)),"warnings":warnings,
            "table_ids":sorted(set(ids))}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("target",type=Path)
    p.add_argument("--root",type=Path,default=Path("."))
    a=p.parse_args()
    paths=list(a.target.rglob("*.md")) if a.target.is_dir() else [a.target]
    if not paths or any(not x.is_file() for x in paths):
        print(json.dumps({"ok":False,"errors":["No readable documents"]}));return 2
    results=[inspect(x,a.root) for x in paths]
    print(json.dumps({"ok":all(r["ok"] for r in results),"files":results},ensure_ascii=False,indent=2))
    return 0 if all(r["ok"] for r in results) else 1

if __name__=="__main__":
    raise SystemExit(main())
