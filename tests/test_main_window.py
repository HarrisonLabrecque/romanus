
"""
Romanus - Main Window Tests

Tests the PySide6 main window, sidebar navigation,
keyboard shortcuts, and page registration.

Version: 0.8.0
"""

import pytest

from PySide6.QtCore import Qt
from PySide6.QtGui import QKeySequence

from ui.main_window import MainWindow


# --------------------------------------------------
# Fixtures
# --------------------------------------------------

@pytest.fixture
def window(qtbot):
    """Create a MainWindow instance for each test."""

    main_window = MainWindow()

    qtbot.addWidget(main_window)

    return main_window


# --------------------------------------------------
# Window Initialization Tests
# --------------------------------------------------

def test_window_title(window):
    """Verify the application window title."""

    assert window.windowTitle() == (
        "Romanus - Greco-Roman Reference"
    )


def test_window_minimum_size(window):
    """Verify the minimum supported window dimensions."""

    assert window.minimumWidth() == 850
    assert window.minimumHeight() == 550


def test_initial_page_is_home(window):
    """Verify that the Home page opens by default."""

    assert window.pages.currentWidget() == window.home_page


def test_all_pages_registered(window):
    """Verify that all seven pages are registered."""

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
# Sidebar Tests
# --------------------------------------------------

def test_sidebar_exists(window):
    """Verify that the sidebar container exists."""

    assert window.sidebar_widget.objectName() == "sidebar"


def test_sidebar_width(window):
    """Verify the configured sidebar width."""

    assert window.sidebar_widget.width() == 230


def test_navigation_buttons_registered(window):
    """Verify that each page has a navigation button."""

    assert set(window.navigation_buttons.keys()) == set(
        window.page_widgets.keys()
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
def test_navigation_to_each_page(window, page_name):
    """Verify navigation to each registered page."""

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
def test_active_navigation_button(window, page_name):
    """Verify that only the active page button is checked."""

    window.navigate_to_page(page_name)

    for name, button in window.navigation_buttons.items():
        assert button.isChecked() == (name == page_name)


def test_invalid_page_navigation(window):
    """Invalid page names must not change the current page."""

    original_page = window.pages.currentWidget()

    window.navigate_to_page("unknown")

    assert window.pages.currentWidget() == original_page


def test_navigation_button_click(window, qtbot):
    """Clicking a sidebar button should navigate to its page."""

    qtbot.mouseClick(
        window.greek_button,
        Qt.MouseButton.LeftButton,
    )

    assert window.pages.currentWidget() == window.greek_page


# --------------------------------------------------
# Search Shortcut Tests
# --------------------------------------------------

def test_search_shortcut_exists(window):
    """Verify that the Ctrl+F shortcut is registered."""

    assert window.search_shortcut.key() == QKeySequence(
        "Ctrl+F"
    )


def test_open_search(window):
    """Verify that the search handler opens Search."""

    window.open_search()

    assert window.pages.currentWidget() == window.search_page
    assert window.search_button.isChecked()


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
def test_navigation_buttons_are_focusable(window, page_name):
    """Verify navigation buttons accept keyboard focus."""

    button = window.navigation_buttons[page_name]

    assert button.focusPolicy() != Qt.FocusPolicy.NoFocus


def test_navigation_buttons_are_checkable(window):
    """Verify sidebar buttons support active-page state."""

    for button in window.navigation_buttons.values():
        assert button.isCheckable()
