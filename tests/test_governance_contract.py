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
    for phrase in (
        "Validation",
        "Visual test evidence",
        "Asset provenance",
        "Platform limitations",
    ):
        assert phrase in text
