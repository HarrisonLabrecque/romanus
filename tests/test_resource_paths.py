
"""
Romanus - Resource Path Tests

Tests resource path resolution and stylesheet loading.

Version: 0.9.0
"""

import sys
from pathlib import Path

from main import get_resource_path, load_stylesheet


def test_resource_path_exists():
    """Verify the stylesheet can be located."""

    path = get_resource_path(
        "resources/styles/main.qss"
    )

    assert path.is_file()


def test_resource_path_is_absolute():
    """Verify resource paths are absolute."""

    path = get_resource_path(
        "resources/styles/main.qss"
    )

    assert path.is_absolute()


def test_resource_path_development(monkeypatch):
    """Verify resource resolution outside PyInstaller."""

    monkeypatch.delattr(
        sys,
        "_MEIPASS",
        raising=False,
    )

    path = get_resource_path(
        "resources/styles/main.qss"
    )

    expected = (
        Path(__file__).resolve().parents[1]
        / "resources"
        / "styles"
        / "main.qss"
    )

    assert path == expected


def test_resource_path_packaged(monkeypatch, tmp_path):
    """Verify resource resolution inside PyInstaller."""

    monkeypatch.setattr(
        sys,
        "_MEIPASS",
        str(tmp_path),
        raising=False,
    )

    path = get_resource_path(
        "resources/styles/main.qss"
    )

    assert path == (
        tmp_path / "resources/styles/main.qss"
    )


def test_stylesheet_loads(qapp):
    """Verify the application stylesheet loads."""

    load_stylesheet(qapp)

    assert qapp.styleSheet().strip()
