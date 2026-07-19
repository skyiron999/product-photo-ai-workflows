# Product Photo AI Workflows Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and publish an English-first, Vietnamese-supported open-source workflow kit for faithful product-background editing inside ChatGPT, Gemini, and Claude.

**Architecture:** Store behavioral rules in a shared Markdown core, platform-specific setup and runtime adapters under `platforms/`, and extensible product/style/output templates as Markdown with YAML front matter. A small Python validator and GitHub Actions workflow enforce schema, content contracts, links, and contribution quality without being required by normal workflow users.

**Tech Stack:** Markdown, YAML front matter, Python 3.11+, PyYAML 6.x, pytest 8.x, GitHub Actions, Git.

## Global Constraints

- Repository name: `product-photo-ai-workflows`.
- License: MIT.
- English is canonical; `README.vi.md` must preserve the same positioning and practical meaning.
- Version 1 implements only product-photo background replacement.
- Version 1 is optimized for flat-lay and tabletop product photography; ghost mannequin and on-model workflows are deferred.
- The original product source outranks all style and user-level creative requests.
- Every output and repair starts from the original product source, never from a generated derivative.
- Product color grading is isolated from background grading; do not infer exact Hex/RGB values without calibrated user input.
- Preserve the source canvas ratio by default; requested ratio changes extend the background before any crop and never rescale or distort the product.
- Ecommerce targets at least 15% safe padding when possible without altering product geometry.
- Reference text, logos, brand marks, watermarks, captions, and typographic decoration are excluded from style extraction.
- Users identify images by chat role; filenames must not be required or standardized.
- Simultaneous unlabeled uploads require a proposed role mapping and user confirmation; do not use pseudo-precise confidence percentages.
- Each platform workflow is self-contained and must not silently redirect the user to another platform.
- Initial products: garments, fabric, earrings, bracelets, and reflective accessories.
- Initial styles: sage minimal flat lay, clean white studio, warm beige editorial, and dark luxury jewelry.
- Initial outputs: ecommerce and social.
- Public example assets require documented redistribution rights.
- README quality is a release requirement: professional, visually literate, commercially relevant, fashion-forward, honest about limitations, and approachable to non-technical users.
- Do not claim perfect fidelity or feature parity across platforms.

---

## File Responsibility Map

| Area | Responsibility |
|---|---|
| `core/` | Platform-independent behavior, precedence, run modes, QA, and repair semantics |
| `platforms/chatgpt/`, `platforms/gemini/`, `platforms/claude/` | Setup, copy-paste bootstrap, persistent instructions, and current limitations for one interface |
| `products/` | Category-specific product invariants and risk checks |
| `styles/` | Reusable background, lighting, palette, material, and mood interpretations |
| `outputs/` | Ecommerce and social composition constraints |
| `examples/` | Redistributable end-to-end examples with provenance and QA evidence |
| `tests/cases/` | Manual visual test case definitions for each product category |
| `tests/synthetic_cases/` | Supplemental controlled cutout tests for edges, contact shadows, and lighting integration |
| `tools/validate_templates.py` | Repository schema, contract, link, and placeholder validation |
| `tests/` | Automated validator and documentation-contract tests |
| `.github/workflows/validate.yml` | Pull-request and main-branch validation |
| `README*` and `QUICKSTART.md` | Professional product narrative and shortest path to a first run |

---

### Task 1: Establish Python Validation Foundation

**Files:**
- Create: `.gitignore`
- Create: `pyproject.toml`
- Create: `tools/__init__.py`
- Create: `tools/validate_templates.py`
- Create: `tests/test_validate_templates.py`

**Interfaces:**
- Produces: `parse_front_matter(path: Path) -> tuple[dict[str, Any], str]`
- Produces: `Issue(path: Path, message: str)`
- Produces: CLI entry point `python tools/validate_templates.py .`
- Consumes: no earlier task output

- [ ] **Step 1: Write the failing front-matter parser tests**

Create `tests/test_validate_templates.py` with:

```python
from pathlib import Path

import pytest

from tools.validate_templates import FrontMatterError, parse_front_matter


def test_parse_front_matter_returns_metadata_and_body(tmp_path: Path) -> None:
    template = tmp_path / "style.md"
    template.write_text(
        """---
id: sage-minimal-flatlay
name: Sage Minimal Flat Lay
kind: style
version: 1.0.0
compatible_with: [chatgpt, gemini, claude]
recommended_for: [garments, fabric]
outputs: [ecommerce, social]
---
# Sage Minimal Flat Lay
""",
        encoding="utf-8",
    )

    metadata, body = parse_front_matter(template)

    assert metadata["id"] == "sage-minimal-flatlay"
    assert metadata["compatible_with"] == ["chatgpt", "gemini", "claude"]
    assert body.startswith("# Sage Minimal Flat Lay")


def test_parse_front_matter_rejects_missing_delimiter(tmp_path: Path) -> None:
    template = tmp_path / "broken.md"
    template.write_text("# No front matter\n", encoding="utf-8")

    with pytest.raises(FrontMatterError, match="opening YAML delimiter"):
        parse_front_matter(template)
```

- [ ] **Step 2: Run the tests and verify the expected failure**

Run:

```bash
python -m pytest tests/test_validate_templates.py -v
```

Expected: collection fails because `tools.validate_templates` does not exist.

- [ ] **Step 3: Add project metadata and minimal parser implementation**

Create `pyproject.toml`:

```toml
[build-system]
requires = ["setuptools>=75"]
build-backend = "setuptools.build_meta"

[project]
name = "product-photo-ai-workflows"
version = "0.1.0"
description = "Platform-native workflows for faithful AI product photo editing"
requires-python = ">=3.11"
dependencies = ["PyYAML>=6.0,<7"]
license = { text = "MIT" }

[project.optional-dependencies]
dev = ["pytest>=8,<9"]

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-q"
```

