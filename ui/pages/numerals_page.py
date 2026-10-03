from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class NumeralsPage(QWidget):
    """Page for the Roman Numerals."""

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Greek Astrology")
        description = QLabel(
            "Roman numerals information will be displayed here."
        )

        layout.addWidget(title)
        layout.addWidget(description)
        layout.addStretch()