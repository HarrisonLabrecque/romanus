from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class HomePage(QWidget):
    """Home page for the application."""

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Greco-Roman Reference")

        description = QLabel(
            "Explore the languages, numerals, astrology, "
            "and deities of the Greco-Roman world."
        )

        layout.addWidget(title)
        layout.addWidget(description)
        layout.addStretch()