Create `.gitignore`:

```gitignore
__pycache__/
*.py[cod]
.pytest_cache/
.venv/
dist/
build/
*.egg-info/
.DS_Store
```

Create an empty `tools/__init__.py` and create `tools/validate_templates.py`:

```python
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
```

- [ ] **Step 4: Install development dependencies and verify parser tests pass**

Run:

```bash
python -m pip install -e '.[dev]'
python -m pytest tests/test_validate_templates.py -v
```

Expected: `2 passed`.

- [ ] **Step 5: Commit the validation foundation**

```bash
git add .gitignore pyproject.toml tools tests/test_validate_templates.py
git commit -m "build: add template validation foundation"
```

---

### Task 2: Implement Repository Validation and CI

**Files:**
- Modify: `tools/validate_templates.py`
- Modify: `tests/test_validate_templates.py`
- Create: `.github/workflows/validate.yml`

**Interfaces:**
- Consumes: `parse_front_matter`, `Issue`
- Produces: `discover_templates(root: Path) -> list[Path]`
- Produces: `validate_repository(root: Path) -> list[Issue]`
- Produces: CLI exit `0` on success and `1` on validation errors

- [ ] **Step 1: Add failing tests for required metadata, duplicate IDs, placeholders, headings, and links**

Append tests that create temporary `products/`, `styles/`, and `outputs/` trees. Use this helper:

```python
def write_template(path: Path, *, template_id: str, kind: str, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"""---
id: {template_id}
name: Test Template
kind: {kind}
version: 1.0.0
compatible_with: [chatgpt, gemini, claude]
recommended_for: [garments]
outputs: [ecommerce]
---
{body}
""",
        encoding="utf-8",
    )
```

Add these assertions:

```python
from tools.validate_templates import validate_repository


def test_validate_repository_reports_duplicate_ids(tmp_path: Path) -> None:
    body = "# Template\n\n## Detect\n\n## Lock\n\n## Risks\n\n## QA\n"
    write_template(tmp_path / "products/a.md", template_id="garments", kind="product", body=body)
    write_template(tmp_path / "products/b.md", template_id="garments", kind="product", body=body)

    issues = validate_repository(tmp_path)

    assert any("duplicate id 'garments'" in issue.message for issue in issues)


def test_validate_repository_reports_publishable_placeholders(tmp_path: Path) -> None:
    body = "# Template\n\n## Visual intent\nTODO\n## Background\nText\n## Lighting\nText\n## Preserve\nText\n## Avoid\nText\n"
    write_template(tmp_path / "styles/broken.md", template_id="broken", kind="style", body=body)

    issues = validate_repository(tmp_path)

    assert any("publishable placeholder" in issue.message for issue in issues)


def test_validate_repository_allows_placeholders_in_underscore_template(tmp_path: Path) -> None:
    body = "# YOUR STYLE\n\n## Visual intent\nYOUR TEXT\n## Background\nYOUR TEXT\n## Lighting\nYOUR TEXT\n## Preserve\nYOUR TEXT\n## Avoid\nYOUR TEXT\n"
    write_template(tmp_path / "styles/_template.md", template_id="style-template", kind="style", body=body)

    issues = validate_repository(tmp_path)

    assert not any("publishable placeholder" in issue.message for issue in issues)


def test_validate_repository_reports_broken_relative_link(tmp_path: Path) -> None:
    readme = tmp_path / "README.md"
    readme.write_text("[Missing](docs/missing.md)\n", encoding="utf-8")

    issues = validate_repository(tmp_path)

    assert any("broken relative link" in issue.message for issue in issues)
```

- [ ] **Step 2: Run the new tests and verify they fail**

Run:

```bash
python -m pytest tests/test_validate_templates.py -v
```

Expected: failures because `validate_repository` is undefined.

- [ ] **Step 3: Implement validation rules and CLI output**

Add constants and functions to `tools/validate_templates.py`:

```python
import re
import sys
from collections import defaultdict

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
PLACEHOLDER_PATTERN = re.compile(r"\b(?:TODO|TBD|YOUR\s+(?:TEXT|STYLE|ID|NAME))\b", re.IGNORECASE)
REQUIRED_HEADINGS = {
    "product": {"## Detect", "## Lock", "## Risks", "## QA"},
    "style": {"## Visual intent", "## Background", "## Lighting", "## Preserve", "## Avoid"},
    "output": {"## Purpose", "## Composition", "## Constraints", "## QA"},
}


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
    if not isinstance(metadata["version"], str) or not SEMVER_PATTERN.fullmatch(metadata["version"]):
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
        issues.append(Issue(path, f"unknown platforms: {', '.join(sorted(unknown_platforms))}"))
    return issues


def _validate_body(path: Path, metadata: dict[str, Any], body: str) -> list[Issue]:
    issues: list[Issue] = []
    kind = metadata.get("kind")
    if kind in REQUIRED_HEADINGS:
        missing = [heading for heading in sorted(REQUIRED_HEADINGS[kind]) if heading not in body]
        if missing:
            issues.append(Issue(path, f"missing required headings: {', '.join(missing)}"))
    if path.name != "_template.md" and PLACEHOLDER_PATTERN.search(body):
        issues.append(Issue(path, "publishable placeholder found"))
    return issues


def _validate_links(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    for path in sorted(root.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
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
            issues.append(Issue(path, f"unknown products: {', '.join(sorted(unknown_products))}"))
        if unknown_outputs:
            issues.append(Issue(path, f"unknown outputs: {', '.join(sorted(unknown_outputs))}"))

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
```

- [ ] **Step 4: Run validator tests and verify they pass**

