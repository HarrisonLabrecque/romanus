
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

from data.latin_alphabet import get_latin_alphabet


class LatinPage(QWidget):
    """Display the classical Latin alphabet reference."""

    def __init__(self):
        super().__init__()

        # Retrieve Latin alphabet reference data.
        self.alphabet = get_latin_alphabet()

        # Initialize the page interface.
        self.setup_ui()

        # Populate the reference table.
        self.load_alphabet()

    def setup_ui(self):
        """Create the Latin alphabet page interface."""

        layout = QVBoxLayout(self)

        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(12)

        # Page title.
        title = QLabel("Latin Alphabet")
        title.setObjectName("pageTitle")

        # Page description.
        description = QLabel(
            "Explore the 26 letters of the classical Latin "
            "alphabet, including their forms, names, "
            "pronunciations, and historical information."
        )

        description.setWordWrap(True)

        # Create the reference table.
        self.table = QTableWidget()

        self.table.setColumnCount(5)

        self.table.setHorizontalHeaderLabels([
            "Uppercase",
            "Lowercase",
            "Name",
            "Pronunciation",
            "Description",
        ])

        # Prevent editing of reference information.
        self.table.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )

        # Select complete rows.
        self.table.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )

        # Allow only one selected row.
        self.table.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )

        # Hide row numbers.
        self.table.verticalHeader().setVisible(False)

        # Configure column resizing.
        header = self.table.horizontalHeader()

        header.setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents
        )

        header.setSectionResizeMode(
            4,
            QHeaderView.ResizeMode.Stretch
        )

        # Add widgets to the layout.
        layout.addWidget(title)
        layout.addWidget(description)
        layout.addWidget(self.table)

    def load_alphabet(self):
        """Populate the table with Latin alphabet data."""

        self.table.setRowCount(len(self.alphabet))

        for row, letter in enumerate(self.alphabet):

            values = [
                letter["uppercase"],
                letter["lowercase"],
                letter["name"],
                letter["pronunciation"],
                letter["description"],
            ]

            for column, value in enumerate(values):

                item = QTableWidgetItem(str(value))

                # Center the shorter reference fields.
                if column < 4:
                    item.setTextAlignment(
                        Qt.AlignmentFlag.AlignCenter
                    )

                self.table.setItem(row, column, item)
