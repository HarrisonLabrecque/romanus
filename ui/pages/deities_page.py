from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class DeitiesPage(QWidget):
    """Page for the Greco-Roman Deities."""

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Greek Astrology")
        description = QLabel(
            "Greco-Roman deities information will be displayed here."
        )

        layout.addWidget(title)
        layout.addWidget(description)
        layout.addStretch()