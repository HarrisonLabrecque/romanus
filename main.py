
"""
Romanus - Application Entry Point

Initializes the PySide6 application, loads the
global stylesheet, and launches the main window.

Supports both development and PyInstaller builds.

Version: 1.0.0
"""

import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow


# --------------------------------------------------
# Application Information
# --------------------------------------------------

APP_NAME = "Romanus"
APP_VERSION = "1.0.0"
ORGANIZATION_NAME = "Romanus"


# --------------------------------------------------
# Resource Management
# --------------------------------------------------

def get_resource_path(relative_path):
    """
    Resolve the absolute path to an application resource.

    Supports normal Python execution and PyInstaller
    one-folder and one-file builds.

    Args:
        relative_path (str): Path relative to the
                             application resource root.

    Returns:
        Path: Absolute resource path.
    """

    if hasattr(sys, "_MEIPASS"):
        base_path = Path(sys._MEIPASS)
    else:
        base_path = Path(__file__).resolve().parent

    return base_path / relative_path


# --------------------------------------------------
# Stylesheet Management
# --------------------------------------------------

def load_stylesheet(app):
    """
    Load the Romanus global QSS stylesheet.

    Args:
        app (QApplication): Active Qt application.
    """

    stylesheet_path = get_resource_path(
        "resources/styles/main.qss"
    )

    if not stylesheet_path.is_file():
        print(
            f"Warning: Stylesheet not found: {stylesheet_path}",
            file=sys.stderr,
        )
        return

    try:
        stylesheet = stylesheet_path.read_text(
            encoding="utf-8"
        )

        app.setStyleSheet(stylesheet)

    except OSError as error:
        print(
            f"Error loading stylesheet: {error}",
            file=sys.stderr,
        )


# --------------------------------------------------
# Application Startup
# --------------------------------------------------

def main():
    """Initialize and launch Romanus."""

    app = QApplication(sys.argv)

    # Configure application metadata.
    app.setApplicationName(APP_NAME)
    app.setApplicationVersion(APP_VERSION)
    app.setOrganizationName(ORGANIZATION_NAME)

    # Apply the global application stylesheet.
    load_stylesheet(app)

    # Create and display the main application window.
    window = MainWindow()
    window.show()

    # Start the Qt event loop.
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
