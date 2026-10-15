#!/usr/bin/env python3
"""Search Python AST definitions and candidate usages in a local Git checkout.

Read-only/offline subset. NOT GitLab Knowledge Graph, LSP, or a call graph.
"""
from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path
import re
import subprocess
import sys


IDENTIFIER = re.compile(r"^[A-Za-z_][A-Za-z_0-9]*$")


def git(root: Path, *args: str) -> bytes:
    return subprocess.run(["git", "-C", str(root), *args], capture_output=True,
                          check=True, timeout=20).stdout


class SymbolVisitor(ast.NodeVisitor):
    def __init__(self, symbol: str, path: str):
        self.symbol = symbol
        self.path = path
        self.scope: list[str] = []
        self.definitions: list[dict] = []
        self.uses: list[dict] = []

    def record_definition(self, name: str, node: ast.AST, kind: str) -> None:
        if name == self.symbol:
            qualified = ".".join([*self.scope, name])
            self.definitions.append({"path": self.path, "line": node.lineno,
                                     "column": node.col_offset, "qualified": qualified,
                                     "kind": kind})

    def scoped(self, name: str, node: ast.AST, kind: str) -> None:
        self.record_definition(name, node, kind)
        self.scope.append(name)
        self.generic_visit(node)
        self.scope.pop()

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        self.scoped(node.name, node, "class")

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self.scoped(node.name, node, "function")

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        self.scoped(node.name, node, "async_function")

    def visit_Name(self, node: ast.Name) -> None:
        if node.id == self.symbol and isinstance(node.ctx, ast.Load):
            self.uses.append({"path": self.path, "line": node.lineno,
                              "column": node.col_offset, "kind": "name_load"})
        self.generic_visit(node)

    def visit_Attribute(self, node: ast.Attribute) -> None:
        if node.attr == self.symbol and isinstance(node.ctx, ast.Load):
            self.uses.append({"path": self.path, "line": node.lineno,
                              "column": node.col_offset, "kind": "attribute_load"})
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        for alias in node.names:
            if alias.name == self.symbol or alias.asname == self.symbol:
                self.uses.append({"path": self.path, "line": node.lineno,
                                  "column": node.col_offset, "kind": "import_binding"})
        self.generic_visit(node)

    def visit_Import(self, node: ast.Import) -> None:
        for alias in node.names:
            if alias.name.split(".")[-1] == self.symbol or alias.asname == self.symbol:
                self.uses.append({"path": self.path, "line": node.lineno,
                                  "column": node.col_offset, "kind": "import_binding"})
        self.generic_visit(node)


def scan(root: Path, symbol: str, max_files: int = 800,
         max_bytes: int = 250_000, mode: str = "both") -> dict:
    if not IDENTIFIER.fullmatch(symbol):
        raise ValueError("symbol must be a single valid Python identifier")
    root = root.resolve(strict=True)
    top = Path(git(root, "rev-parse", "--show-toplevel").decode("utf-8").strip()).resolve()
    if top != root:
        raise ValueError("select the exact local Git worktree root")
    all_files = sorted(set(
        x.decode("utf-8", "replace") for x in
        git(root, "ls-files", "-z", "--cached", "--others", "--exclude-standard").split(b"\0")
        if x and x.endswith(b".py")
    ))
    definitions: list[dict] = []
    uses: list[dict] = []
    skipped: list[dict] = []
    indexed = 0
    for rel in all_files:
        path = root / rel
        if indexed >= max_files:
            skipped.append({"path": rel, "reason": "file_limit"})
            continue
        try:
            resolved = path.resolve(strict=True)
            if path.is_symlink() or not resolved.is_relative_to(root) or not path.is_file():
                skipped.append({"path": rel, "reason": "symlink_or_nonlocal"})
                continue
            if path.stat().st_size > max_bytes:
                skipped.append({"path": rel, "reason": "oversized"})
                continue
            data = path.read_text(encoding="utf-8")
            syntax = ast.parse(data, filename=rel)
        except (OSError, UnicodeDecodeError, SyntaxError, RecursionError, ValueError) as exc:
            skipped.append({"path": rel, "reason": type(exc).__name__})
            continue
        visitor = SymbolVisitor(symbol, rel)
        visitor.visit(syntax)
        indexed += 1
        definitions.extend(visitor.definitions)
        uses.extend(visitor.uses)
    return {
        "symbol": symbol, "language": "python",
        "mode": mode,
        "definitions": definitions if mode != "uses" else [],
        "possible_uses": uses if mode != "definitions" else [],
        "index": {"files_seen": len(all_files), "files_parsed": indexed,
                  "skipped": skipped, "complete_python_parse": not skipped},
        "limitations": [
            "AST name/attribute matches are possible uses, not resolved call edges",
            "dynamic dispatch, reflection, aliases and external dependencies are not resolved",
            "only local Git Python files are read; ignored files and other languages not searched",
            "missing results never prove absence of callers or security impact",
        ],
        "source": "local_python_ast_no_network",
    }


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--root", type=Path, default=Path("."))
    p.add_argument("--symbol", required=True)
    p.add_argument("--mode", choices=("definitions", "uses", "both"), default="both")
    p.add_argument("--max-files", type=int, default=800)
    p.add_argument("--max-file-bytes", type=int, default=250_000)
    args = p.parse_args(argv)
    if args.max_files < 1 or args.max_file_bytes < 1:
        p.error("limits must be positive")
    try:
        result = scan(args.root, args.symbol, args.max_files,
                      args.max_file_bytes, args.mode)
    except (OSError, ValueError, subprocess.SubprocessError) as exc:
        print(f"gkg AST fallback: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
