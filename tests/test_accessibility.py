
"""
Romanus - Accessibility Unit Tests

Tests keyboard accessibility, accessible labels,
navigation shortcuts, tooltips, and active-page state.

Version: 0.8.0
"""

import pytest

from PySide6.QtCore import Qt
from PySide6.QtGui import QKeySequence

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
# Accessible Names and Descriptions
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
def test_navigation_accessible_name(window, page_name):
    """Verify each sidebar button has an accessible name."""

    button = window.navigation_buttons[page_name]

    assert button.accessibleName() == button.text()


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
def test_navigation_accessible_description(window, page_name):
    """Verify sidebar buttons have accessible descriptions."""

    button = window.navigation_buttons[page_name]

    expected_description = (
        f"Navigate to the {button.text()} reference page"
    )

    assert button.accessibleDescription() == expected_description


def test_main_window_accessible_name(window):
    """Verify the main window has an accessible name."""

    assert window.accessibleName() == "Romanus Main Window"


def test_main_window_accessible_description(window):
    """Verify the main window has an accessible description."""

    assert window.accessibleDescription().strip()


# --------------------------------------------------
# Keyboard Focus Tests
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
def test_navigation_keyboard_focus(window, page_name):
    """Verify every navigation button accepts Tab focus."""

    button = window.navigation_buttons[page_name]

    assert button.focusPolicy() & Qt.FocusPolicy.TabFocus


# --------------------------------------------------
# Tooltip Tests
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
def test_navigation_tooltip(window, page_name):
    """Verify each navigation button has a tooltip."""

    button = window.navigation_buttons[page_name]

    assert button.toolTip() == f"Open {button.text()}"


# --------------------------------------------------
# Keyboard Shortcut Tests
# --------------------------------------------------

def test_search_shortcut(window):
    """Verify Ctrl+F is assigned to Search."""

    assert window.search_shortcut.key() == QKeySequence(
        "Ctrl+F"
    )


def test_home_shortcut(window):
    """Verify Ctrl+H is assigned to Home."""

    assert window.home_shortcut.key() == QKeySequence(
        "Ctrl+H"
    )


def test_back_home_shortcut(window):
    """Verify Alt+Left is assigned to Home."""

    assert window.back_home_shortcut.key() == QKeySequence(
        "Alt+Left"
    )


def test_search_shortcut_navigation(window):
    """Verify activating the Search shortcut opens Search."""

    window.search_shortcut.activated.emit()

    assert window.pages.currentWidget() == window.search_page


def test_home_shortcut_navigation(window):
    """Verify activating the Home shortcut opens Home."""

    window.navigate_to_page("latin")

    window.home_shortcut.activated.emit()

    assert window.pages.currentWidget() == window.home_page


def test_back_home_shortcut_navigation(window):
    """Verify activating Alt+Left returns to Home."""

    window.navigate_to_page("greek")

    window.back_home_shortcut.activated.emit()

    assert window.pages.currentWidget() == window.home_page


# --------------------------------------------------
# Active Navigation State
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
def test_only_active_button_checked(window, page_name):
    """Verify only the selected page button is checked."""

    window.navigate_to_page(page_name)

    checked_buttons = [
        name
        for name, button in window.navigation_buttons.items()
        if button.isChecked()
    ]

    assert checked_buttons == [page_name]
