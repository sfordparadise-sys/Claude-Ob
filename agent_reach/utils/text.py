"""UTF-8-safe text helpers for cross-platform file operations."""

from __future__ import annotations

from pathlib import Path


def read_utf8_text(path: str | Path, default: str = "") -> str:
    target = Path(path)
    if not target.exists():
        return default
    return target.read_text(encoding="utf-8", errors="replace")
