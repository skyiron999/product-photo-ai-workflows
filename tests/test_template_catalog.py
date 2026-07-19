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
