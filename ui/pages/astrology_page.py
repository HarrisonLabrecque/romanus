from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class AstrologyPage(QWidget):
    """Page for the Greek Astrology."""

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Greek Astrology")
        description = QLabel(
            "Greek astrology information will be displayed here."
        )

        layout.addWidget(title)
        layout.addWidget(description)
        layout.addStretch()