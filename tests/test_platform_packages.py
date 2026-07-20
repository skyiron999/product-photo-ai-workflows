from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
PLATFORM_FILES = {
    "setup.md",
    "setup.vi.md",
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


@pytest.mark.parametrize("platform", ["chatgpt", "gemini", "claude"])
@pytest.mark.parametrize("filename", ["installed-instructions.md", "instant-run.md"])
def test_platform_runtime_is_reference_first(platform: str, filename: str) -> None:
    text = (ROOT / "platforms" / platform / filename).read_text(encoding="utf-8")

    assert "Reference Style Profile" in text
    assert "do not auto-select" in text
    assert "Style Card: NONE — reference-driven" in text


@pytest.mark.parametrize("platform", ["chatgpt", "gemini", "claude"])
@pytest.mark.parametrize("filename", ["installed-instructions.md", "instant-run.md"])
def test_platform_runtime_supports_strict_reference_match(
    platform: str, filename: str
) -> None:
    text = (ROOT / "platforms" / platform / filename).read_text(encoding="utf-8")

    for phrase in (
        "STRICT MATCH",
        "requires an explicitly mapped style reference",
        "do not use a Style Card",
        "Product Lock remains higher priority",
        "Background mode: STRICT MATCH",
        "Match assessment: PASS | WARN | FAIL",
        "Pixel-exact guarantee: NO — generative visual match",
    ):
        assert phrase in text
