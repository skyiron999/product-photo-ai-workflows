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
