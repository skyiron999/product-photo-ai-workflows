from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
BUNDLE_DIR = ROOT / "bundles"
EXPECTED_BUNDLES = {
    "knowledge-core.md",
    "knowledge-products.md",
    "knowledge-styles.md",
    "knowledge-outputs.md",
}


def test_publishable_knowledge_bundle_set_is_complete() -> None:
    actual = {
        path.name
        for path in BUNDLE_DIR.glob("knowledge-*.md")
        if path.is_file()
    }

    assert actual == EXPECTED_BUNDLES


def test_committed_bundles_match_canonical_sources() -> None:
    result = subprocess.run(
        [sys.executable, "tools/build_bundles.py", "--check"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stdout + result.stderr


def test_contributor_templates_are_not_in_knowledge_bundles() -> None:
    combined = "\n".join(
        path.read_text(encoding="utf-8")
        for path in sorted(BUNDLE_DIR.glob("knowledge-*.md"))
    )

    assert "_template.md" not in combined
    assert "YOUR TEXT" not in combined
    assert "YOUR STYLE" not in combined


def test_platform_setup_guides_link_all_four_bundles() -> None:
    for platform in ("chatgpt", "gemini", "claude"):
        for language_suffix in ("", ".vi"):
            setup = (
                ROOT / f"platforms/{platform}/setup{language_suffix}.md"
            ).read_text(encoding="utf-8")
            for bundle in EXPECTED_BUNDLES:
                assert f"../../bundles/{bundle}" in setup