Run:

```bash
python -m pytest tests/test_validate_templates.py -v
```

Expected: all tests pass.

- [ ] **Step 5: Add GitHub Actions validation**

Create `.github/workflows/validate.yml`:

```yaml
name: Validate repository

on:
  pull_request:
  push:
    branches: [main]

permissions:
  contents: read

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
          cache: pip
      - run: python -m pip install -e '.[dev]'
      - run: python -m pytest -v
      - run: python tools/validate_templates.py .
```

- [ ] **Step 6: Commit validator and CI**

```bash
git add tools/validate_templates.py tests/test_validate_templates.py .github/workflows/validate.yml
git commit -m "ci: validate workflow templates and links"
```

---

### Task 3: Author the Shared Workflow Core

**Files:**
- Create: `core/product-lock.md`
- Create: `core/workflow-protocol.md`
- Create: `core/safe-run.md`
- Create: `core/fast-run.md`
- Create: `core/repair-loop.md`
- Create: `core/quality-check.md`
- Create: `tests/test_core_contracts.py`

**Interfaces:**
- Produces: canonical commands and precedence consumed by every platform adapter
- Produces: canonical `PASS`, `WARN`, `FAIL`, and `MANUAL REVIEW` semantics
- Consumes: global constraints only

- [ ] **Step 1: Write failing core documentation-contract tests**

Create `tests/test_core_contracts.py`:

```python
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_CORE_FILES = {
    "product-lock.md",
    "workflow-protocol.md",
    "safe-run.md",
    "fast-run.md",
    "repair-loop.md",
    "quality-check.md",
}


def test_all_core_files_exist() -> None:
    assert {path.name for path in (ROOT / "core").glob("*.md")} == REQUIRED_CORE_FILES


@pytest.mark.parametrize(
    "command",
    [
        "SAFE RUN",
        "FAST RUN",
        "ECOMMERCE",
        "SOCIAL",
        "BOTH",
        "CONTINUE",
        "NEXT PRODUCT",
        "REPAIR PRODUCT",
        "REPAIR COLOR",
        "REPAIR DETAILS",
        "REPAIR EDGES",
        "REPAIR BACKGROUND",
        "REPAIR LIGHTING",
        "REPAIR COMPOSITION",
        "START OVER FROM SOURCE",
    ],
)
def test_protocol_defines_every_canonical_command(command: str) -> None:
    protocol = (ROOT / "core/workflow-protocol.md").read_text(encoding="utf-8")
    assert f"`{command}`" in protocol


def test_repair_loop_is_source_first_and_bounded() -> None:
    repair = (ROOT / "core/repair-loop.md").read_text(encoding="utf-8")
    assert "original product source" in repair
    assert "never repair from a generated output" in repair
    assert "MANUAL REVIEW" in repair


def test_product_lock_protects_color_without_claiming_uncalibrated_hex() -> None:
    text = (ROOT / "core/product-lock.md").read_text(encoding="utf-8")
    assert "background grading must not alter product color" in text
    assert "do not infer exact Hex or RGB values" in text


def test_protocol_confirms_unlabeled_image_roles() -> None:
    text = (ROOT / "core/workflow-protocol.md").read_text(encoding="utf-8")
    assert "simultaneous unlabeled uploads" in text
    assert "require confirmation before editing" in text
    assert "do not report a numeric confidence percentage" in text
```

- [ ] **Step 2: Run the core tests and verify failure**

Run:

```bash
python -m pytest tests/test_core_contracts.py -v
```

Expected: failure because `core/` does not exist.

- [ ] **Step 3: Write the six canonical core documents**

Use these exact responsibilities and clauses:

- `product-lock.md`: declare the original source authoritative; lock geometry, silhouette, arrangement, color, material, construction, text, logos, patterns, product counts, jewelry components, and identity details; explicitly prohibit copying products or props from the reference. Include the literal clauses `background grading must not alter product color` and `do not infer exact Hex or RGB values from an ordinary photograph without calibrated user input`.
- `workflow-protocol.md`: define intake, product analysis, lock, style extraction, render brief, edit, QA, repair, reset, precedence, and every canonical short command. For `simultaneous unlabeled uploads`, describe each image using observable features, propose roles, `require confirmation before editing`, and `do not report a numeric confidence percentage`.
- `safe-run.md`: require a visible lock sheet with `Product detected`, `Locked`, `Style extracted`, `Excluded from reference`, and `Risks`; wait for `CONTINUE`.
- `fast-run.md`: perform the same analysis internally; pause on ambiguous roles, multiple inseparable products, unreadable critical details, geometry conflicts, or unavailable platform capability.
- `repair-loop.md`: include the literal clauses `Return to the original product source.` and `Never repair from a generated output.`; allow one targeted repair, then Safe Run, then `MANUAL REVIEW`.
- `quality-check.md`: compare source/reference/output and define `PASS`, `WARN`, and `FAIL`; require explicit uncertainty for details that cannot be verified.

In `workflow-protocol.md`, state the precedence exactly:

```text
1. Product Lock core rules
2. Original product source image
3. Product Module
4. Output Profile
5. Style Card and style-reference image
6. Non-conflicting user requests
```

- [ ] **Step 4: Run core and repository validation**

Run:

```bash
python -m pytest tests/test_core_contracts.py -v
python tools/validate_templates.py .
```

Expected: core tests pass; repository validation passes because no publishable templates exist yet.

- [ ] **Step 5: Commit the shared core**

```bash
git add core tests/test_core_contracts.py
git commit -m "docs: define shared product editing workflow"
```

---

### Task 4: Add Product Modules and Output Profiles

