
"""
Romanus - Main Application Window

Manages sidebar navigation, the Home dashboard,
reference pages, and unified search.

Version: 0.8.0
"""

from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QStackedWidget,
)

from PySide6.QtGui import QShortcut, QKeySequence

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

        self.setWindowTitle(
            "Romanus - Greco-Roman Reference"
        )

        self.resize(1100, 700)
        self.setMinimumSize(850, 550)

        self.setup_ui()
        self.setup_connections()
        self.setup_shortcuts()

        self.navigate_to_page("home")

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

        title = QLabel("Romanus")
        title.setObjectName("sidebarTitle")
        sidebar.addWidget(title)

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

        self.navigation_buttons = {
            "home": self.home_button,
            "search": self.search_button,
            "latin": self.latin_button,
            "greek": self.greek_button,
            "numerals": self.numerals_button,
            "astrology": self.astrology_button,
            "deities": self.deities_button,
        }

        for button in self.navigation_buttons.values():
            button.setObjectName("navigationButton")
            button.setMinimumHeight(42)
            button.setCheckable(True)
            button.setCursor(
                __import__(
                    "PySide6.QtCore",
                    fromlist=["Qt"]
                ).Qt.CursorShape.PointingHandCursor
            )
            sidebar.addWidget(button)

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

        self.page_widgets = {
            "home": self.home_page,
            "search": self.search_page,
            "latin": self.latin_page,
            "greek": self.greek_page,
            "numerals": self.numerals_page,
            "astrology": self.astrology_page,
            "deities": self.deities_page,
        }

        for page in self.page_widgets.values():
            self.pages.addWidget(page)

        main_layout.addWidget(self.sidebar_widget)
        main_layout.addWidget(self.pages, 1)

    def setup_connections(self):
        """Connect sidebar and dashboard navigation."""

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

    def setup_shortcuts(self):
        """Configure application keyboard shortcuts."""

        self.search_shortcut = QShortcut(
            QKeySequence("Ctrl+F"),
            self
        )

        self.search_shortcut.activated.connect(
            self.open_search
        )

    def navigate_to_page(self, page_name):
        """Navigate to a reference page."""

        page = self.page_widgets.get(page_name)

        if page is None:
            return

        self.pages.setCurrentWidget(page)

        # Highlight the active navigation button.
        for name, button in self.navigation_buttons.items():
            button.setChecked(name == page_name)

        if page_name == "search":
            self.search_page.focus_search()

    def open_search(self):
        """Open unified search using Ctrl+F."""

        self.navigate_to_page("search")
