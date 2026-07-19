from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
PLATFORM_FILES = {
    "setup.md",
    "instant-run.md",
    "installed-instructions.md",
    "limitations.md",
}


@pytest.mark.parametrize("platform", ["chatgpt"])
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