**Files:**
- Create: `products/garments.md`
- Create: `products/fabric.md`
- Create: `products/earrings.md`
- Create: `products/bracelets.md`
- Create: `products/reflective-accessories.md`
- Create: `products/_template.md`
- Create: `outputs/ecommerce.md`
- Create: `outputs/social.md`
- Create: `outputs/_template.md`
- Create: `tests/test_template_catalog.py`

**Interfaces:**
- Produces product IDs: `garments`, `fabric`, `earrings`, `bracelets`, `reflective-accessories`
- Produces output IDs: `ecommerce`, `social`
- Consumes validator schema and Product Lock semantics

- [ ] **Step 1: Write failing catalog tests**

Create `tests/test_template_catalog.py`:

```python
from pathlib import Path

from tools.validate_templates import parse_front_matter

ROOT = Path(__file__).resolve().parents[1]


def template_ids(directory: str) -> set[str]:
    ids: set[str] = set()
    for path in (ROOT / directory).glob("*.md"):
        if path.name == "_template.md":
            continue
        metadata, _ = parse_front_matter(path)
        ids.add(metadata["id"])
    return ids


def test_initial_product_catalog_is_complete() -> None:
    assert template_ids("products") == {
        "garments",
        "fabric",
        "earrings",
        "bracelets",
        "reflective-accessories",
    }


def test_initial_output_catalog_is_complete() -> None:
    assert template_ids("outputs") == {"ecommerce", "social"}
```

- [ ] **Step 2: Run catalog tests and verify failure**

Run:

```bash
python -m pytest tests/test_template_catalog.py -v
```

Expected: failure because product and output directories do not exist.

- [ ] **Step 3: Create Product Modules with complete front matter and required headings**

Every product file must contain `## Detect`, `## Lock`, `## Risks`, and `## QA`.

For each publishable Product Module, set `kind: product`, set `recommended_for` to a one-item list containing its own ID, set `outputs` to `[ecommerce, social]`, and set all three platforms in `compatible_with`.

Required lock coverage:

- `garments.md`: silhouette, folds, seams, collar, sleeves, buttons, closures, labels, logos, pattern repetition, fabric thickness, texture, and color.
- `fabric.md`: cut edge, weave, knit, pile, translucency, drape, fold placement, printed pattern scale and repeat, and color.
- `earrings.md`: item count, pairing, symmetry, posts, hooks, clasps, stones, prongs, spacing, metal finish, and reflections.
- `bracelets.md`: circumference, band or chain geometry, visible links, charms, spacing, clasp, stones, metal finish, and reflections.
- `reflective-accessories.md`: geometry, engravings, polished edges, glass or stone transparency, metal color, highlights, and physically plausible background reflections.

The `_template.md` file uses explicit contributor tokens and explains all required headings. Its metadata ID is `product-template`, and it is excluded from the public catalog test.

- [ ] **Step 4: Create Output Profiles with exact behavioral boundaries**

Every output file contains `## Purpose`, `## Composition`, `## Constraints`, and `## QA`.

For both publishable outputs, set `kind: output`, set `recommended_for` to all five initial Product Module IDs, set `outputs` to a one-item list containing the profile's own ID, and set all three platforms in `compatible_with`.

`ecommerce.md` requires faithful representation, restrained background, clean silhouette, realistic grounding, no generated text, no watermark, and minimal reinterpretation. Preserve the source canvas ratio by default. When another ratio is requested, expand only the background before considering crop; never rescale, distort, or crop the product. Target at least 15% safe padding from the product's outermost edge when possible without altering product geometry.

`social.md` keeps Product Lock mandatory, permits stronger background mood, allows negative space, prohibits invented copy, and makes props opt-in. Ratio changes expand background first and never distort or crop the product.

`outputs/_template.md` documents the same contract with contributor tokens.

- [ ] **Step 5: Run catalog, validator, and full tests**

Run:

```bash
python -m pytest -v
python tools/validate_templates.py .
```

Expected: all tests and validation pass.

- [ ] **Step 6: Commit product and output modules**

```bash
git add products outputs tests/test_template_catalog.py
git commit -m "feat: add product locks and output profiles"
```

---

### Task 5: Add Initial Style Card Library

**Files:**
- Create: `styles/sage-minimal-flatlay.md`
- Create: `styles/clean-white-studio.md`
- Create: `styles/warm-beige-editorial.md`
- Create: `styles/dark-luxury-jewelry.md`
- Create: `styles/_template.md`
- Modify: `tests/test_template_catalog.py`

**Interfaces:**
- Produces style IDs consumed by quickstarts and examples
- Consumes Product Lock precedence and output IDs

- [ ] **Step 1: Add a failing initial-style catalog test**

Append:

```python
def test_initial_style_catalog_is_complete() -> None:
    assert template_ids("styles") == {
        "sage-minimal-flatlay",
        "clean-white-studio",
        "warm-beige-editorial",
        "dark-luxury-jewelry",
    }
```

- [ ] **Step 2: Run the catalog test and verify failure**

Run:

```bash
python -m pytest tests/test_template_catalog.py::test_initial_style_catalog_is_complete -v
```

Expected: failure because `styles/` is absent.

- [ ] **Step 3: Author four complete style cards**

Every style card contains `## Visual intent`, `## Background`, `## Lighting`, `## Preserve`, and `## Avoid`.

For each publishable style, set `kind: style`, `recommended_for` to the product IDs named below, `outputs` to `[ecommerce, social]`, and all three platforms in `compatible_with`:

- `sage-minimal-flatlay`: garments, fabric, earrings, bracelets;
- `clean-white-studio`: all five initial products;
- `warm-beige-editorial`: garments, fabric, earrings, bracelets;
- `dark-luxury-jewelry`: earrings, bracelets, reflective accessories.

Use these canonical visual definitions:

