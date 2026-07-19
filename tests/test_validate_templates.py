from pathlib import Path

import pytest

from tools.validate_templates import FrontMatterError, parse_front_matter, validate_repository


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


def write_catalog_baseline(root: Path) -> None:
    write_template(
        root / "products/garments.md",
        template_id="garments",
        kind="product",
        body="# Garments\n\n## Detect\nText\n## Lock\nText\n## Risks\nText\n## QA\nText\n",
    )
    write_template(
        root / "outputs/ecommerce.md",
        template_id="ecommerce",
        kind="output",
        body="# Ecommerce\n\n## Purpose\nText\n## Composition\nText\n## Constraints\nText\n## QA\nText\n",
    )


def test_validate_repository_reports_duplicate_ids(tmp_path: Path) -> None:
    write_catalog_baseline(tmp_path)
    body = "# Template\n\n## Detect\nText\n## Lock\nText\n## Risks\nText\n## QA\nText\n"
    write_template(tmp_path / "products/duplicate.md", template_id="garments", kind="product", body=body)

    issues = validate_repository(tmp_path)

    assert any("duplicate id 'garments'" in issue.message for issue in issues)


def test_validate_repository_reports_publishable_placeholders(tmp_path: Path) -> None:
    write_catalog_baseline(tmp_path)
    body = "# Template\n\n## Visual intent\nTODO\n## Background\nText\n## Lighting\nText\n## Preserve\nText\n## Avoid\nText\n"
    write_template(tmp_path / "styles/broken.md", template_id="broken", kind="style", body=body)

    issues = validate_repository(tmp_path)

    assert any("publishable placeholder" in issue.message for issue in issues)


def test_validate_repository_allows_placeholders_in_underscore_template(tmp_path: Path) -> None:
    write_catalog_baseline(tmp_path)
    body = "# YOUR STYLE\n\n## Visual intent\nYOUR TEXT\n## Background\nYOUR TEXT\n## Lighting\nYOUR TEXT\n## Preserve\nYOUR TEXT\n## Avoid\nYOUR TEXT\n"
    write_template(tmp_path / "styles/_template.md", template_id="style-template", kind="style", body=body)

    issues = validate_repository(tmp_path)

    assert not any("publishable placeholder" in issue.message for issue in issues)


def test_validate_repository_reports_broken_relative_link(tmp_path: Path) -> None:
    readme = tmp_path / "README.md"
    readme.write_text("[Missing](docs/missing.md)\n", encoding="utf-8")

    issues = validate_repository(tmp_path)

    assert any("broken relative link" in issue.message for issue in issues)


def test_validate_repository_ignores_links_inside_fenced_code(tmp_path: Path) -> None:
    readme = tmp_path / "README.md"
    readme.write_text(
        "```markdown\n[Missing](docs/missing.md)\n```\n",
        encoding="utf-8",
    )

    issues = validate_repository(tmp_path)

    assert not any("broken relative link" in issue.message for issue in issues)


def test_validate_repository_reports_unknown_product_and_output_references(tmp_path: Path) -> None:
    write_catalog_baseline(tmp_path)
    style = tmp_path / "styles/unknown-references.md"
    style.parent.mkdir(parents=True)
    style.write_text(
        """---
id: unknown-references
name: Unknown References
kind: style
version: 1.0.0
compatible_with: [chatgpt]
recommended_for: [shoes]
outputs: [social]
---
# Unknown References

## Visual intent
Text
## Background
Text
## Lighting
Text
## Preserve
Text
## Avoid
Text
""",
        encoding="utf-8",
    )

    issues = validate_repository(tmp_path)

    assert any("unknown products: shoes" in issue.message for issue in issues)
    assert any("unknown outputs: social" in issue.message for issue in issues)


def test_validate_repository_reports_non_list_reference_fields(tmp_path: Path) -> None:
    write_catalog_baseline(tmp_path)
    broken = tmp_path / "styles/bad-types.md"
    broken.parent.mkdir(parents=True)
    broken.write_text(
        """---
id: bad-types
name: Bad Types
kind: style
version: 1.0.0
compatible_with: chatgpt
recommended_for: garments
outputs: ecommerce
---
# Bad Types

## Visual intent
Text
## Background
Text
## Lighting
Text
## Preserve
Text
## Avoid
Text
""",
        encoding="utf-8",
    )

    issues = validate_repository(tmp_path)

    assert sum("must be a list of strings" in issue.message for issue in issues) == 3
