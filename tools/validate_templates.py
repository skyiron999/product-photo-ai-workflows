from __future__ import annotations

import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

REQUIRED_FIELDS = {
    "id",
    "name",
    "kind",
    "version",
    "compatible_with",
    "recommended_for",
    "outputs",
}
VALID_KINDS = {"product", "style", "output"}
VALID_PLATFORMS = {"chatgpt", "gemini", "claude"}
ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SEMVER_PATTERN = re.compile(r"^\d+\.\d+\.\d+$")
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
FENCE_PATTERN = re.compile(r"^[ \t]{0,3}(`{3,}|~{3,})")
PLACEHOLDER_PATTERN = re.compile(
    r"\b(?:TODO|TBD|YOUR\s+(?:TEXT|STYLE|ID|NAME))\b",
    re.IGNORECASE,
)
REQUIRED_HEADINGS = {
    "product": {"## Detect", "## Lock", "## Risks", "## QA"},
    "style": {
        "## Visual intent",
        "## Background",
        "## Lighting",
        "## Preserve",
        "## Avoid",
    },
    "output": {"## Purpose", "## Composition", "## Constraints", "## QA"},
}


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
    try:
        parsed = yaml.safe_load(raw_metadata)
    except yaml.YAMLError as exc:
        raise FrontMatterError(f"invalid YAML: {exc}") from exc
    if not isinstance(parsed, dict):
        raise FrontMatterError("front matter must be a YAML mapping")

    body = "\n".join(lines[closing_index + 1 :]).lstrip()
    return parsed, body


def discover_templates(root: Path) -> list[Path]:
    paths: list[Path] = []
    for directory in ("products", "styles", "outputs"):
        candidate = root / directory
        if candidate.exists():
            paths.extend(sorted(candidate.glob("*.md")))
    return paths


def _validate_metadata(path: Path, metadata: dict[str, Any]) -> list[Issue]:
    issues: list[Issue] = []
    missing = sorted(REQUIRED_FIELDS - metadata.keys())
    if missing:
        issues.append(Issue(path, f"missing required metadata: {', '.join(missing)}"))
        return issues

    template_id = metadata["id"]
    if not isinstance(template_id, str) or not ID_PATTERN.fullmatch(template_id):
        issues.append(Issue(path, "id must use lowercase kebab-case"))
    if metadata["kind"] not in VALID_KINDS:
        issues.append(Issue(path, f"invalid kind '{metadata['kind']}'"))
    if not isinstance(metadata["version"], str) or not SEMVER_PATTERN.fullmatch(
        metadata["version"]
    ):
        issues.append(Issue(path, "version must use semantic versioning"))

    list_fields: dict[str, list[str]] = {}
    for field in ("compatible_with", "recommended_for", "outputs"):
        value = metadata[field]
        if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
            issues.append(Issue(path, f"{field} must be a list of strings"))
            list_fields[field] = []
        else:
            list_fields[field] = value

    unknown_platforms = set(list_fields["compatible_with"]) - VALID_PLATFORMS
    if unknown_platforms:
        issues.append(
            Issue(path, f"unknown platforms: {', '.join(sorted(unknown_platforms))}")
        )
    return issues


def _validate_body(path: Path, metadata: dict[str, Any], body: str) -> list[Issue]:
    issues: list[Issue] = []
    kind = metadata.get("kind")
    if kind in REQUIRED_HEADINGS:
        missing = [
            heading for heading in sorted(REQUIRED_HEADINGS[kind]) if heading not in body
        ]
        if missing:
            issues.append(Issue(path, f"missing required headings: {', '.join(missing)}"))
    if path.name != "_template.md" and PLACEHOLDER_PATTERN.search(body):
        issues.append(Issue(path, "publishable placeholder found"))
    return issues


def _without_fenced_code(text: str) -> str:
    visible_lines: list[str] = []
    fence_character: str | None = None
    minimum_fence_length = 0

    for line in text.splitlines():
        match = FENCE_PATTERN.match(line)
        token = match.group(1) if match else ""
        if fence_character is None:
            if token:
                fence_character = token[0]
                minimum_fence_length = len(token)
                visible_lines.append("")
            else:
                visible_lines.append(line)
            continue

        if (
            token
            and token[0] == fence_character
            and len(token) >= minimum_fence_length
        ):
            fence_character = None
            minimum_fence_length = 0
        visible_lines.append("")

    return "\n".join(visible_lines)


def _validate_links(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    for path in sorted(root.rglob("*.md")):
        text = _without_fenced_code(path.read_text(encoding="utf-8"))
        for target in LINK_PATTERN.findall(text):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            clean_target = target.split("#", 1)[0]
            if clean_target and not (path.parent / clean_target).resolve().exists():
                issues.append(Issue(path, f"broken relative link: {target}"))
    return issues


def validate_repository(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    ids: dict[tuple[str, str], list[Path]] = defaultdict(list)
    records: list[tuple[Path, dict[str, Any]]] = []

    for path in discover_templates(root):
        try:
            metadata, body = parse_front_matter(path)
        except FrontMatterError as exc:
            issues.append(Issue(path, str(exc)))
            continue
        issues.extend(_validate_metadata(path, metadata))
        issues.extend(_validate_body(path, metadata, body))
        records.append((path, metadata))
        if isinstance(metadata.get("kind"), str) and isinstance(metadata.get("id"), str):
            ids[(metadata["kind"], metadata["id"])].append(path)

    for (_, template_id), paths in ids.items():
        if len(paths) > 1:
            for path in paths:
                issues.append(Issue(path, f"duplicate id '{template_id}'"))

    known_products = {
        metadata["id"]
        for path, metadata in records
        if path.name != "_template.md" and metadata.get("kind") == "product"
    }
    known_outputs = {
        metadata["id"]
        for path, metadata in records
        if path.name != "_template.md" and metadata.get("kind") == "output"
    }
    for path, metadata in records:
        if path.name == "_template.md":
            continue
        recommended_for = metadata.get("recommended_for")
        outputs = metadata.get("outputs")
        product_refs = recommended_for if isinstance(recommended_for, list) else []
        output_refs = outputs if isinstance(outputs, list) else []
        unknown_products = set(product_refs) - known_products
        unknown_outputs = set(output_refs) - known_outputs
        if unknown_products:
            issues.append(
                Issue(path, f"unknown products: {', '.join(sorted(unknown_products))}")
            )
        if unknown_outputs:
            issues.append(
                Issue(path, f"unknown outputs: {', '.join(sorted(unknown_outputs))}")
            )

    issues.extend(_validate_links(root))
    return sorted(issues, key=lambda issue: (str(issue.path), issue.message))


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    issues = validate_repository(root)
    if issues:
        for issue in issues:
            print(issue)
        print(f"Validation failed with {len(issues)} issue(s).")
        return 1
    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