- `sage-minimal-flatlay`: pale desaturated sage matte surface; subtle paper-like grain; soft upper-left light; short diffused contact shadow; restrained editorial mood.
- `clean-white-studio`: neutral white-to-light-gray commercial surface; broad soft light; controlled highlights; clean grounding; no decorative props.
- `warm-beige-editorial`: warm beige matte surface; gentle directional light; low-to-medium contrast; tactile fashion-editorial mood; props only when explicitly requested.
- `dark-luxury-jewelry`: charcoal-to-black controlled surface; precise specular highlights; realistic reflections; luxury presentation; protect stone transparency and metal color.

Every `Preserve` section states that style cannot alter the product. Every `Avoid` section excludes all reference text, logos, brand marks, watermarks, captions, labels, typographic decoration, products, and props. Output remains text-free unless the user supplies exact text and explicitly requests it.

- [ ] **Step 4: Add contributor style template**

Create `styles/_template.md` with the required metadata and headings, plus short guidance that distinguishes visual intent, surface material, lighting, invariants, and avoid rules.

- [ ] **Step 5: Run validation and commit**

```bash
python -m pytest -v
python tools/validate_templates.py .
git add styles tests/test_template_catalog.py
git commit -m "feat: add initial background style cards"
```

Expected: tests and validation pass before commit.

---

### Task 6: Build the ChatGPT Platform Package

**Files:**
- Create: `platforms/chatgpt/setup.md`
- Create: `platforms/chatgpt/instant-run.md`
- Create: `platforms/chatgpt/installed-instructions.md`
- Create: `platforms/chatgpt/limitations.md`
- Create: `tests/test_platform_packages.py`

**Interfaces:**
- Consumes all core commands and template IDs
- Produces a self-contained ChatGPT path for Instant Run and Custom GPT installation

- [ ] **Step 1: Write failing platform-package tests**

Create `tests/test_platform_packages.py`:

```python
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
PLATFORM_FILES = {"setup.md", "instant-run.md", "installed-instructions.md", "limitations.md"}


@pytest.mark.parametrize("platform", ["chatgpt"])
def test_platform_package_is_complete(platform: str) -> None:
    package = ROOT / "platforms" / platform
    assert {path.name for path in package.glob("*.md")} == PLATFORM_FILES


def test_chatgpt_installed_instructions_include_core_safety_commands() -> None:
    text = (ROOT / "platforms/chatgpt/installed-instructions.md").read_text(encoding="utf-8")
    for phrase in ("original product source", "SAFE RUN", "FAST RUN", "NEXT PRODUCT", "MANUAL REVIEW"):
        assert phrase in text
```

- [ ] **Step 2: Run tests and verify failure**

Run:

```bash
python -m pytest tests/test_platform_packages.py -v
```

Expected: failure because `platforms/chatgpt/` is absent.

- [ ] **Step 3: Write ChatGPT setup and limitations docs**

`setup.md` must provide two paths:

1. Instant Run: paste `instant-run.md` into a new chat.
2. Install Once: create a Custom GPT, enable Image Generation, paste `installed-instructions.md` into Instructions, and upload core/product/style/output Markdown files as Knowledge.

Link to the official Custom GPT and ChatGPT Images documentation. State that creating/editing GPTs requires an eligible paid plan while using a shared GPT may have different availability.

`limitations.md` must state that edits can extend beyond a selected area, fidelity is not guaranteed, small text and jewelry details require review, usage limits vary, and a failed repair must restart from the source.

- [ ] **Step 4: Write copy-paste runtime instructions**

`instant-run.md` must be self-contained for the common reference-plus-target case. It must:

- assign image roles from the user's messages rather than filenames;
- implement precedence, source-first editing, Safe/Fast Run, output profiles, QA, repair limits, and reset behavior;
- auto-detect a product category and ask one short question only when ambiguous;
- when multiple images arrive unlabeled, propose a role mapping from observable features and require confirmation without claiming a numeric confidence score;
- never copy products or props from the reference;
- produce one independent output per target and never create a collage unless requested.

`installed-instructions.md` contains the same behavior but tells ChatGPT to consult uploaded Knowledge modules by their `id` and never allow Knowledge style content to override Product Lock.

- [ ] **Step 5: Run tests, validation, and commit**

```bash
python -m pytest -v
python tools/validate_templates.py .
git add platforms/chatgpt tests/test_platform_packages.py
git commit -m "feat: add ChatGPT workflow package"
```

---

### Task 7: Build the Gemini Platform Package

**Files:**
- Create: `platforms/gemini/setup.md`
- Create: `platforms/gemini/instant-run.md`
- Create: `platforms/gemini/installed-instructions.md`
- Create: `platforms/gemini/limitations.md`
- Modify: `tests/test_platform_packages.py`

**Interfaces:**
- Consumes shared core and template IDs
- Produces a self-contained Gemini path for Instant Run and Gem installation

- [ ] **Step 1: Expand the failing package matrix**

Change the platform parameterization to:

```python
@pytest.mark.parametrize("platform", ["chatgpt", "gemini"])
```

Add:

```python
def test_gemini_instructions_preserve_image_roles() -> None:
    text = (ROOT / "platforms/gemini/installed-instructions.md").read_text(encoding="utf-8")
    assert "style reference only" in text
    assert "product source" in text
    assert "do not require renamed files" in text
```

- [ ] **Step 2: Run Gemini package tests and verify failure**

Run:

```bash
python -m pytest tests/test_platform_packages.py -v
```

Expected: Gemini-specific tests fail because its package is absent.

- [ ] **Step 3: Write Gemini setup and limitations docs**

`setup.md` provides Instant Run and Install Once via a custom Gem. Explain how to paste instructions and add knowledge files. Link to official Gemini Gems and Gemini image-editing help.

