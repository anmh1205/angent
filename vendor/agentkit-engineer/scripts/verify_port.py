#!/usr/bin/env python3
"""Verify Engineer fallback identity, metadata and local references.

Structural compatibility gate, NOT runtime/behavioral parity certification.
Standard library only; safe for local preflight and branch CI.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re

STATUS_MODE = {
    "VERIFIED_ADAPTED": "adapted",
    "VERIFIED_DEGRADED": "degraded",
    "VERIFIED_PORTABLE": "portable",
}
SKILL_ROW = re.compile(
    r"^\| `(ak-[a-z0-9-]+)` \| "
    r"(VERIFIED_ADAPTED|VERIFIED_DEGRADED|VERIFIED_PORTABLE|REVIEW_PENDING) \|",
    re.MULTILINE,
)
AGENT_ROW = re.compile(
    r"^\| `([a-z][a-z0-9-]+)` \| (VERIFIED_ADAPTED|REVIEW_PENDING) \|",
    re.MULTILINE,
)
LOCAL_REF = re.compile(r"(?:\]\(|`)(?:\./)?(references/[\w./-]+\.md)")
MARKDOWN_LINK = re.compile(r"\[[^\]\n]+\]\(([^)\n]+)\)")
LOCAL_EXTENSIONS = {".md", ".mdx", ".png", ".jpg", ".svg", ".html", ".json", ".py", ".js", ".ts", ".cjs", ".css"}
NAME = re.compile(r"^name:\s*(\S+)", re.MULTILINE)
MODE = re.compile(r"\bmode:\s*(portable|adapted|degraded)\b")


def frontmatter(path: Path, issues: list[str]) -> str:
    try:
        source = path.read_text(encoding="utf-8")
    except OSError as exc:
        issues.append(f"unreadable: {path}: {exc.__class__.__name__}")
        return ""
    lines = source.splitlines()
    if not lines or lines[0].strip() != "---":
        issues.append(f"frontmatter missing: {path}")
        return ""
    try:
        close = next(i for i, line in enumerate(lines[1:30], 1) if line.strip() == "---")
    except StopIteration:
        issues.append(f"frontmatter unclosed: {path}")
        return ""
    return "\n".join(lines[1:close])


def audit_port(root: Path, expected_skills: int = 103, expected_agents: int = 16) -> list[str]:
    """Return actionable structural errors. No commands, network or mutations."""
    issues: list[str] = []
    manifest = root / "PORTING_MANIFEST.md"
    try:
        text = manifest.read_text(encoding="utf-8")
        skills_part = text.split("## Skills — 103 identities", 1)[1]
        skills_part, agents_part = skills_part.split("## Agents — 16 identities", 1)
        agents_part = agents_part.split("## Upstream evidence boundary", 1)[0]
    except (OSError, IndexError, ValueError):
        return ["missing or unparseable Engineer PORTING_MANIFEST.md sections"]

    skill_rows = SKILL_ROW.findall(skills_part)
    agent_rows = AGENT_ROW.findall(agents_part)
    skill_states = dict(skill_rows)
    agent_states = dict(agent_rows)
    if len(skill_rows) != expected_skills or len(skill_states) != len(skill_rows):
        issues.append(f"skill ledger: {len(skill_rows)} rows, {len(skill_states)} unique; expected {expected_skills}")
    if len(agent_rows) != expected_agents or len(agent_states) != len(agent_rows):
        issues.append(f"agent ledger: {len(agent_rows)} rows, {len(agent_states)} unique; expected {expected_agents}")

    skills_dir = root / "skills"
    actual_skills = {
        item.name for item in skills_dir.iterdir() if item.is_dir()
    } if skills_dir.is_dir() else set()
    if actual_skills != set(skill_states):
        issues.append(
            f"skill identity drift: missing={sorted(set(skill_states) - actual_skills)}, "
            f"extra={sorted(actual_skills - set(skill_states))}"
        )

    agents_dir = root / "agents"
    actual_agents = {
        item.stem for item in agents_dir.glob("*.md") if item.name != "README.md"
    } if agents_dir.is_dir() else set()
    if actual_agents != set(agent_states):
        issues.append(
            f"agent identity drift: missing={sorted(set(agent_states) - actual_agents)}, "
            f"extra={sorted(actual_agents - set(agent_states))}"
        )

    for name, status in skill_rows:
        path = skills_dir / name / "SKILL.md"
        header = frontmatter(path, issues)
        if not header:
            continue
        declared = NAME.search(header)
        if not declared or declared.group(1) != name:
            issues.append(f"skill name mismatch: {name} ({declared.group(1) if declared else 'missing'})")
        if not re.search(r"^description:", header, flags=re.MULTILINE):
            issues.append(f"skill description missing: {name}")
        mode = MODE.search(header)
        if status == "REVIEW_PENDING":
            issues.append(f"skill still unreviewed: {name}")
        elif not mode or mode.group(1) != STATUS_MODE[status]:
            issues.append(f"mode mismatch: {name} manifest={status} frontmatter={mode.group(1) if mode else 'missing'}")
        try:
            content = path.read_text(encoding="utf-8")
        except OSError:
            continue
        for ref in set(LOCAL_REF.findall(content)):
            ref_root = (skills_dir / name / "references").resolve()
            relative = (skills_dir / name / ref).resolve()
            if not relative.is_relative_to(ref_root):
                issues.append(f"unsafe local reference traversal: {name}/{ref}")
            elif not relative.is_file():
                issues.append(f"missing local reference: {name}/{ref}")

    # Check actual Markdown links throughout the bundle, including support references.
    for document in root.rglob("*.md"):
        if document.name == "PORTING_MANIFEST.md":
            continue
        try:
            body = document.read_text(encoding="utf-8")
        except OSError as exc:
            issues.append(f"unreadable markdown: {document}: {exc.__class__.__name__}")
            continue
        for match in MARKDOWN_LINK.finditer(body):
            target = match.group(1).strip().split(" ", 1)[0].strip("<>")
            if not target or target.startswith(("https:", "http:", "mailto:", "data:", "#", "/")):
                continue
            path_part = target.split("#", 1)[0].split("?", 1)[0]
            if not path_part or Path(path_part).suffix.lower() not in LOCAL_EXTENSIONS:
                continue
            target_path = (document.parent / path_part).resolve()
            if not target_path.is_relative_to(root.resolve()):
                continue  # Caller-repository links are outside this package's scope.
            if not target_path.is_file():
                line = body.count("\n", 0, match.start()) + 1
                issues.append(f"broken markdown link: {document.relative_to(root)}:{line} -> {target}")

    for name, status in agent_rows:
        path = agents_dir / f"{name}.md"
        header = frontmatter(path, issues)
        if not header:
            continue
        declared = NAME.search(header)
        if not declared or declared.group(1) != name:
            issues.append(f"agent name mismatch: {name}")
        if status == "REVIEW_PENDING":
            issues.append(f"agent still unreviewed: {name}")

    if expected_skills == 103:
        accepted = sum(s != "REVIEW_PENDING" for _, s in skill_rows)
        advertised = re.search(
            r"Current accepted coverage: \*\*(\d+) / (\d+) Skill identities reviewed semantically\*\*",
            text,
        )
        if not advertised or (int(advertised.group(1)), int(advertised.group(2))) != (accepted, 103):
            issues.append(f"coverage summary inconsistent: accepted={accepted}/103")
        for status in (*STATUS_MODE, "REVIEW_PENDING"):
            rows = {name for name, state in skill_rows if state == status}
            summary = re.search(
                rf"^- \*\*(\d+) {status}\*\*: (.*)$",
                text, flags=re.MULTILINE,
            )
            if not summary or int(summary.group(1)) != len(rows):
                issues.append(f"status count inconsistent: {status}")
            elif status != "REVIEW_PENDING":
                names = set(re.findall(r"`(ak-[a-z0-9-]+)`", summary.group(2)))
                if names != rows:
                    issues.append(f"status list inconsistent: {status}")

    return sorted(set(issues))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    errors = audit_port(args.root)
    report = {"ok": not errors, "expected_skills": 103, "expected_agents": 16, "errors": errors,
              "proof_level": "structural_only"}
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print("Engineer structural audit: " + ("PASS" if not errors else "FAIL"))
        for error in errors:
            print("  - " + error)
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
