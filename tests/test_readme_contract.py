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
    for audience in (
        "fashion brands",
        "jewelry businesses",
        "ecommerce teams",
        "creative studios",
    ):
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


def test_vietnamese_quickstart_links_vietnamese_platform_guides() -> None:
    text = (ROOT / "QUICKSTART.vi.md").read_text(encoding="utf-8")
    for platform in ("chatgpt", "gemini", "claude"):
        assert f"platforms/{platform}/setup.vi.md" in text


def test_each_platform_has_a_complete_vietnamese_setup_guide() -> None:
    for platform in ("chatgpt", "gemini", "claude"):
        english = (ROOT / f"platforms/{platform}/setup.md").read_text(
            encoding="utf-8"
        )
        vietnamese = (ROOT / f"platforms/{platform}/setup.vi.md").read_text(
            encoding="utf-8"
        )
        assert len(vietnamese) >= len(english) * 0.65
        assert "Tiếng Việt" in vietnamese
        assert "instant-run.md" in vietnamese


def test_quickstarts_link_to_each_other() -> None:
    english = (ROOT / "QUICKSTART.md").read_text(encoding="utf-8")
    vietnamese = (ROOT / "QUICKSTART.vi.md").read_text(encoding="utf-8")
    assert "QUICKSTART.vi.md" in english
    assert "QUICKSTART.md" in vietnamese