`limitations.md` records that feature availability can vary by language, country, age, account type, and plan; reference interpretation is not a strict mask; product details require review; repairs restart from source.

- [ ] **Step 4: Write Gemini runtime instructions**

Mirror shared behavior without mentioning ChatGPT-specific controls. Explicitly support one reference plus one or more uploaded target images, process targets independently, and preserve the user's role messages. Include the literal clause `do not require renamed files`.

For simultaneous unlabeled uploads, propose the role mapping and require confirmation before editing. Do not classify roles solely from plain-versus-decorative backgrounds.

- [ ] **Step 5: Run tests, validation, and commit**

```bash
python -m pytest -v
python tools/validate_templates.py .
git add platforms/gemini tests/test_platform_packages.py
git commit -m "feat: add Gemini workflow package"
```

---

### Task 8: Build the Claude Platform Package

**Files:**
- Create: `platforms/claude/setup.md`
- Create: `platforms/claude/instant-run.md`
- Create: `platforms/claude/installed-instructions.md`
- Create: `platforms/claude/limitations.md`
- Modify: `tests/test_platform_packages.py`

**Interfaces:**
- Consumes shared core and template IDs
- Produces a self-contained Claude path with capability-aware behavior

- [ ] **Step 1: Expand package tests to Claude**

Change the platform parameterization to:

```python
@pytest.mark.parametrize("platform", ["chatgpt", "gemini", "claude"])
```

Add:

```python
def test_claude_package_never_claims_unsupported_rendering() -> None:
    limitations = (ROOT / "platforms/claude/limitations.md").read_text(encoding="utf-8")
    instructions = (ROOT / "platforms/claude/installed-instructions.md").read_text(encoding="utf-8")
    assert "capability" in limitations.lower()
    assert "do not claim that an image was edited when no image-editing tool ran" in instructions
```

- [ ] **Step 2: Run Claude package tests and verify failure**

Run:

```bash
python -m pytest tests/test_platform_packages.py -v
```

Expected: Claude tests fail because its package is absent.

- [ ] **Step 3: Write Claude setup and limitations docs**

`setup.md` provides Instant Run and Install Once via a Claude Project with Project Instructions and Knowledge files. Link to official Claude Projects and image-upload documentation.

`limitations.md` states the image-editing capability must be checked in the user's current interface. When unavailable, Claude may still perform reference analysis, Product Lock creation, prompt assembly, and QA, but must not pretend a raster edit occurred and must not silently move the user to another platform.

Do not add an automatic Prompt Exporter or one-click redirect to another model in Version 1. Any future export command must be user-triggered and disclose that prompts are not behaviorally portable across image models.

- [ ] **Step 4: Write capability-aware Claude instructions**

The instructions follow the full core pipeline when applicable tools are available. Include this exact rule:

```text
Do not claim that an image was edited when no image-editing tool ran.
State the current interface limitation plainly and complete only the workflow stages available here.
```

Keep all short commands, role handling, Product Lock, and QA behavior consistent with the shared core.

- [ ] **Step 5: Run tests, validation, and commit**

```bash
python -m pytest -v
python tools/validate_templates.py .
git add platforms/claude tests/test_platform_packages.py
git commit -m "feat: add Claude workflow package"
```

---

### Task 9: Add Manual Test Matrix and Redistributable Example Contract

**Files:**
- Create: `tests/manual-test-matrix.md`
- Create: `tests/cases/garments.md`
- Create: `tests/cases/fabric.md`
- Create: `tests/cases/earrings.md`
- Create: `tests/cases/bracelets.md`
- Create: `tests/cases/reflective-accessories.md`
- Create: `tests/synthetic_cases/README.md`
- Create: `tests/synthetic_cases/manifest.md`
- Create: `examples/sage-minimal-flatlay/README.md`
- Create: `examples/sage-minimal-flatlay/assembled-prompt.md`
- Create: `examples/sage-minimal-flatlay/lock-sheet.md`
- Create: `examples/sage-minimal-flatlay/qa-report.md`
- Create: `tests/test_manual_test_contract.py`

**Interfaces:**
- Produces repeatable human evaluation records used for release decisions
- Consumes Product Modules, Style Cards, Output Profiles, and platform packages

- [ ] **Step 1: Write failing manual-test contract tests**

Create `tests/test_manual_test_contract.py`:

```python
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_manual_matrix_has_required_columns() -> None:
    text = (ROOT / "tests/manual-test-matrix.md").read_text(encoding="utf-8")
    for column in ("Platform", "Surface", "Test date", "Case", "Mode", "Output", "Status", "Reviewer notes"):
        assert column in text


def test_each_product_has_a_manual_case() -> None:
    expected = {
        "garments.md",
        "fabric.md",
        "earrings.md",
        "bracelets.md",
        "reflective-accessories.md",
    }
    assert {path.name for path in (ROOT / "tests/cases").glob("*.md")} == expected


def test_example_records_asset_provenance() -> None:
    text = (ROOT / "examples/sage-minimal-flatlay/README.md").read_text(encoding="utf-8")
    assert "Asset provenance" in text
    assert "Redistribution license" in text


def test_synthetic_cases_are_supplemental_and_rights_checked() -> None:
    readme = (ROOT / "tests/synthetic_cases/README.md").read_text(encoding="utf-8")
    manifest = (ROOT / "tests/synthetic_cases/manifest.md").read_text(encoding="utf-8")
    assert "supplemental" in readme.lower()
    assert "do not replace real photographed-source tests" in readme
    assert "Redistribution license" in manifest
```

- [ ] **Step 2: Run tests and verify failure**

Run:

```bash
python -m pytest tests/test_manual_test_contract.py -v
```

