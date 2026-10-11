
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGroupBox,
    QLabel,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QAbstractItemView,
    QHeaderView,
    QScrollArea,
)

from PySide6.QtCore import Qt

from data.roman_numerals import (
    get_roman_numerals,
    get_subtractive_numerals,
)

from services.roman_numeral_service import RomanNumeralService


class NumeralsPage(QWidget):
    """Roman numeral reference and conversion page."""

    def __init__(self):
        super().__init__()

        # Load the reference datasets.
        self.numerals = get_roman_numerals()
        self.subtractive_numerals = get_subtractive_numerals()

        # Initialize the interface.
        self.setup_ui()
        self.load_numerals()
        self.load_subtractive_numerals()

    def setup_ui(self):
        """Build the Roman numeral page."""

        # Allow the page to scroll on smaller windows.
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(
            QScrollArea.Shape.NoFrame
        )

        content = QWidget()
        layout = QVBoxLayout(content)

        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(12)

        # Page heading.
        title = QLabel("Roman Numerals")
        title.setObjectName("pageTitle")

        description = QLabel(
            "Convert numbers between Arabic and Roman notation, "
            "and explore the Roman numeral reference tables."
        )
        description.setWordWrap(True)

        layout.addWidget(title)
        layout.addWidget(description)

        # Create the converter interface.
        self.setup_converter(layout)

        # Primary Roman numeral reference.
        primary_label = QLabel("Primary Roman Numerals")
        layout.addWidget(primary_label)

        self.numerals_table = QTableWidget()
        self.numerals_table.setColumnCount(4)
        self.numerals_table.setHorizontalHeaderLabels(
            ["Symbol", "Value", "Latin Name", "Description"]
        )

        self.configure_table(self.numerals_table)
        layout.addWidget(self.numerals_table)

        # Subtractive numeral reference.
        subtractive_label = QLabel(
            "Subtractive Combinations"
        )
        layout.addWidget(subtractive_label)

        self.subtractive_table = QTableWidget()
        self.subtractive_table.setColumnCount(3)
        self.subtractive_table.setHorizontalHeaderLabels(
            ["Symbol", "Value", "Description"]
        )

        self.configure_table(self.subtractive_table)
        layout.addWidget(self.subtractive_table)

        # Attach scrollable content to the page.
        scroll_area.setWidget(content)

        page_layout = QVBoxLayout(self)
        page_layout.setContentsMargins(0, 0, 0, 0)
        page_layout.addWidget(scroll_area)

    def setup_converter(self, layout):
        """Create the two-way Roman numeral converter."""

        converter_group = QGroupBox("Roman Numeral Converter")
        converter_layout = QVBoxLayout(converter_group)

        # Arabic number input.
        arabic_row = QHBoxLayout()

        self.arabic_input = QLineEdit()
        self.arabic_input.setPlaceholderText(
            "Enter a number (1-3999)"
        )

        self.to_roman_button = QPushButton(
            "Convert to Roman"
        )

        arabic_row.addWidget(self.arabic_input)
        arabic_row.addWidget(self.to_roman_button)

        converter_layout.addLayout(arabic_row)

        # Roman numeral input.
        roman_row = QHBoxLayout()

        self.roman_input = QLineEdit()
        self.roman_input.setPlaceholderText(
            "Enter a Roman numeral (e.g. MMXXVI)"
        )

        self.to_arabic_button = QPushButton(
            "Convert to Arabic"
        )

        roman_row.addWidget(self.roman_input)
        roman_row.addWidget(self.to_arabic_button)

        converter_layout.addLayout(roman_row)

        # Display conversion results and errors.
        self.result_label = QLabel(
            "Enter a value and select a conversion."
        )
        self.result_label.setWordWrap(True)
        self.result_label.setObjectName(
            "conversionResult"
        )

        converter_layout.addWidget(self.result_label)

        # Connect buttons to conversion methods.
        self.to_roman_button.clicked.connect(
            self.convert_to_roman
        )

        self.to_arabic_button.clicked.connect(
            self.convert_to_arabic
        )

        # Allow Enter to trigger the appropriate conversion.
        self.arabic_input.returnPressed.connect(
            self.convert_to_roman
        )

        self.roman_input.returnPressed.connect(
            self.convert_to_arabic
        )

        layout.addWidget(converter_group)

    def convert_to_roman(self):
        """Convert an Arabic integer to a Roman numeral."""

        text = self.arabic_input.text().strip()

        if not text:
            self.result_label.setText(
                "Error: Please enter an Arabic number."
            )
            return

        try:
            # Convert the text into an integer.
            number = int(text)

            # Use the service for conversion and validation.
            roman = RomanNumeralService.to_roman(number)

            self.result_label.setText(
                f"Result: {number} = {roman}"
            )

        except ValueError as error:
            self.result_label.setText(
                f"Error: {error}"
            )

    def convert_to_arabic(self):
        """Convert a Roman numeral to an Arabic integer."""

        text = self.roman_input.text().strip()

        try:
            # Validate and convert through the service.
            number = RomanNumeralService.from_roman(text)

            self.result_label.setText(
                f"Result: {text.upper()} = {number}"
            )

        except (TypeError, ValueError) as error:
            self.result_label.setText(
                f"Error: {error}"
            )

    def configure_table(self, table):
        """Configure a read-only Roman numeral reference table."""

        table.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )

        table.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )

        table.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )

        table.verticalHeader().setVisible(False)

        header = table.horizontalHeader()

        for column in range(table.columnCount() - 1):
            header.setSectionResizeMode(
                column,
                QHeaderView.ResizeMode.ResizeToContents
            )

        header.setSectionResizeMode(
            table.columnCount() - 1,
            QHeaderView.ResizeMode.Stretch
        )

    def load_numerals(self):
        """Populate the primary Roman numeral table."""

        self.numerals_table.setRowCount(
            len(self.numerals)
        )

        for row, numeral in enumerate(self.numerals):
            values = [
                numeral["symbol"],
                str(numeral["value"]),
                numeral["name"],
                numeral["description"],
            ]

            for column, value in enumerate(values):
                item = QTableWidgetItem(value)

                if column < 3:
                    item.setTextAlignment(
                        Qt.AlignmentFlag.AlignCenter
                    )

                self.numerals_table.setItem(
                    row, column, item
                )

        # Fit the table to its seven rows.
        self.numerals_table.resizeRowsToContents()

        header_height = (
            self.numerals_table.horizontalHeader().height()
        )

        rows_height = sum(
            self.numerals_table.rowHeight(row)
            for row in range(self.numerals_table.rowCount())
        )

        self.numerals_table.setFixedHeight(
            header_height + rows_height + 4
        )

    def load_subtractive_numerals(self):
        """Populate the subtractive combinations table."""

        self.subtractive_table.setRowCount(
            len(self.subtractive_numerals)
        )

        for row, numeral in enumerate(
            self.subtractive_numerals
        ):
            values = [
                numeral["symbol"],
                str(numeral["value"]),
                numeral["description"],
            ]

            for column, value in enumerate(values):
                item = QTableWidgetItem(value)

                if column < 2:
                    item.setTextAlignment(
                        Qt.AlignmentFlag.AlignCenter
                    )

                self.subtractive_table.setItem(
                    row, column, item
                )

        # Fit the table to its six rows.
        self.subtractive_table.resizeRowsToContents()

        header_height = (
            self.subtractive_table.horizontalHeader().height()
        )

        rows_height = sum(
            self.subtractive_table.rowHeight(row)
            for row in range(self.subtractive_table.rowCount())
        )

        self.subtractive_table.setFixedHeight(
            header_height + rows_height + 4
        )
