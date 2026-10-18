
"""
Romanus - Application Entry Point

Initializes the PySide6 application and loads
resources for development and packaged builds.

Version: 0.9.0
"""

import sys
from pathlib import Path

from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow


# --------------------------------------------------
# Resource Management
# --------------------------------------------------

def get_resource_path(relative_path):
    """
    Return the absolute path to an application resource.

    Supports:
    - Standard Python development environment
    - PyInstaller one-folder builds
    - PyInstaller one-file builds

    Args:
        relative_path (str): Resource path relative
                             to the project root.

    Returns:
        Path: Absolute resource path.
    """

    if hasattr(sys, "_MEIPASS"):
        # PyInstaller extracts bundled resources here.
        base_path = Path(sys._MEIPASS)
    else:
        # Normal Python execution.
        base_path = Path(__file__).resolve().parent

    return base_path / relative_path


# --------------------------------------------------
# Stylesheet Management
# --------------------------------------------------

def load_stylesheet(app):
    """
    Load the application's global QSS stylesheet.

    Args:
        app (QApplication): Application instance.
    """

    stylesheet_path = get_resource_path(
        "resources/styles/main.qss"
    )

    if not stylesheet_path.is_file():
        print(
            f"Warning: Stylesheet not found: "
            f"{stylesheet_path}"
        )
        return

    try:
        stylesheet = stylesheet_path.read_text(
            encoding="utf-8"
        )

        app.setStyleSheet(stylesheet)

    except OSError as error:
        print(
            f"Error loading stylesheet: {error}"
        )


# --------------------------------------------------
# Application Startup
# --------------------------------------------------

def main():
    """Start the Romanus desktop application."""

    app = QApplication(sys.argv)

    # Application metadata.
    app.setApplicationName("Romanus")
    app.setApplicationVersion("0.9.0")
    app.setOrganizationName("Romanus")

    # Apply the global stylesheet.
    load_stylesheet(app)

    # Initialize the main application window.
    window = MainWindow()
    window.show()

    # Start the Qt event loop.
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
