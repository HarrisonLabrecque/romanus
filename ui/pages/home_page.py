
"""
Romanus - Home Page

Displays the application dashboard, reference statistics,
navigation shortcuts, and unified search access.

Version: 0.6.0
"""

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QLabel,
    QPushButton,
    QFrame,
    QScrollArea,
)

from PySide6.QtCore import Qt, Signal

from data.latin_alphabet import get_latin_alphabet
from data.greek_alphabet import get_greek_alphabet
from data.roman_numerals import get_roman_numerals
from data.deities import get_deity_count
from data.astrology import (
    get_zodiac_count,
    get_planet_count,
)


class HomePage(QWidget):
    """Main dashboard for the Romanus application."""

    # Signal used to request navigation to another page.
    navigate_requested = Signal(str)

    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):
        """Create the Home Page dashboard."""

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Make the dashboard scrollable.
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QFrame.Shape.NoFrame)

        container = QWidget()
        layout = QVBoxLayout(container)

        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(20)

        # -----------------------------------------
        # Welcome Section
        # -----------------------------------------

        title = QLabel("Welcome to Romanus")
        title.setObjectName("pageTitle")

        description = QLabel(
            "Explore the languages, numeral systems, "
            "mythology, and historical astrology "
            "of the Greco-Roman world."
        )
        description.setWordWrap(True)

        layout.addWidget(title)
        layout.addWidget(description)

        # -----------------------------------------
        # Unified Search
        # -----------------------------------------

        search_button = QPushButton("Search Romanus")
        search_button.setObjectName("searchButton")
        search_button.setMinimumHeight(42)

        search_button.clicked.connect(
            lambda: self.navigate_requested.emit("search")
        )

        layout.addWidget(search_button)

        # -----------------------------------------
        # Reference Statistics
        # -----------------------------------------

        statistics_title = QLabel("Reference Library")
        statistics_title.setObjectName("sectionTitle")

        layout.addWidget(statistics_title)

        statistics_layout = QGridLayout()
        statistics_layout.setSpacing(12)

        statistics = [
            ("Latin Letters", len(get_latin_alphabet())),
            ("Greek Letters", len(get_greek_alphabet())),
            ("Roman Symbols", len(get_roman_numerals())),
            ("Deities", get_deity_count()),
            ("Zodiac Signs", get_zodiac_count()),
            ("Traditional Planets", get_planet_count()),
        ]

        for index, (name, count) in enumerate(statistics):
            card = self.create_statistic_card(name, count)

            row = index // 3
            column = index % 3

            statistics_layout.addWidget(card, row, column)

        layout.addLayout(statistics_layout)

        # -----------------------------------------
        # Reference Navigation
        # -----------------------------------------

        categories_title = QLabel("Explore References")
        categories_title.setObjectName("sectionTitle")

        layout.addWidget(categories_title)

        categories_layout = QGridLayout()
        categories_layout.setSpacing(12)

        categories = [
            (
                "Latin Alphabet",
                "Explore classical Latin letters, "
                "names, and pronunciation.",
                "latin",
            ),
            (
                "Greek Alphabet",
                "Discover Greek letters, "
                "transliterations, and pronunciation.",
                "greek",
            ),
            (
                "Roman Numerals",
                "Study Roman numeral notation "
                "and convert between numeral systems.",
                "numerals",
            ),
            (
                "Greek Astrology",
                "Explore zodiac signs, traditional "
                "planets, and historical associations.",
                "astrology",
            ),
            (
                "Greco-Roman Deities",
                "Learn about Greek and Roman deities, "
                "their domains, and symbols.",
                "deities",
            ),
        ]

        for index, (name, description, page) in enumerate(categories):
            card = self.create_reference_card(
                name,
                description,
                page
            )

            row = index // 2
            column = index % 2

            categories_layout.addWidget(card, row, column)

        layout.addLayout(categories_layout)

        # -----------------------------------------
        # Footer
        # -----------------------------------------

        layout.addStretch()

        footer = QLabel(
            "Romanus v1.0.0 | Greco-Roman Reference Application"
        )
        footer.setObjectName("dashboardFooter")
        footer.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(footer)

        scroll_area.setWidget(container)
        main_layout.addWidget(scroll_area)

    def create_statistic_card(self, name, count):
        """
        Create a card displaying a reference count.

        Args:
            name (str): Reference category name.
            count (int): Number of available records.

        Returns:
            QFrame: Configured statistics card.
        """

        card = QFrame()
        card.setObjectName("statisticCard")
        card.setFrameShape(QFrame.Shape.StyledPanel)
        card.setMinimumHeight(100)

        layout = QVBoxLayout(card)
        layout.setSpacing(6)

        count_label = QLabel(str(count))
        count_label.setObjectName("statisticValue")
        count_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        name_label = QLabel(name)
        name_label.setObjectName("statisticLabel")
        name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        name_label.setWordWrap(True)

        layout.addWidget(count_label)
        layout.addWidget(name_label)

        return card

    def create_reference_card(self, name, description, page):
        """
        Create a reference navigation card.

        Args:
            name (str): Reference category name.
            description (str): Category description.
            page (str): Destination page identifier.

        Returns:
            QFrame: Configured reference card.
        """

        card = QFrame()
        card.setObjectName("referenceCard")
        card.setFrameShape(QFrame.Shape.StyledPanel)
        card.setMinimumHeight(155)

        layout = QVBoxLayout(card)
        layout.setSpacing(8)

        title = QLabel(name)
        title.setObjectName("referenceCardTitle")

        description_label = QLabel(description)
        description_label.setWordWrap(True)

        button = QPushButton("Explore")
        button.setObjectName("referenceButton")

        # Navigate to the selected reference page.
        button.clicked.connect(
            lambda checked=False, destination=page:
            self.navigate_requested.emit(destination)
        )

        layout.addWidget(title)
        layout.addWidget(description_label)
        layout.addStretch()
        layout.addWidget(button)

        return card
