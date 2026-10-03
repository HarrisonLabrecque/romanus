from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class LatinPage(QWidget):
    """Page for the Latin alphabet."""

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Latin Alphabet")
        description = QLabel(
            "Latin alphabet information will be displayed here."
        )

        layout.addWidget(title)
        layout.addWidget(description)
        layout.addStretch()