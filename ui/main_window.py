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
    """Main application window."""

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Greco-Roman Reference")
        self.resize(1000, 650)

        # Main central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Main horizontal layout
        main_layout = QHBoxLayout(central_widget)

        # -------------------------
        # Navigation sidebar
        # -------------------------

        sidebar = QVBoxLayout()

        title = QLabel("Greco-Roman")
        sidebar.addWidget(title)

        self.home_button = QPushButton("Home")
        self.latin_button = QPushButton("Latin Alphabet")
        self.greek_button = QPushButton("Greek Alphabet")
        self.numerals_button = QPushButton("Roman Numerals")
        self.astrology_button = QPushButton("Greek Astrology")
        self.deities_button = QPushButton("Greco-Roman Deities")

        sidebar.addWidget(self.home_button)
        sidebar.addWidget(self.latin_button)
        sidebar.addWidget(self.greek_button)
        sidebar.addWidget(self.numerals_button)
        sidebar.addWidget(self.astrology_button)
        sidebar.addWidget(self.deities_button)

        # Push navigation buttons toward the top.
        sidebar.addStretch()

        # -------------------------
        # Application pages
        # -------------------------

        self.pages = QStackedWidget()

        self.home_page = HomePage()
        self.latin_page = LatinPage()
        self.greek_page = GreekPage()
        self.numerals_page = NumeralsPage()
        self.astrology_page = AstrologyPage()
        self.deities_page = DeitiesPage()

        self.pages.addWidget(self.home_page)
        self.pages.addWidget(self.latin_page)
        self.pages.addWidget(self.greek_page)
        self.pages.addWidget(self.numerals_page)
        self.pages.addWidget(self.astrology_page)
        self.pages.addWidget(self.deities_page)

        # -------------------------
        # Button connections
        # -------------------------

        self.home_button.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.home_page)
        )

        self.latin_button.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.latin_page)
        )

        self.greek_button.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.greek_page)
        )

        self.numerals_button.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.numerals_page)
        )

        self.astrology_button.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.astrology_page)
        )

        self.deities_button.clicked.connect(
            lambda: self.pages.setCurrentWidget(self.deities_page)
        )

        # Add sidebar and page area to main layout.
        main_layout.addLayout(sidebar)
        main_layout.addWidget(self.pages, 1)