
"""
Romanus - Main Application Window

Manages the sidebar, reference pages, unified search,
keyboard shortcuts, and accessibility features.

Version: 1.0.0
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
        # Window Configuration
        # ------------------------------------------

        self.setWindowTitle(
            "Romanus - Greco-Roman Reference"
        )

        self.resize(1100, 700)
        self.setMinimumSize(850, 550)

        # Main window accessibility information.
        self.setAccessibleName("Romanus Main Window")
        self.setAccessibleDescription(
            "Greco-Roman reference application featuring "
            "alphabets, Roman numerals, astrology, "
            "deities, and unified search."
        )

        # Initialize the interface.
        self.setup_ui()
        self.setup_connections()
        self.setup_shortcuts()

        # Open the Home dashboard by default.
        self.navigate_to_page("home")

    # --------------------------------------------------
    # User Interface
    # --------------------------------------------------

    def setup_ui(self):
        """Build the sidebar and reference page container."""

        central_widget = QWidget()
        central_widget.setObjectName("centralWidget")

        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(12, 12, 12, 12)
        main_layout.setSpacing(12)

        # ------------------------------------------
        # Sidebar
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
        # Navigation Buttons
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

        # Navigation button registry.
        self.navigation_buttons = {
            "home": self.home_button,
            "search": self.search_button,
            "latin": self.latin_button,
            "greek": self.greek_button,
            "numerals": self.numerals_button,
            "astrology": self.astrology_button,
            "deities": self.deities_button,
        }

        # Configure navigation accessibility and styling.
        for page_name, button in self.navigation_buttons.items():

            button.setObjectName("navigationButton")
            button.setMinimumHeight(42)
            button.setCheckable(True)

            button.setCursor(
                Qt.CursorShape.PointingHandCursor
            )

            # Enable keyboard focus.
            button.setFocusPolicy(
                Qt.FocusPolicy.StrongFocus
            )

            # Accessible information.
            button.setAccessibleName(button.text())
            button.setAccessibleDescription(
                f"Navigate to the {button.text()} reference page"
            )

            # Navigation tooltip.
            button.setToolTip(
                f"Open {button.text()}"
            )

            sidebar.addWidget(button)

        sidebar.addStretch()

        # Display current application version.
        version_label = QLabel("Romanus v1.0.0")
        version_label.setObjectName("sidebarVersion")
        sidebar.addWidget(version_label)

        # ------------------------------------------
        # Reference Pages
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

        # Reference page registry.
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

        # Add sidebar and page container.
        main_layout.addWidget(self.sidebar_widget)
        main_layout.addWidget(self.pages, 1)

    # --------------------------------------------------
    # Signal Connections
    # --------------------------------------------------

    def setup_connections(self):
        """Connect navigation buttons and page signals."""

        for page_name, button in self.navigation_buttons.items():

            button.clicked.connect(
                lambda checked=False, name=page_name:
                self.navigate_to_page(name)
            )

        # Home dashboard navigation.
        self.home_page.navigate_requested.connect(
            self.navigate_to_page
        )

        # Unified search navigation.
        self.search_page.navigate_requested.connect(
            self.navigate_to_page
        )

    # --------------------------------------------------
    # Keyboard Shortcuts
    # --------------------------------------------------

    def setup_shortcuts(self):
        """Register application keyboard shortcuts."""

        # Ctrl+F opens Search.
        self.search_shortcut = QShortcut(
            QKeySequence("Ctrl+F"),
            self
        )

        self.search_shortcut.activated.connect(
            self.open_search
        )

        # Ctrl+H opens Home.
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

        if page is None:
            return

        # Display the requested page.
        self.pages.setCurrentWidget(page)

        # Update active navigation button state.
        for name, button in self.navigation_buttons.items():
            button.setChecked(name == page_name)

        # Focus the search field when opening Search.
        if page_name == "search":
            self.search_page.focus_search()

    # --------------------------------------------------
    # Search Navigation
    # --------------------------------------------------

    def open_search(self):
        """Open unified search."""

        self.navigate_to_page("search")
