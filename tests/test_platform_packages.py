from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
PLATFORM_FILES = {
    "setup.md",
    "instant-run.md",
    "installed-instructions.md",
    "limitations.md",
}


@pytest.mark.parametrize("platform", ["chatgpt", "gemini", "claude"])
def test_platform_package_is_complete(platform: str) -> None:
    package = ROOT / "platforms" / platform
    assert {path.name for path in package.glob("*.md")} == PLATFORM_FILES


def test_chatgpt_installed_instructions_include_core_safety_commands() -> None:
    text = (ROOT / "platforms/chatgpt/installed-instructions.md").read_text(
        encoding="utf-8"
    )
    for phrase in (
        "original product source",
        "SAFE RUN",
        "FAST RUN",
        "NEXT PRODUCT",
        "MANUAL REVIEW",
    ):
        assert phrase in text


def test_gemini_instructions_preserve_image_roles() -> None:
    text = (ROOT / "platforms/gemini/installed-instructions.md").read_text(
        encoding="utf-8"
    )
    assert "style reference only" in text
    assert "product source" in text
    assert "do not require renamed files" in text


def test_claude_package_never_claims_unsupported_rendering() -> None:
    limitations = (ROOT / "platforms/claude/limitations.md").read_text(
        encoding="utf-8"
    )
    instructions = (ROOT / "platforms/claude/installed-instructions.md").read_text(
        encoding="utf-8"
    )
    assert "capability" in limitations.lower()
    assert (
        "do not claim that an image was edited when no image-editing tool ran"
        in instructions
    )
