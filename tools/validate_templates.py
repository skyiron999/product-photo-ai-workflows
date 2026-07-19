from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


class FrontMatterError(ValueError):
    """Raised when a Markdown template has invalid YAML front matter."""


@dataclass(frozen=True)
class Issue:
    path: Path
    message: str

    def __str__(self) -> str:
        return f"{self.path}: {self.message}"


def parse_front_matter(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise FrontMatterError("missing opening YAML delimiter")

    try:
        closing_index = lines[1:].index("---") + 1
    except ValueError as exc:
        raise FrontMatterError("missing closing YAML delimiter") from exc

    raw_metadata = "\n".join(lines[1:closing_index])
    parsed = yaml.safe_load(raw_metadata)
    if not isinstance(parsed, dict):
        raise FrontMatterError("front matter must be a YAML mapping")

    body = "\n".join(lines[closing_index + 1 :]).lstrip()
    return parsed, body


def main() -> int:
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
