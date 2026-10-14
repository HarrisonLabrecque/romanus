
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QTableWidget,
    QTableWidgetItem,
    QAbstractItemView,
    QHeaderView,
    QGroupBox,
    QTextEdit,
    QSplitter,
)

from PySide6.QtCore import Qt

from data.deities import (
    get_deities,
    get_deity_by_id,
    search_deities,
)


class DeitiesPage(QWidget):
    """Page for Greco-Roman deity reference information."""

    def __init__(self):
        super().__init__()

        # Load the deity reference dataset.
        self.deities = get_deities()

        # Build the interface.
        self.setup_ui()

        # Display the initial deity records.
        self.load_deities(self.deities)

    def setup_ui(self):
        """Create the Greco-Roman deity reference interface."""

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(12)

        # Page title.
        title = QLabel("Greco-Roman Deities")
        title.setObjectName("pageTitle")

        description = QLabel(
            "Explore major Greek deities, their commonly "
            "associated Roman counterparts, domains, "
            "symbols, and mythological descriptions."
        )
        description.setWordWrap(True)

        layout.addWidget(title)
        layout.addWidget(description)

        # Search bar.
        search_layout = QHBoxLayout()

        search_label = QLabel("Search:")

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText(
            "Search by name, domain, or symbol..."
        )
        self.search_input.setClearButtonEnabled(True)

        search_layout.addWidget(search_label)
        search_layout.addWidget(self.search_input)

        layout.addLayout(search_layout)

        # Split the page into reference table and details.
        splitter = QSplitter(Qt.Orientation.Vertical)

        # Deity reference table.
        self.deities_table = QTableWidget()
        self.deities_table.setColumnCount(3)
        self.deities_table.setHorizontalHeaderLabels(
            ["Greek Name", "Roman Name", "Domain"]
        )

        self.configure_table()
        splitter.addWidget(self.deities_table)

        # Deity details section.
        details_group = QGroupBox("Deity Information")
        details_layout = QVBoxLayout(details_group)

        self.deity_name_label = QLabel(
            "Select a deity to view information."
        )

        self.deity_name_label.setObjectName(
            "deityDetailTitle"
        )

        self.domain_label = QLabel("")
        self.domain_label.setWordWrap(True)

        self.symbols_label = QLabel("")
        self.symbols_label.setWordWrap(True)

        self.description_text = QTextEdit()
        self.description_text.setReadOnly(True)
        self.description_text.setPlaceholderText(
            "Deity descriptions will appear here."
        )

        details_layout.addWidget(self.deity_name_label)
        details_layout.addWidget(self.domain_label)
        details_layout.addWidget(self.symbols_label)
        details_layout.addWidget(self.description_text)

        splitter.addWidget(details_group)

        # Allocate more initial space to the reference table.
        splitter.setStretchFactor(0, 3)
        splitter.setStretchFactor(1, 2)

        layout.addWidget(splitter)

        # Connect user interactions.
        self.search_input.textChanged.connect(
            self.filter_deities
        )

        self.deities_table.itemSelectionChanged.connect(
            self.display_selected_deity
        )

    def configure_table(self):
        """Configure the read-only deity reference table."""

        self.deities_table.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )

        self.deities_table.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )

        self.deities_table.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )

        self.deities_table.verticalHeader().setVisible(False)

        header = self.deities_table.horizontalHeader()

        header.setSectionResizeMode(
            0, QHeaderView.ResizeMode.ResizeToContents
        )

        header.setSectionResizeMode(
            1, QHeaderView.ResizeMode.ResizeToContents
        )

        header.setSectionResizeMode(
            2, QHeaderView.ResizeMode.Stretch
        )

    def load_deities(self, deities):
        """
        Populate the table with deity records.

        Args:
            deities (list): Deity reference records.
        """

        # Temporarily block selection signals during updates.
        self.deities_table.blockSignals(True)

        self.deities_table.setRowCount(len(deities))

        for row, deity in enumerate(deities):
            values = [
                deity["greek_name"],
                deity["roman_name"],
                deity["domain"],
            ]

            for column, value in enumerate(values):
                item = QTableWidgetItem(value)

                # Store the unique deity ID on the first column.
                if column == 0:
                    item.setData(
                        Qt.ItemDataRole.UserRole,
                        deity["id"]
                    )

                self.deities_table.setItem(
                    row, column, item
                )

        self.deities_table.blockSignals(False)

        # Clear outdated selection and details.
        self.deities_table.clearSelection()
        self.clear_details()

        # Automatically select the first available deity.
        if deities:
            self.deities_table.selectRow(0)

    def filter_deities(self, text):
        """Filter deity records using the search field."""

        filtered_deities = search_deities(text)

        self.load_deities(filtered_deities)

    def display_selected_deity(self):
        """Display information about the selected deity."""

        selected_row = self.deities_table.currentRow()

        if selected_row < 0:
            self.clear_details()
            return

        # Retrieve the deity ID stored in the table.
        item = self.deities_table.item(selected_row, 0)

        if item is None:
            self.clear_details()
            return

        deity_id = item.data(Qt.ItemDataRole.UserRole)

        deity = get_deity_by_id(deity_id)

        if deity is None:
            self.clear_details()
            return

        # Update the deity detail panel.
        self.deity_name_label.setText(
            f"{deity['greek_name']} / {deity['roman_name']}"
        )

        self.domain_label.setText(
            f"Domain: {deity['domain']}"
        )

        self.symbols_label.setText(
            "Symbols: " + ", ".join(deity["symbols"])
        )

        self.description_text.setPlainText(
            deity["description"]
        )

    def clear_details(self):
        """Clear the deity information panel."""

        self.deity_name_label.setText(
            "Select a deity to view information."
        )

        self.domain_label.clear()
        self.symbols_label.clear()
        self.description_text.clear()
