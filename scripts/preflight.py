#!/usr/bin/env python3
"""Fail closed until a verified source registry and ingestion adapter are implemented."""

import json
from pathlib import Path

registry = Path("sources.json")
if not registry.is_file():
    raise SystemExit("Missing sources.json. Copy the example only after verifying official API access and implementing an adapter.")

try:
    config = json.loads(registry.read_text(encoding="utf-8"))
except (OSError, json.JSONDecodeError) as exc:
    raise SystemExit(f"Invalid sources.json: {exc}") from exc

if config.get("version") != 1 or not isinstance(config.get("sources"), list) or not config["sources"]:
    raise SystemExit("No verified government API sources configured; refusing to report a successful sync.")

raise SystemExit("Source registry is present, but no source adapters or SchemePulse ingest client have been implemented yet.")
