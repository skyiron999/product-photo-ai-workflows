from pathlib import Path
import tomllib

ROOT = Path(__file__).resolve().parents[1]


def test_editable_install_has_explicit_package_scope() -> None:
    config = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))

    assert config["tool"]["setuptools"]["packages"] == ["tools"]


def test_license_uses_spdx_expression() -> None:
    config = tomllib.loads((ROOT / "pyproject.toml").read_text(encoding="utf-8"))

    assert config["project"]["license"] == "MIT"
