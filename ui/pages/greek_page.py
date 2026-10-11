
from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QAbstractItemView,
)

from data.greek_alphabet import get_greek_alphabet


class GreekPage(QWidget):
    """Display the Greek alphabet reference."""

    def __init__(self):
        super().__init__()

        # Retrieve Greek alphabet reference data.
        self.alphabet = get_greek_alphabet()

        # Initialize the page interface.
        self.setup_ui()

        # Populate the reference table.
        self.load_alphabet()

    def setup_ui(self):
        """Create the Greek alphabet page interface."""

        layout = QVBoxLayout(self)

        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(12)

        # Page title.
        title = QLabel("Greek Alphabet")
        title.setObjectName("pageTitle")

        # Page description.
        description = QLabel(
            "Explore the 24 letters of the Greek alphabet, "
            "including their uppercase and lowercase forms, "
            "names, transliterations, and historical pronunciations."
        )

        description.setWordWrap(True)

        # Create the Greek alphabet reference table.
        self.table = QTableWidget()

        self.table.setColumnCount(6)

        self.table.setHorizontalHeaderLabels([
            "Uppercase",
            "Lowercase",
            "Name",
            "Transliteration",
            "Pronunciation",
            "Description",
        ])

        # Prevent users from editing reference information.
        self.table.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )

        # Select complete rows.
        self.table.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )

        # Allow only one row to be selected at a time.
        self.table.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )

        # Hide row numbers.
        self.table.verticalHeader().setVisible(False)

        # Configure table column resizing.
        header = self.table.horizontalHeader()

        header.setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents
        )

        # Allow the description column to expand.
        header.setSectionResizeMode(
            5,
            QHeaderView.ResizeMode.Stretch
        )

        # Add widgets to the page layout.
        layout.addWidget(title)
        layout.addWidget(description)
        layout.addWidget(self.table)

    def load_alphabet(self):
        """Populate the table with Greek alphabet data."""

        self.table.setRowCount(len(self.alphabet))

        for row, letter in enumerate(self.alphabet):

            values = [
                letter["uppercase"],
                letter["lowercase"],
                letter["name"],
                letter["transliteration"],
                letter["pronunciation"],
                letter["description"],
            ]

            for column, value in enumerate(values):

                item = QTableWidgetItem(str(value))

                # Center the shorter reference fields.
                if column < 5:
                    item.setTextAlignment(
                        Qt.AlignmentFlag.AlignCenter
                    )

                self.table.setItem(row, column, item)
