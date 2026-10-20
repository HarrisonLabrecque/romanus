
"""
Romanus - Stable Release Regression Tests

Verifies the main application configuration,
reference pages, keyboard shortcuts, and resources.

Version: 1.0.0
"""

import pytest

from PySide6.QtCore import Qt
from PySide6.QtGui import QKeySequence

from main import (
    APP_NAME,
    APP_VERSION,
    get_resource_path,
    load_stylesheet,
)

from ui.main_window import MainWindow


# --------------------------------------------------
# Test Fixtures
# --------------------------------------------------

@pytest.fixture
def window(qtbot):
    """Create a Romanus main window for testing."""

    main_window = MainWindow()
    qtbot.addWidget(main_window)

    return main_window


# --------------------------------------------------
# Application Configuration Tests
# --------------------------------------------------

def test_application_name():
    """Verify the application name."""

    assert APP_NAME == "Romanus"


def test_application_version():
    """Verify the stable release version."""

    assert APP_VERSION == "1.0.0"


def test_stylesheet_resource_exists():
    """Verify the global stylesheet is available."""

    stylesheet_path = get_resource_path(
        "resources/styles/main.qss"
    )

    assert stylesheet_path.is_file()


def test_stylesheet_loading(qapp):
    """Verify the stylesheet loads successfully."""

    load_stylesheet(qapp)

    assert qapp.styleSheet().strip()


# --------------------------------------------------
# Main Window Tests
# --------------------------------------------------

def test_window_title(window):
    """Verify the main window title."""

    assert window.windowTitle() == (
        "Romanus - Greco-Roman Reference"
    )


def test_window_minimum_size(window):
    """Verify minimum window dimensions."""

    assert window.minimumWidth() == 850
    assert window.minimumHeight() == 550


def test_default_page(window):
    """Verify Home is the default page."""

    assert window.pages.currentWidget() == window.home_page


def test_all_reference_pages_registered(window):
    """Verify all seven pages are registered."""

    expected_pages = {
        "home",
        "search",
        "latin",
        "greek",
        "numerals",
        "astrology",
        "deities",
    }

    assert set(window.page_widgets.keys()) == expected_pages

    assert window.pages.count() == 7


# --------------------------------------------------
# Navigation Tests
# --------------------------------------------------

@pytest.mark.parametrize(
    "page_name",
    [
        "home",
        "search",
        "latin",
        "greek",
        "numerals",
        "astrology",
        "deities",
    ],
)
def test_page_navigation(window, page_name):
    """Verify navigation to every reference page."""

    window.navigate_to_page(page_name)

    assert window.pages.currentWidget() == (
        window.page_widgets[page_name]
    )


@pytest.mark.parametrize(
    "page_name",
    [
        "home",
        "search",
        "latin",
        "greek",
        "numerals",
        "astrology",
        "deities",
    ],
)
def test_active_sidebar_button(window, page_name):
    """Verify the active page is highlighted."""

    window.navigate_to_page(page_name)

    for name, button in window.navigation_buttons.items():
        assert button.isChecked() == (name == page_name)


def test_invalid_navigation(window):
    """Verify unknown pages are ignored."""

    original_page = window.pages.currentWidget()

    window.navigate_to_page("invalid_page")

    assert window.pages.currentWidget() == original_page


# --------------------------------------------------
# Accessibility Tests
# --------------------------------------------------

@pytest.mark.parametrize(
    "page_name",
    [
        "home",
        "search",
        "latin",
        "greek",
        "numerals",
        "astrology",
        "deities",
    ],
)
def test_navigation_accessibility(window, page_name):
    """Verify accessible names and keyboard focus."""

    button = window.navigation_buttons[page_name]

    assert button.accessibleName() == button.text()

    assert button.accessibleDescription().strip()

    assert button.focusPolicy() & Qt.FocusPolicy.TabFocus


# --------------------------------------------------
# Keyboard Shortcut Tests
# --------------------------------------------------

def test_search_shortcut(window):
    """Verify Ctrl+F is configured."""

    assert window.search_shortcut.key() == QKeySequence(
        "Ctrl+F"
    )


def test_home_shortcut(window):
    """Verify Ctrl+H is configured."""

    assert window.home_shortcut.key() == QKeySequence(
        "Ctrl+H"
    )


def test_back_home_shortcut(window):
    """Verify Alt+Left is configured."""

    assert window.back_home_shortcut.key() == QKeySequence(
        "Alt+Left"
    )


def test_search_shortcut_action(window):
    """Verify the Search shortcut opens Search."""

    window.search_shortcut.activated.emit()

    assert window.pages.currentWidget() == window.search_page


def test_home_shortcut_action(window):
    """Verify the Home shortcut opens Home."""

    window.navigate_to_page("latin")

    window.home_shortcut.activated.emit()

    assert window.pages.currentWidget() == window.home_page


def test_back_home_shortcut_action(window):
    """Verify Alt+Left returns to Home."""

    window.navigate_to_page("greek")

    window.back_home_shortcut.activated.emit()

    assert window.pages.currentWidget() == window.home_page