Expected: failure because manual-test and example files are absent.

- [ ] **Step 3: Create the manual test matrix and five case definitions**

The matrix table includes the exact required columns and starts with no fabricated passes. Use `NOT RUN` until a real platform test is performed.

Each case defines:

- objective;
- minimum source-image characteristics;
- critical invariants;
- reference-style requirements;
- Safe Run checks;
- Fast Run checks;
- ecommerce checks;
- social checks;
- failure conditions;
- asset-rights requirement.

Create `tests/synthetic_cases/README.md` to define transparent cutouts as a supplemental control for edge integration, contact shadows, and background-light harmonization. State exactly: `These cases do not replace real photographed-source tests.`

Create `tests/synthetic_cases/manifest.md` with columns for Asset, Product category, Source type, Creator, Source URL or generation record, Redistribution license, Edge characteristics, and Intended checks. Do not add an asset until every provenance field is complete.

- [ ] **Step 4: Create the example documentation contract without unlicensed images**

`examples/sage-minimal-flatlay/README.md` explains that image files are added only after ownership or compatible licensing is verified. It includes `Asset provenance`, `Redistribution license`, platform, test date, source role, reference role, output profile, and QA status.

The assembled prompt, lock sheet, and QA report use a clearly labeled synthetic bracelet case and contain no claims that an unrun generation passed.

- [ ] **Step 5: Run tests, validation, and commit**

```bash
python -m pytest -v
python tools/validate_templates.py .
git add tests/manual-test-matrix.md tests/cases tests/synthetic_cases examples tests/test_manual_test_contract.py
git commit -m "test: add visual workflow evaluation matrix"
```

---

### Task 10: Write the Professional README and Quickstarts

**Files:**
- Create: `README.md`
- Create: `README.vi.md`
- Create: `QUICKSTART.md`
- Create: `tests/test_readme_contract.py`

**Interfaces:**
- Consumes all platform packages, templates, examples, and test policy
- Produces the public product narrative and shortest user path

- [ ] **Step 1: Write failing README acceptance tests**

Create `tests/test_readme_contract.py`:

```python
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_english_readme_has_required_reader_journey() -> None:
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    headings = [
        "# Product Photo AI Workflows",
        "## Why ordinary background replacement fails",
        "## Who this is for",
        "## How the workflow protects your product",
        "## Quick start",
        "## Choose your platform",
        "## Product and style coverage",
        "## Examples",
        "## Use in a business workflow",
        "## Extend the library",
        "## Contributing and license",
    ]
    for heading in headings:
        assert heading in text


def test_readme_addresses_fashion_business_users() -> None:
    text = (ROOT / "README.md").read_text(encoding="utf-8").lower()
    for audience in ("fashion brands", "jewelry businesses", "ecommerce teams", "creative studios"):
        assert audience in text
    for detail in ("folds", "seams", "texture", "stones", "clasps", "reflections"):
        assert detail in text


def test_vietnamese_readme_is_not_a_short_stub() -> None:
    english = (ROOT / "README.md").read_text(encoding="utf-8")
    vietnamese = (ROOT / "README.vi.md").read_text(encoding="utf-8")
    assert len(vietnamese) >= len(english) * 0.65


def test_quickstart_links_all_platforms() -> None:
    text = (ROOT / "QUICKSTART.md").read_text(encoding="utf-8")
    for platform in ("chatgpt", "gemini", "claude"):
        assert f"platforms/{platform}/setup.md" in text
```

- [ ] **Step 2: Run README tests and verify failure**

Run:

```bash
python -m pytest tests/test_readme_contract.py -v
```

Expected: failure because public documentation files are absent.

- [ ] **Step 3: Write canonical English README in the approved narrative order**

Use the exact headings tested above. The hero promise must communicate controlled background transformation with product fidelity, not generic beautification. The opening is written for commercial image makers, not developers.

Include:

- a concise tagline: `Reusable, platform-native workflows for faithful AI product photo editing.`;
- a fashion-focused explanation of commercial fidelity risk;
- a compact source + reference → lock → edit → QA → repair diagram;
- Instant Run and Install Once paths;
- platform capability notes without claiming parity;
- scan-friendly product/style/output tables;
- business review and privacy considerations;
- honest limitations and no “perfect results” claim;
- example slots only for assets with documented rights;
- contribution and MIT licensing summary.

- [ ] **Step 4: Write complete Vietnamese README**

Translate meaning and positioning, not sentence order mechanically. Preserve the professional, visually literate tone and the same practical coverage. Use familiar Vietnamese terms for product photography while retaining canonical command names in English.

Use this canonical glossary consistently:

```text
Product Fidelity → Độ trung thực sản phẩm
Product Lock → Khóa toàn vẹn sản phẩm
Silhouette → Phom dáng và đường biên sản phẩm
Contact Shadow → Bóng tiếp xúc
Specular Highlights → Vùng bắt sáng bề mặt
Color Drift → Sai lệch màu sản phẩm
```

- [ ] **Step 5: Write the concise English Quickstart**

Keep `QUICKSTART.md` focused on a first successful run:

1. choose a platform;
2. choose Instant Run or Install Once;
3. attach reference with the reference-role sentence;
4. attach target with the edit-role sentence;
5. choose Safe/Fast and Ecommerce/Social/Both;
6. review QA status;
7. repair or move to `NEXT PRODUCT`.

- [ ] **Step 6: Run documentation tests, validator, and commit**

```bash
python -m pytest -v
python tools/validate_templates.py .
git add README.md README.vi.md QUICKSTART.md tests/test_readme_contract.py
git commit -m "docs: publish professional bilingual quickstart"
```

---

### Task 11: Add Open-Source Governance and Contribution Guidance

