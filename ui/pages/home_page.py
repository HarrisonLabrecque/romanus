
"""
Romanus - Home Page

Displays the main application dashboard, including
reference categories, dataset statistics, and
navigation shortcuts.

Version: 0.5.0
"""

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QLabel,
    QPushButton,
    QFrame,
    QScrollArea,
    QSizePolicy,
)

from PySide6.QtCore import Signal, Qt

from data.latin_alphabet import get_latin_alphabet
from data.greek_alphabet import get_greek_alphabet
from data.roman_numerals import get_roman_numerals
from data.deities import get_deity_count
from data.astrology import (
    get_zodiac_count,
    get_planet_count,
)


class HomePage(QWidget):
    """
    Main dashboard for the Romanus application.

    Displays reference statistics and provides
    navigation shortcuts to the reference pages.
    """

    # Signal emitted when a navigation button is clicked.
    # The signal contains the destination page name.
    navigate_requested = Signal(str)

    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):
        """Build the home dashboard interface."""

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Scroll area keeps the dashboard usable
        # when the application window is resized.
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(
            QFrame.Shape.NoFrame
        )

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
        # Statistics Section
        # -----------------------------------------

        statistics_title = QLabel(
            "Reference Library"
        )
        statistics_title.setObjectName(
            "sectionTitle"
        )

        layout.addWidget(statistics_title)

        statistics_layout = QGridLayout()
        statistics_layout.setSpacing(12)

        # Read statistics directly from the datasets.
        statistics = [
            (
                "Latin Letters",
                len(get_latin_alphabet()),
            ),
            (
                "Greek Letters",
                len(get_greek_alphabet()),
            ),
            (
                "Roman Symbols",
                len(get_roman_numerals()),
            ),
            (
                "Deities",
                get_deity_count(),
            ),
            (
                "Zodiac Signs",
                get_zodiac_count(),
            ),
            (
                "Traditional Planets",
                get_planet_count(),
            ),
        ]

        for index, (name, count) in enumerate(statistics):
            card = self.create_statistic_card(
                name,
                count
            )

            row = index // 3
            column = index % 3

            statistics_layout.addWidget(
                card,
                row,
                column
            )

        layout.addLayout(statistics_layout)

        # -----------------------------------------
        # Reference Categories
        # -----------------------------------------

        categories_title = QLabel(
            "Explore References"
        )
        categories_title.setObjectName(
            "sectionTitle"
        )

        layout.addWidget(categories_title)

        categories_layout = QGridLayout()
        categories_layout.setSpacing(12)

        categories = [
            (
                "Latin Alphabet",
                "Explore the classical Latin alphabet, "
                "letter names, and pronunciation.",
                "latin",
            ),
            (
                "Greek Alphabet",
                "Discover the 24 Greek letters, "
                "transliterations, and pronunciation.",
                "greek",
            ),
            (
                "Roman Numerals",
                "Study Roman numeral symbols and "
                "convert between numeral systems.",
                "numerals",
            ),
            (
                "Greek Astrology",
                "Explore the twelve zodiac signs "
                "and seven traditional planets.",
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

            categories_layout.addWidget(
                card,
                row,
                column
            )

        layout.addLayout(categories_layout)

        # -----------------------------------------
        # Footer
        # -----------------------------------------

        layout.addStretch()

        footer = QLabel(
            "Romanus v0.5.0 | Greco-Roman Reference Application"
        )

        footer.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        footer.setObjectName("dashboardFooter")

        layout.addWidget(footer)

        scroll_area.setWidget(container)
        main_layout.addWidget(scroll_area)

    def create_statistic_card(self, name, count):
        """
        Create a dashboard statistics card.

        Args:
            name (str): Name of the reference category.
            count (int): Number of available entries.

        Returns:
            QFrame: The configured statistics card.
        """

        card = QFrame()
        card.setObjectName("statisticCard")

        card.setFrameShape(
            QFrame.Shape.StyledPanel
        )

        card.setMinimumHeight(100)

        layout = QVBoxLayout(card)
        layout.setSpacing(6)

        count_label = QLabel(str(count))
        count_label.setObjectName("statisticValue")

        count_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        name_label = QLabel(name)
        name_label.setObjectName("statisticLabel")

        name_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        name_label.setWordWrap(True)

        layout.addWidget(count_label)
        layout.addWidget(name_label)

        return card

    def create_reference_card(self, name, description, page):
        """
        Create a reference navigation card.

        Args:
            name (str): Reference category title.
            description (str): Category description.
            page (str): Destination page identifier.

        Returns:
            QFrame: The configured reference card.
        """

        card = QFrame()
        card.setObjectName("referenceCard")

        card.setFrameShape(
            QFrame.Shape.StyledPanel
        )

        card.setMinimumHeight(155)

        card.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Preferred
        )

        layout = QVBoxLayout(card)
        layout.setSpacing(8)

        title = QLabel(name)
        title.setObjectName("referenceCardTitle")

        description_label = QLabel(description)
        description_label.setWordWrap(True)

        button = QPushButton("Explore")
        button.setObjectName("referenceButton")

        # Emit the destination when clicked.
        # Default argument captures the correct page
        # for each button created in the loop.
        button.clicked.connect(
            lambda checked=False, destination=page:
            self.navigate_requested.emit(destination)
        )

        layout.addWidget(title)
        layout.addWidget(description_label)
        layout.addStretch()
        layout.addWidget(button)

        return card
