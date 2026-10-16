
"""
Romanus - Application Entry Point

Initializes the PySide6 application, loads the global
stylesheet, and launches the main window.

Version: 0.8.0
"""

import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow


def load_stylesheet(app: QApplication):
    """Load the application's global QSS stylesheet."""

    # Resolve the stylesheet relative to this script.
    project_root = Path(__file__).resolve().parent
    stylesheet_path = (
        project_root / "resources" / "styles" / "main.qss"
    )

    # Load the stylesheet if it exists.
    if stylesheet_path.is_file():
        stylesheet = stylesheet_path.read_text(
            encoding="utf-8"
        )

        app.setStyleSheet(stylesheet)
    else:
        print(
            f"Warning: Stylesheet not found: {stylesheet_path}"
        )


def main():
    """Start the Romanus desktop application."""

    app = QApplication(sys.argv)

    # Application metadata.
    app.setApplicationName("Romanus")
    app.setApplicationVersion("0.8.0")

    # Load global application styling.
    load_stylesheet(app)

    # Create and display the main window.
    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