**Files:**
- Create: `LICENSE`
- Create: `CONTRIBUTING.md`
- Create: `CODE_OF_CONDUCT.md`
- Create: `CHANGELOG.md`
- Create: `.github/pull_request_template.md`
- Create: `tests/test_governance_contract.py`

**Interfaces:**
- Consumes template schema, validator command, manual testing policy, and asset-rights policy
- Produces a safe, welcoming, reproducible contribution path

- [ ] **Step 1: Write failing governance tests**

Create `tests/test_governance_contract.py`:

```python
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_license_is_mit() -> None:
    text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    assert "MIT License" in text
    assert "Permission is hereby granted" in text


def test_contributing_requires_validation_and_asset_rights() -> None:
    text = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
    assert "python tools/validate_templates.py ." in text
    assert "redistribution rights" in text
    assert "manual test matrix" in text


def test_pull_request_template_requires_evidence() -> None:
    text = (ROOT / ".github/pull_request_template.md").read_text(encoding="utf-8")
    for phrase in ("Validation", "Visual test evidence", "Asset provenance", "Platform limitations"):
        assert phrase in text
```

- [ ] **Step 2: Run governance tests and verify failure**

Run:

```bash
python -m pytest tests/test_governance_contract.py -v
```

Expected: failure because governance files are absent.

- [ ] **Step 3: Add license and community standards**

Use the canonical MIT License text with `Copyright (c) 2026 Product Photo AI Workflows contributors`.

Use Contributor Covenant 2.1 for `CODE_OF_CONDUCT.md`. The enforcement section must say: `Contact the repository owner using the private contact method listed on the maintainer's GitHub profile. Do not open a public issue for a conduct report.`

- [ ] **Step 4: Write contribution and pull-request workflow**

`CONTRIBUTING.md` must explain:

- template kinds and front matter;
- copying `_template.md`;
- unique IDs and semantic versions;
- required headings;
- running pytest and validator;
- recording manual visual tests without inventing results;
- documenting redistribution rights;
- reviewing core changes more strictly than style additions;
- keeping English canonical and Vietnamese meaning consistent.

The pull-request template includes checkboxes for Validation, Visual test evidence, Asset provenance, Platform limitations, documentation, and backward compatibility.

- [ ] **Step 5: Initialize changelog and commit governance files**

`CHANGELOG.md` follows Keep a Changelog structure with `[Unreleased]` and an initial `0.1.0` entry describing the shared core, three platform packages, five product modules, four style cards, two outputs, validation, and bilingual docs.

Run and commit:

```bash
python -m pytest -v
python tools/validate_templates.py .
git add LICENSE CONTRIBUTING.md CODE_OF_CONDUCT.md CHANGELOG.md .github/pull_request_template.md tests/test_governance_contract.py
git commit -m "chore: add open-source governance"
```

---

### Task 12: Perform Release-Candidate Verification

**Files:**
- Modify only if verification exposes a defect in files created by Tasks 1–11
- Update: `tests/manual-test-matrix.md` only with real, observed test results
- Update: `CHANGELOG.md` only when the release candidate is genuinely complete

**Interfaces:**
- Consumes the complete repository
- Produces a clean local `0.1.0` release candidate suitable for GitHub publication

- [ ] **Step 1: Run automated tests and repository validation**

```bash
python -m pytest -v
python tools/validate_templates.py .
```

Expected: all tests pass and CLI prints `Validation passed.`

- [ ] **Step 2: Run static repository checks**

```bash
git diff --check
rg -n "TODO|TBD|PLACEHOLDER" --glob '!docs/superpowers/**' .
```

Expected: no whitespace errors and no unresolved publishable placeholders. Contributor `_template.md` tokens must be intentional and documented, not TODO/TBD markers.

- [ ] **Step 3: Execute the manual platform test matrix**

For each available platform surface, run at least one Safe Run and one Fast Run using assets with documented rights. Record platform, surface, date, case, mode, output, status, and reviewer notes. Mark unavailable capabilities as `UNSUPPORTED`, never `PASS`.

Run both real photographed-source cases and the supplemental transparent-cutout cases. Do not treat a synthetic pass as evidence that source-background separation works on real photographs.

The release matrix must include:

- one requested ratio change that verifies background expansion without product crop, scale, stretch, or squeeze;
- one ecommerce composition that evaluates the 15% safe-padding target;
- one style reference containing visible text, a logo, or a watermark and an output check confirming no typography contamination;
- one color-sensitive product checked for visible product-color drift after background grading.

Expected: every claimed capability has observed evidence; unsupported surfaces are documented honestly.

- [ ] **Step 4: Perform README acceptance review**

Review as two personas:

1. an independent fashion seller with no technical background;
2. an ecommerce or creative lead responsible for brand consistency.

Confirm both can locate the value proposition, first-run instructions, fidelity controls, limitations, business review process, platform path, and contribution model without reading internal architecture docs.

- [ ] **Step 5: Verify Git history and clean working tree**

```bash
git log --oneline --decorate -12
git status --short
```

Expected: focused commits for each task and no unexpected uncommitted files.

- [ ] **Step 6: Route any release-candidate defect back to its owning task**

If verification finds a defect, stop the release check, return to the task that owns the affected file, repeat that task's test cycle, and use its explicit `git add` file list. Resume Task 12 from Step 1 afterward. If no changes are required, do not create an empty commit.

- [ ] **Step 7: Stop before remote publication**

Report the verified local state, proposed GitHub repository description, and suggested release tag `v0.1.0`. Do not create a GitHub repository, push, tag, publish a release, or upload assets until the user explicitly approves that external action.

Ghost mannequin/on-model modules and an optional user-triggered Prompt Exporter remain roadmap items. They require separate specifications and must not be added opportunistically during Version 1 implementation.
