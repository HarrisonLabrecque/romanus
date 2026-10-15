
"""
Romanus - Greek and Hellenistic Astrology Page

Displays historical reference information about
the twelve zodiac signs and seven traditional planets.

Version: 0.7.0
"""

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QTableWidget,
    QTableWidgetItem,
    QAbstractItemView,
    QHeaderView,
    QGroupBox,
    QTextEdit,
    QSplitter,
    QTabWidget,
    QComboBox,
    QSpinBox,
    QPushButton,
    QHBoxLayout,
)

from PySide6.QtCore import Qt

from services.zodiac_service import ZodiacService

from data.astrology import (
    get_zodiac_signs,
    get_traditional_planets,
    search_zodiac_signs,
    search_traditional_planets,
)


class AstrologyPage(QWidget):
    """Page for Greek and Hellenistic astrology references."""

    def __init__(self):
        super().__init__()

        # Load the reference datasets.
        self.zodiac_signs = get_zodiac_signs()
        self.planets = get_traditional_planets()

        # Build the interface.
        self.setup_ui()

        # Populate both reference tables.
        self.load_zodiac_signs(self.zodiac_signs)
        self.load_planets(self.planets)

    def setup_ui(self):
        """Create the astrology reference interface."""

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(12)

        # Page title.
        title = QLabel("Greek and Hellenistic Astrology")
        title.setObjectName("pageTitle")

        description = QLabel(
            "Explore the twelve zodiac signs, seven traditional "
            "planets, and their historical astrological associations."
        )
        description.setWordWrap(True)

        layout.addWidget(title)
        layout.addWidget(description)

        # Separate zodiac and planetary information.
        self.tabs = QTabWidget()

        self.setup_zodiac_tab()
        self.setup_planets_tab()
        self.setup_explorer_tab()

        layout.addWidget(self.tabs)

    def setup_zodiac_tab(self):
        """Create the zodiac sign reference tab."""

        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setSpacing(10)

        # Search field.
        self.zodiac_search = QLineEdit()
        self.zodiac_search.setPlaceholderText(
            "Search zodiac signs by name, element, or ruler..."
        )
        self.zodiac_search.setClearButtonEnabled(True)

        layout.addWidget(self.zodiac_search)

        # Split the reference table and detail viewer.
        splitter = QSplitter(Qt.Orientation.Vertical)

        self.zodiac_table = QTableWidget()
        self.zodiac_table.setColumnCount(6)
        self.zodiac_table.setHorizontalHeaderLabels(
            [
                "Symbol",
                "Sign",
                "Greek Name",
                "Element",
                "Modality",
                "Ruling Planet",
            ]
        )

        self.configure_table(self.zodiac_table)
        splitter.addWidget(self.zodiac_table)

        # Detail viewer.
        details_group = QGroupBox("Zodiac Sign Information")
        details_layout = QVBoxLayout(details_group)

        self.zodiac_name_label = QLabel(
            "Select a zodiac sign."
        )
        self.zodiac_name_label.setObjectName(
            "astrologyDetailTitle"
        )

        self.zodiac_element_label = QLabel("")
        self.zodiac_modality_label = QLabel("")
        self.zodiac_ruler_label = QLabel("")

        self.zodiac_description = QTextEdit()
        self.zodiac_description.setReadOnly(True)

        details_layout.addWidget(self.zodiac_name_label)
        details_layout.addWidget(self.zodiac_element_label)
        details_layout.addWidget(self.zodiac_modality_label)
        details_layout.addWidget(self.zodiac_ruler_label)
        details_layout.addWidget(self.zodiac_description)

        splitter.addWidget(details_group)
        splitter.setStretchFactor(0, 3)
        splitter.setStretchFactor(1, 2)

        layout.addWidget(splitter)

        self.tabs.addTab(tab, "Zodiac Signs")

        # Connect interactions.
        self.zodiac_search.textChanged.connect(
            self.filter_zodiac_signs
        )

        self.zodiac_table.itemSelectionChanged.connect(
            self.display_selected_zodiac
        )

    def setup_planets_tab(self):
        """Create the traditional planets reference tab."""

        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setSpacing(10)

        # Search field.
        self.planet_search = QLineEdit()
        self.planet_search.setPlaceholderText(
            "Search planets by name, Greek association, or rulership..."
        )
        self.planet_search.setClearButtonEnabled(True)

        layout.addWidget(self.planet_search)

        splitter = QSplitter(Qt.Orientation.Vertical)

        # Planet reference table.
        self.planet_table = QTableWidget()
        self.planet_table.setColumnCount(4)
        self.planet_table.setHorizontalHeaderLabels(
            [
                "Symbol",
                "Planet",
                "Greek Association",
                "Rulerships",
            ]
        )

        self.configure_table(self.planet_table)
        splitter.addWidget(self.planet_table)

        # Planet detail viewer.
        details_group = QGroupBox(
            "Traditional Planet Information"
        )
        details_layout = QVBoxLayout(details_group)

        self.planet_name_label = QLabel(
            "Select a traditional planet."
        )
        self.planet_name_label.setObjectName(
            "astrologyDetailTitle"
        )

        self.planet_greek_label = QLabel("")
        self.planet_rulership_label = QLabel("")

        self.planet_description = QTextEdit()
        self.planet_description.setReadOnly(True)

        details_layout.addWidget(self.planet_name_label)
        details_layout.addWidget(self.planet_greek_label)
        details_layout.addWidget(self.planet_rulership_label)
        details_layout.addWidget(self.planet_description)

        splitter.addWidget(details_group)
        splitter.setStretchFactor(0, 3)
        splitter.setStretchFactor(1, 2)

        layout.addWidget(splitter)

        self.tabs.addTab(tab, "Traditional Planets")

        # Connect interactions.
        self.planet_search.textChanged.connect(
            self.filter_planets
        )

        self.planet_table.itemSelectionChanged.connect(
            self.display_selected_planet
        )

    def setup_explorer_tab(self):
        """Create the interactive Zodiac Explorer tab."""

        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setSpacing(12)

        introduction = QLabel(
            "Select a zodiac sign or enter a birth month and day "
            "to explore its traditional astrological associations."
        )
        introduction.setWordWrap(True)
        layout.addWidget(introduction)

        # Select a sign directly.
        sign_row = QHBoxLayout()
        sign_row.addWidget(QLabel("Zodiac sign:"))

        self.explorer_sign = QComboBox()
        for sign in self.zodiac_signs:
            self.explorer_sign.addItem(
                f"{sign['symbol']} {sign['name']}",
                sign['name'],
            )
        sign_row.addWidget(self.explorer_sign, 1)
        layout.addLayout(sign_row)

        show_button = QPushButton("Show Zodiac Profile")
        show_button.clicked.connect(self.show_selected_profile)
        layout.addWidget(show_button)

        # Alternatively, calculate a sign using a calendar date.
        date_row = QHBoxLayout()
        date_row.addWidget(QLabel("Birth month:"))
        self.birth_month = QSpinBox()
        self.birth_month.setRange(1, 12)
        self.birth_month.setValue(1)
        date_row.addWidget(self.birth_month)

        date_row.addWidget(QLabel("Day:"))
        self.birth_day = QSpinBox()
        self.birth_day.setRange(1, 31)
        self.birth_day.setValue(1)
        date_row.addWidget(self.birth_day)

        date_button = QPushButton("Find Sign by Date")
        date_button.clicked.connect(self.show_date_profile)
        date_row.addWidget(date_button)
        layout.addLayout(date_row)

        # Display the selected sign's profile.
        profile_group = QGroupBox("Your Zodiac Reference Profile")
        profile_layout = QVBoxLayout(profile_group)

        self.explorer_title = QLabel("Select a sign to begin.")
        self.explorer_title.setObjectName("astrologyDetailTitle")
        profile_layout.addWidget(self.explorer_title)

        self.explorer_details = QTextEdit()
        self.explorer_details.setReadOnly(True)
        profile_layout.addWidget(self.explorer_details)

        layout.addWidget(profile_group, 1)

        disclaimer = QLabel(
            "These descriptions reflect historical astrological "
            "traditions, not scientifically established personality "
            "traits or predictions. Date boundaries are approximate."
        )
        disclaimer.setWordWrap(True)
        layout.addWidget(disclaimer)

        self.tabs.addTab(tab, "Zodiac Explorer")

        # Display an initial profile when the tab is opened.
        self.show_selected_profile()

    def show_selected_profile(self):
        """Display the profile for the selected zodiac sign."""
        name = self.explorer_sign.currentData()
        profile = ZodiacService.get_zodiac_profile(name)
        self.display_explorer_profile(profile)

    def show_date_profile(self):
        """Find and display a sign from the entered month and day."""
        month = self.birth_month.value()
        day = self.birth_day.value()

        try:
            profile = ZodiacService.get_profile_by_date(month, day)
        except ValueError:
            self.explorer_title.setText("Invalid date")
            self.explorer_details.setPlainText(
                "Enter a valid calendar month and day."
            )
            return

        if profile is not None:
            index = self.explorer_sign.findData(profile["name"])
            if index >= 0:
                self.explorer_sign.setCurrentIndex(index)

        self.display_explorer_profile(profile)

    def display_explorer_profile(self, profile):
        """Render a traditional astrology profile safely."""
        if profile is None:
            self.explorer_title.setText("Profile unavailable")
            self.explorer_details.setPlainText(
                "No zodiac information was found for that selection."
            )
            return

        self.explorer_title.setText(
            f"{profile['symbol']} {profile['name']} "
            f"({profile['greek_name']})"
        )

        self.explorer_details.setPlainText(
            f"Element: {profile['element']}\n"
            f"Modality: {profile['modality']}\n"
            f"Traditional ruler: {profile['ruling_planet']}\n\n"
            f"Historical reference:\n{profile['description']}\n\n"
            f"Traditional interpretation:\n"
            f"{profile.get('interpretation', '')}\n\n"
            f"Planetary association:\n"
            f"{profile.get('planet_description', '')}"
        )

    def configure_table(self, table):
        """Configure a read-only reference table."""

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

        # Resize columns according to their contents.
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

    def load_zodiac_signs(self, signs):
        """Populate the zodiac reference table."""

        self.zodiac_table.blockSignals(True)

        self.zodiac_table.setRowCount(len(signs))

        for row, sign in enumerate(signs):
            values = [
                sign["symbol"],
                sign["name"],
                sign["greek_name"],
                sign["element"],
                sign["modality"],
                sign["ruling_planet"],
            ]

            for column, value in enumerate(values):
                item = QTableWidgetItem(value)

                if column == 0:
                    item.setTextAlignment(
                        Qt.AlignmentFlag.AlignCenter
                    )

                self.zodiac_table.setItem(
                    row, column, item
                )

        self.zodiac_table.blockSignals(False)

        # Clear outdated details after filtering.
        self.zodiac_table.clearSelection()
        self.clear_zodiac_details()

        # Select the first matching sign.
        if signs:
            self.zodiac_table.selectRow(0)

    def load_planets(self, planets):
        """Populate the traditional planet reference table."""

        self.planet_table.blockSignals(True)

        self.planet_table.setRowCount(len(planets))

        for row, planet in enumerate(planets):
            values = [
                planet["symbol"],
                planet["name"],
                planet["greek_name"],
                ", ".join(planet["rulerships"]),
            ]

            for column, value in enumerate(values):
                item = QTableWidgetItem(value)

                if column == 0:
                    item.setTextAlignment(
                        Qt.AlignmentFlag.AlignCenter
                    )

                self.planet_table.setItem(
                    row, column, item
                )

        self.planet_table.blockSignals(False)

        # Clear outdated details after filtering.
        self.planet_table.clearSelection()
        self.clear_planet_details()

        # Select the first matching planet.
        if planets:
            self.planet_table.selectRow(0)

    def filter_zodiac_signs(self, text):
        """Filter zodiac signs using the search field."""

        results = search_zodiac_signs(text)
        self.load_zodiac_signs(results)

    def filter_planets(self, text):
        """Filter traditional planets using the search field."""

        results = search_traditional_planets(text)
        self.load_planets(results)

    def display_selected_zodiac(self):
        """Display information about the selected zodiac sign."""

        row = self.zodiac_table.currentRow()

        if row < 0:
            self.clear_zodiac_details()
            return

        # Retrieve the sign name from the table.
        item = self.zodiac_table.item(row, 1)

        if item is None:
            self.clear_zodiac_details()
            return

        sign_name = item.text()

        sign = next(
            (
                record
                for record in self.zodiac_signs
                if record["name"] == sign_name
            ),
            None
        )

        if sign is None:
            self.clear_zodiac_details()
            return

        self.zodiac_name_label.setText(
            f"{sign['symbol']} {sign['name']} "
            f"({sign['greek_name']})"
        )

        self.zodiac_element_label.setText(
            f"Element: {sign['element']}"
        )

        self.zodiac_modality_label.setText(
            f"Modality: {sign['modality']}"
        )

        self.zodiac_ruler_label.setText(
            f"Traditional Ruler: {sign['ruling_planet']}"
        )

        self.zodiac_description.setPlainText(
            sign["description"]
        )

    def display_selected_planet(self):
        """Display information about the selected planet."""

        row = self.planet_table.currentRow()

        if row < 0:
            self.clear_planet_details()
            return

        # Retrieve the planet name from the table.
        item = self.planet_table.item(row, 1)

        if item is None:
            self.clear_planet_details()
            return

        planet_name = item.text()

        planet = next(
            (
                record
                for record in self.planets
                if record["name"] == planet_name
            ),
            None
        )

        if planet is None:
            self.clear_planet_details()
            return

        self.planet_name_label.setText(
            f"{planet['symbol']} {planet['name']}"
        )

        self.planet_greek_label.setText(
            f"Greek Association: {planet['greek_name']}"
        )

        self.planet_rulership_label.setText(
            "Traditional Rulerships: "
            + ", ".join(planet["rulerships"])
        )

        self.planet_description.setPlainText(
            planet["description"]
        )

    def clear_zodiac_details(self):
        """Clear the zodiac sign detail viewer."""

        self.zodiac_name_label.setText(
            "Select a zodiac sign."
        )

        self.zodiac_element_label.clear()
        self.zodiac_modality_label.clear()
        self.zodiac_ruler_label.clear()
        self.zodiac_description.clear()

    def clear_planet_details(self):
        """Clear the planet detail viewer."""

        self.planet_name_label.setText(
            "Select a traditional planet."
        )

        self.planet_greek_label.clear()
        self.planet_rulership_label.clear()
        self.planet_description.clear()
