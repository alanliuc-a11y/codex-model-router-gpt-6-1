#!/usr/bin/env python3
"""Release packaging: generate both manifests using LF-normalized text hashes."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILES = ["SKILL.md", "GLOBAL-ROUTING.md", "agents/openai.yaml",
         "scripts/global-routing.ps1", "scripts/global-routing.sh",
         "scripts/router-update.py", "references/updating.md"]


def build(root, profile, path):
    manifest = {"schema": 1, "version": "1.2.0",
                "repository": "alanliuc-a11y/codex-model-router-gpt-6-1",
                "profile": profile, "source_path": path,
                "files": {name: hashlib.sha256((root / name).read_bytes().replace(b"\r\n", b"\n")).hexdigest()
                          for name in FILES}}
    (root / "version.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build(ROOT, "model-router", ".")
    build(ROOT / "profiles/20-usd", "model-router-20", "profiles/20-usd")
