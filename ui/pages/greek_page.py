from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class GreekPage(QWidget):
    """Page for the Greek Alphabet."""

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Greek Astrology")
        description = QLabel(
            "Greek alphabet information will be displayed here."
        )

        layout.addWidget(title)
        layout.addWidget(description)
        layout.addStretch()