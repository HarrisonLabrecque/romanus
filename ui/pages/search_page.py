
"""
Romanus - Unified Search Page

Provides a searchable reference table, category
filters, result details, and page navigation.

Version: 0.6.0
"""

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QComboBox,
    QTableWidget,
    QTableWidgetItem,
    QAbstractItemView,
    QHeaderView,
    QTextEdit,
    QPushButton,
    QGroupBox,
    QSplitter,
)

from PySide6.QtCore import Qt, Signal

from services.search_service import SearchService


class SearchPage(QWidget):
    """Display unified search results across Romanus."""

    # Request navigation to a reference page.
    navigate_requested = Signal(str)

    def __init__(self):
        super().__init__()

        self.results = []

        self.setup_ui()
        self.load_results()

    def setup_ui(self):
        """Create the unified search interface."""

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(12)

        # Page heading.
        title = QLabel("Unified Search")
        title.setObjectName("pageTitle")

        description = QLabel(
            "Search across all Romanus reference categories."
        )
        description.setWordWrap(True)

        layout.addWidget(title)
        layout.addWidget(description)

        # Search controls.
        controls = QHBoxLayout()

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText(
            "Search letters, numerals, deities, or astrology..."
        )
        self.search_input.setClearButtonEnabled(True)

        self.category_filter = QComboBox()
        self.category_filter.addItems(
            SearchService.get_categories()
        )

        controls.addWidget(self.search_input, 1)
        controls.addWidget(self.category_filter)

        layout.addLayout(controls)

        # Result counter.
        self.result_count = QLabel("")
        layout.addWidget(self.result_count)

        # Split search results and detail viewer.
        splitter = QSplitter(Qt.Orientation.Vertical)

        self.results_table = QTableWidget()
        self.results_table.setColumnCount(3)
        self.results_table.setHorizontalHeaderLabels(
            ["Category", "Reference", "Information"]
        )

        self.results_table.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )

        self.results_table.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )

        self.results_table.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )

        self.results_table.verticalHeader().setVisible(False)

        header = self.results_table.horizontalHeader()
        header.setSectionResizeMode(
            0, QHeaderView.ResizeMode.ResizeToContents
        )
        header.setSectionResizeMode(
            1, QHeaderView.ResizeMode.ResizeToContents
        )
        header.setSectionResizeMode(
            2, QHeaderView.ResizeMode.Stretch
        )

        splitter.addWidget(self.results_table)

        # Selected result details.
        details_group = QGroupBox("Reference Information")
        details_layout = QVBoxLayout(details_group)

        self.detail_title = QLabel("Select a search result.")
        self.detail_title.setObjectName("searchDetailTitle")

        self.detail_category = QLabel("")

        self.detail_description = QTextEdit()
        self.detail_description.setReadOnly(True)

        self.open_button = QPushButton("Open Reference Page")
        self.open_button.setEnabled(False)

        details_layout.addWidget(self.detail_title)
        details_layout.addWidget(self.detail_category)
        details_layout.addWidget(self.detail_description)
        details_layout.addWidget(self.open_button)

        splitter.addWidget(details_group)
        splitter.setStretchFactor(0, 3)
        splitter.setStretchFactor(1, 2)

        layout.addWidget(splitter)

        # Connect search interactions.
        self.search_input.textChanged.connect(
            self.load_results
        )

        self.category_filter.currentTextChanged.connect(
            self.load_results
        )

        self.results_table.itemSelectionChanged.connect(
            self.display_selected_result
        )

        self.results_table.itemDoubleClicked.connect(
            self.open_selected_result
        )

        self.open_button.clicked.connect(
            self.open_selected_result
        )

    def load_results(self, *_args):
        """Search the datasets and populate the results table."""

        query = self.search_input.text()
        category = self.category_filter.currentText()

        self.results = SearchService.search(
            query,
            category
        )

        self.results_table.blockSignals(True)
        self.results_table.setRowCount(len(self.results))

        for row, record in enumerate(self.results):
            values = [
                record["category"],
                record["title"],
                record["subtitle"],
            ]

            for column, value in enumerate(values):
                self.results_table.setItem(
                    row,
                    column,
                    QTableWidgetItem(str(value))
                )

        self.results_table.blockSignals(False)

        self.result_count.setText(
            f"{len(self.results)} reference(s) found"
        )

        self.clear_details()

        if self.results:
            self.results_table.selectRow(0)

    def display_selected_result(self):
        """Show the details of the selected search result."""

        row = self.results_table.currentRow()

        if row < 0 or row >= len(self.results):
            self.clear_details()
            return

        record = self.results[row]

        self.detail_title.setText(record["title"])
        self.detail_category.setText(
            f"{record['category']} | {record['subtitle']}"
        )
        self.detail_description.setPlainText(
            record["description"]
        )

        self.open_button.setEnabled(True)

    def open_selected_result(self, *_args):
        """Open the reference page for the selected result."""

        row = self.results_table.currentRow()

        if row < 0 or row >= len(self.results):
            return

        page_name = self.results[row]["page"]
        self.navigate_requested.emit(page_name)

    def clear_details(self):
        """Clear the selected reference information."""

        self.detail_title.setText("Select a search result.")
        self.detail_category.clear()
        self.detail_description.clear()
        self.open_button.setEnabled(False)

    def focus_search(self):
        """Move keyboard focus to the search input."""

        self.search_input.setFocus()
        self.search_input.selectAll()
