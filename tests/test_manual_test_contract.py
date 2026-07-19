from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_manual_matrix_has_required_columns() -> None:
    text = (ROOT / "tests/manual-test-matrix.md").read_text(encoding="utf-8")
    for column in (
        "Platform",
        "Surface",
        "Test date",
        "Case",
        "Mode",
        "Output",
        "Status",
        "Reviewer notes",
    ):
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
    text = (ROOT / "examples/sage-minimal-flatlay/README.md").read_text(
        encoding="utf-8"
    )
    assert "Asset provenance" in text
    assert "Redistribution license" in text


def test_synthetic_cases_are_supplemental_and_rights_checked() -> None:
    readme = (ROOT / "tests/synthetic_cases/README.md").read_text(encoding="utf-8")
    manifest = (ROOT / "tests/synthetic_cases/manifest.md").read_text(
        encoding="utf-8"
    )
    assert "supplemental" in readme.lower()
    assert "do not replace real photographed-source tests" in readme
    assert "Redistribution license" in manifest
