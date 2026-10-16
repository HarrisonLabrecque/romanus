
"""
Romanus - Main Application Window

Manages sidebar navigation, the Home dashboard,
reference pages, unified search, and accessibility.

Version: 0.8.0
"""

from PySide6.QtCore import Qt
from PySide6.QtGui import QShortcut, QKeySequence

from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QStackedWidget,
)

from ui.pages.home_page import HomePage
from ui.pages.latin_page import LatinPage
from ui.pages.greek_page import GreekPage
from ui.pages.numerals_page import NumeralsPage
from ui.pages.astrology_page import AstrologyPage
from ui.pages.deities_page import DeitiesPage
from ui.pages.search_page import SearchPage


class MainWindow(QMainWindow):
    """Main application window for Romanus."""

    def __init__(self):
        super().__init__()

        # ------------------------------------------
        # Window configuration
        # ------------------------------------------

        self.setWindowTitle(
            "Romanus - Greco-Roman Reference"
        )

        self.resize(1100, 700)
        self.setMinimumSize(850, 550)

        # Accessibility information for the window.
        self.setAccessibleName("Romanus Main Window")
        self.setAccessibleDescription(
            "Greco-Roman reference application with "
            "alphabet, numeral, deity, astrology, "
            "and search reference pages."
        )

        # Initialize application components.
        self.setup_ui()
        self.setup_connections()
        self.setup_shortcuts()

        # Display Home by default.
        self.navigate_to_page("home")

    # --------------------------------------------------
    # User Interface
    # --------------------------------------------------

    def setup_ui(self):
        """Create the sidebar and application pages."""

        central_widget = QWidget()
        central_widget.setObjectName("centralWidget")

        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(12, 12, 12, 12)
        main_layout.setSpacing(12)

        # ------------------------------------------
        # Sidebar container
        # ------------------------------------------

        self.sidebar_widget = QWidget()
        self.sidebar_widget.setObjectName("sidebar")
        self.sidebar_widget.setFixedWidth(230)

        sidebar = QVBoxLayout(self.sidebar_widget)
        sidebar.setContentsMargins(12, 18, 12, 12)
        sidebar.setSpacing(8)

        # Application title.
        title = QLabel("Romanus")
        title.setObjectName("sidebarTitle")

        sidebar.addWidget(title)

        # Application subtitle.
        subtitle = QLabel("Greco-Roman Reference")
        subtitle.setObjectName("sidebarSubtitle")

        sidebar.addWidget(subtitle)

        sidebar.addSpacing(20)

        # ------------------------------------------
        # Navigation buttons
        # ------------------------------------------

        self.home_button = QPushButton("Home")
        self.search_button = QPushButton("Search")
        self.latin_button = QPushButton("Latin Alphabet")
        self.greek_button = QPushButton("Greek Alphabet")
        self.numerals_button = QPushButton("Roman Numerals")
        self.astrology_button = QPushButton("Greek Astrology")
        self.deities_button = QPushButton(
            "Greco-Roman Deities"
        )

        # Map page identifiers to navigation buttons.
        self.navigation_buttons = {
            "home": self.home_button,
            "search": self.search_button,
            "latin": self.latin_button,
            "greek": self.greek_button,
            "numerals": self.numerals_button,
            "astrology": self.astrology_button,
            "deities": self.deities_button,
        }

        # Configure accessible sidebar navigation.
        for page_name, button in self.navigation_buttons.items():

            # QSS styling identifier.
            button.setObjectName("navigationButton")

            # Consistent button dimensions.
            button.setMinimumHeight(42)

            # Support active-page highlighting.
            button.setCheckable(True)

            # Use a pointing cursor when hovering.
            button.setCursor(
                Qt.CursorShape.PointingHandCursor
            )

            # Allow keyboard focus through Tab navigation.
            button.setFocusPolicy(
                Qt.FocusPolicy.StrongFocus
            )

            # Provide information for assistive technologies.
            button.setAccessibleName(button.text())
            button.setAccessibleDescription(
                f"Navigate to the {button.text()} reference page"
            )

            # Provide a tooltip for mouse users.
            button.setToolTip(
                f"Open {button.text()}"
            )

            # Add the button to the sidebar.
            sidebar.addWidget(button)

        # Push version information to the bottom.
        sidebar.addStretch()

        version_label = QLabel("Romanus v0.8.0")
        version_label.setObjectName("sidebarVersion")

        sidebar.addWidget(version_label)

        # ------------------------------------------
        # Application pages
        # ------------------------------------------

        self.pages = QStackedWidget()
        self.pages.setObjectName("pageStack")

        self.home_page = HomePage()
        self.search_page = SearchPage()
        self.latin_page = LatinPage()
        self.greek_page = GreekPage()
        self.numerals_page = NumeralsPage()
        self.astrology_page = AstrologyPage()
        self.deities_page = DeitiesPage()

        # Map page identifiers to their widgets.
        self.page_widgets = {
            "home": self.home_page,
            "search": self.search_page,
            "latin": self.latin_page,
            "greek": self.greek_page,
            "numerals": self.numerals_page,
            "astrology": self.astrology_page,
            "deities": self.deities_page,
        }

        # Register pages in the stacked widget.
        for page in self.page_widgets.values():
            self.pages.addWidget(page)

        # Add sidebar and content area.
        main_layout.addWidget(self.sidebar_widget)
        main_layout.addWidget(self.pages, 1)

    # --------------------------------------------------
    # Signal Connections
    # --------------------------------------------------

    def setup_connections(self):
        """Connect sidebar and dashboard navigation."""

        # Connect sidebar buttons to their reference pages.
        for page_name, button in self.navigation_buttons.items():

            button.clicked.connect(
                lambda checked=False, name=page_name:
                self.navigate_to_page(name)
            )

        # Home dashboard navigation.
        self.home_page.navigate_requested.connect(
            self.navigate_to_page
        )

        # Search result navigation.
        self.search_page.navigate_requested.connect(
            self.navigate_to_page
        )

    # --------------------------------------------------
    # Keyboard Shortcuts
    # --------------------------------------------------

    def setup_shortcuts(self):
        """Configure application keyboard shortcuts."""

        # Ctrl+F opens unified search.
        self.search_shortcut = QShortcut(
            QKeySequence("Ctrl+F"),
            self
        )

        self.search_shortcut.activated.connect(
            self.open_search
        )

        # Ctrl+H opens the Home dashboard.
        self.home_shortcut = QShortcut(
            QKeySequence("Ctrl+H"),
            self
        )

        self.home_shortcut.activated.connect(
            lambda: self.navigate_to_page("home")
        )

        # Alt+Left returns to Home.
        self.back_home_shortcut = QShortcut(
            QKeySequence("Alt+Left"),
            self
        )

        self.back_home_shortcut.activated.connect(
            lambda: self.navigate_to_page("home")
        )

    # --------------------------------------------------
    # Page Navigation
    # --------------------------------------------------

    def navigate_to_page(self, page_name):
        """
        Navigate to a registered reference page.

        Args:
            page_name (str): Destination page identifier.
        """

        page = self.page_widgets.get(page_name)

        # Ignore unknown page identifiers.
        if page is None:
            return

        # Display the requested page.
        self.pages.setCurrentWidget(page)

        # Update active sidebar button highlighting.
        for name, button in self.navigation_buttons.items():
            button.setChecked(name == page_name)

        # Place keyboard focus in the search input.
        if page_name == "search":
            self.search_page.focus_search()

    # --------------------------------------------------
    # Search Navigation
    # --------------------------------------------------

    def open_search(self):
        """Open unified search using Ctrl+F."""

        self.navigate_to_page("search")
