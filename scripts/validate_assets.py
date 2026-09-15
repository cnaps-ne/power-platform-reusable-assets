#!/usr/bin/env python3
"""Dependency-free validation for curated public assets."""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors = []

for path in ROOT.rglob("*.json"):
    try:
        json.loads(path.read_text(encoding="utf-8-sig"))
    except Exception as exc:  # noqa: BLE001
        errors.append(f"Invalid JSON: {path.relative_to(ROOT)}: {exc}")

for path in ROOT.rglob("*.controls.yaml"):
    text = path.read_text(encoding="utf-8-sig")
    if not text.lstrip().startswith(("#", "-")):
        errors.append(f"Unexpected YAML fragment start: {path.relative_to(ROOT)}")
    if "Control:" not in text or "Properties:" not in text:
        errors.append(f"Missing control structure: {path.relative_to(ROOT)}")

placeholder_rules = {
    "APP_WEB_LINK": ROOT / "sharepoint/column-formatting/power-app-deep-link.json",
    "FLOW_ID": ROOT / "sharepoint/column-formatting/trigger-flow.json",
}
for placeholder, expected_path in placeholder_rules.items():
    matches = [p for p in ROOT.rglob("*") if p.is_file() and placeholder in p.read_text(encoding="utf-8-sig", errors="ignore")]
    if expected_path not in matches:
        errors.append(f"Expected placeholder missing: {placeholder}")

secret_patterns = [
    re.compile(r"(?i)(client_secret|api[_-]?key|password)\s*[:=]\s*[^<\s][^\s]{7,}"),
    re.compile(r"https://[^/\s]+\.sharepoint\.com/sites/", re.I),
]
for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue
    text = path.read_text(encoding="utf-8-sig", errors="ignore")
    for pattern in secret_patterns:
        if pattern.search(text):
            errors.append(f"Potential tenant/secret material: {path.relative_to(ROOT)}")

if errors:
    print("\n".join(errors))
    sys.exit(1)

print("Validated JSON, local YAML fragment structure, placeholders and public-boundary checks.")
