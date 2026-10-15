
"""
Romanus - Main Application Window

Manages the application's sidebar navigation,
reference pages, and Home Page dashboard shortcuts.

Version: 0.5.0
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

from ui.pages.home_page import HomePage
from ui.pages.latin_page import LatinPage
from ui.pages.greek_page import GreekPage
from ui.pages.numerals_page import NumeralsPage
from ui.pages.astrology_page import AstrologyPage
from ui.pages.deities_page import DeitiesPage


class MainWindow(QMainWindow):
    """
    Main application window for Romanus.

    Provides sidebar navigation and manages the
    reference pages through a QStackedWidget.
    """

    def __init__(self):
        super().__init__()

        # Configure the main application window.
        self.setWindowTitle("Romanus - Greco-Roman Reference")
        self.resize(1000, 650)
        self.setMinimumSize(850, 550)

        # Build the interface.
        self.setup_ui()

        # Connect navigation signals.
        self.setup_connections()

        # Display the Home Page when Romanus starts.
        self.navigate_to_page("home")

    def setup_ui(self):
        """Create the main window layout and reference pages."""

        # -----------------------------------------
        # Main Central Widget
        # -----------------------------------------

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(12)

        # -----------------------------------------
        # Navigation Sidebar
        # -----------------------------------------

        sidebar = QVBoxLayout()
        sidebar.setSpacing(8)

        title = QLabel("Romanus")
        title.setObjectName("sidebarTitle")

        sidebar.addWidget(title)

        # Create navigation buttons.
        self.home_button = QPushButton("Home")
        self.latin_button = QPushButton("Latin Alphabet")
        self.greek_button = QPushButton("Greek Alphabet")
        self.numerals_button = QPushButton("Roman Numerals")
        self.astrology_button = QPushButton("Greek Astrology")
        self.deities_button = QPushButton("Greco-Roman Deities")

        # Store buttons by their page identifiers.
        self.navigation_buttons = {
            "home": self.home_button,
            "latin": self.latin_button,
            "greek": self.greek_button,
            "numerals": self.numerals_button,
            "astrology": self.astrology_button,
            "deities": self.deities_button,
        }

        # Add navigation buttons to the sidebar.
        for button in self.navigation_buttons.values():
            button.setMinimumHeight(36)

            # Make the selected page visually identifiable.
            button.setCheckable(True)

            sidebar.addWidget(button)

        # Keep navigation buttons at the top.
        sidebar.addStretch()

        # -----------------------------------------
        # Application Pages
        # -----------------------------------------

        self.pages = QStackedWidget()

        # Initialize existing reference pages.
        self.home_page = HomePage()
        self.latin_page = LatinPage()
        self.greek_page = GreekPage()
        self.numerals_page = NumeralsPage()
        self.astrology_page = AstrologyPage()
        self.deities_page = DeitiesPage()

        # Store pages by their identifiers.
        self.page_widgets = {
            "home": self.home_page,
            "latin": self.latin_page,
            "greek": self.greek_page,
            "numerals": self.numerals_page,
            "astrology": self.astrology_page,
            "deities": self.deities_page,
        }

        # Add pages to the stacked widget.
        for page in self.page_widgets.values():
            self.pages.addWidget(page)

        # -----------------------------------------
        # Final Layout
        # -----------------------------------------

        main_layout.addLayout(sidebar)
        main_layout.addWidget(self.pages, 1)

    def setup_connections(self):
        """
        Connect sidebar buttons and Home Page shortcuts
        to the application's navigation system.
        """

        # Connect each sidebar button to its page.
        for page_name, button in self.navigation_buttons.items():
            button.clicked.connect(
                lambda checked=False, name=page_name:
                self.navigate_to_page(name)
            )

        # Connect dashboard Explore buttons.
        self.home_page.navigate_requested.connect(
            self.navigate_to_page
        )

    def navigate_to_page(self, page_name):
        """
        Navigate to a reference page.

        Args:
            page_name (str): Identifier of the destination page.
        """

        # Find the destination page.
        page = self.page_widgets.get(page_name)

        # Ignore unknown page identifiers.
        if page is None:
            return

        # Display the selected page.
        self.pages.setCurrentWidget(page)

        # Update sidebar button states.
        for name, button in self.navigation_buttons.items():
            button.setChecked(name == page_name)
