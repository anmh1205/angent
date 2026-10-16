#!/usr/bin/env python3
"""Make one byte-reproducible all-target ZIP from six independently valid ZIPs."""
from __future__ import annotations

import argparse
import hashlib
import io
from pathlib import Path
import sys
import zipfile

FILES = (
    "angent-claude-code.zip",
    "angent-gemini-extension.zip",
    "angent-gemini-skills.zip",
    "angent-local-agent.zip",
    "angent-openai-plugin.zip",
    "angent-chatgpt.zip",
)
COMBINED = "angent-all-targets.zip"
TIMESTAMP = (2020, 1, 1, 0, 0, 0)


def build(directory: Path) -> dict[str, str]:
    directory = directory.resolve()
    items = {}
    for name in FILES:
        path = directory / name
        if not path.is_file() or path.is_symlink():
            raise ValueError(f"Missing/unsafe ZIP: {name}")
        content = path.read_bytes()
        with zipfile.ZipFile(io.BytesIO(content)) as z:
            if z.testzip() is not None:
                raise ValueError(f"Corrupt ZIP: {name}")
        items[name] = content
    digests = {name: hashlib.sha256(content).hexdigest() for name, content in items.items()}
    checksums = "".join(f"{digests[name]}  {name}\n" for name in FILES).encode()
    items["SHA256SUMS"] = checksums
    output = directory / COMBINED
    if output.is_symlink():
        raise ValueError("Refusing symlink output")
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for name, content in sorted(items.items()):
            entry = zipfile.ZipInfo(name, TIMESTAMP)
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            z.writestr(entry, content, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    return digests


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dist", type=Path, default=Path("dist"))
    args = parser.parse_args()
    try:
        digests = build(args.dist)
    except (ValueError, OSError, zipfile.BadZipFile) as exc:
        print(f"All-target package invalid: {exc}", file=sys.stderr)
        return 1
    print(f"Created {args.dist / COMBINED} containing {len(digests)} independent ZIPs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
