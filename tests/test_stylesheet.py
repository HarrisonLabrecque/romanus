
"""
Romanus - Stylesheet Tests

Tests the global QSS stylesheet introduced in v0.8.0.
"""

from pathlib import Path

from PySide6.QtWidgets import QApplication

from main import load_stylesheet


PROJECT_ROOT = Path(__file__).resolve().parents[1]

STYLESHEET_PATH = (
    PROJECT_ROOT / "resources" / "styles" / "main.qss"
)


def test_stylesheet_exists():
    """Verify the stylesheet file exists."""

    assert STYLESHEET_PATH.is_file()


def test_stylesheet_is_not_empty():
    """Verify the stylesheet contains styling rules."""

    content = STYLESHEET_PATH.read_text(encoding="utf-8")

    assert content.strip()


def test_stylesheet_contains_sidebar_rules():
    """Verify sidebar styling rules are defined."""

    content = STYLESHEET_PATH.read_text(encoding="utf-8")

    assert "QWidget#sidebar" in content
    assert "QPushButton#navigationButton" in content


def test_stylesheet_contains_active_navigation_style():
    """Verify active sidebar buttons have a visual state."""

    content = STYLESHEET_PATH.read_text(encoding="utf-8")

    assert "QPushButton#navigationButton:checked" in content


def test_stylesheet_contains_focus_style():
    """Verify keyboard focus indicators are defined."""

    content = STYLESHEET_PATH.read_text(encoding="utf-8")

    assert "QPushButton#navigationButton:focus" in content


def test_stylesheet_loads(qapp):
    """Verify that the global stylesheet loads successfully."""

    load_stylesheet(qapp)

    assert qapp.styleSheet().strip()
