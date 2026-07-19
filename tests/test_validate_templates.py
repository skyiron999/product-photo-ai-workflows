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
