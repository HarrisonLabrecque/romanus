
# -*- mode: python ; coding: utf-8 -*-

"""
Romanus - PyInstaller Build Configuration

Packages the Romanus desktop application into
a single Windows executable containing Python,
PySide6 dependencies, application modules,
and stylesheet resources.

Version: 1.0.0
"""

from pathlib import Path

from PyInstaller.utils.hooks import collect_submodules


# --------------------------------------------------
# Project Configuration
# --------------------------------------------------

PROJECT_ROOT = Path(SPECPATH).resolve()

APP_NAME = "Romanus"

ENTRY_POINT = PROJECT_ROOT / "main.py"

STYLESHEET_PATH = (
    PROJECT_ROOT
    / "resources"
    / "styles"
    / "main.qss"
)


# --------------------------------------------------
# Application Resources
# --------------------------------------------------

# Bundle the stylesheet in the relative directory
# expected by get_resource_path() in main.py.

datas = [
    (
        str(STYLESHEET_PATH),
        "resources/styles",
    ),
]


# --------------------------------------------------
# Hidden Imports
# --------------------------------------------------

# Collect application modules to ensure they are
# included in the standalone executable.

hiddenimports = (
    collect_submodules("ui")
    + collect_submodules("data")
    + collect_submodules("services")
)


# --------------------------------------------------
# Analysis
# --------------------------------------------------

a = Analysis(
    [str(ENTRY_POINT)],
    pathex=[str(PROJECT_ROOT)],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        "pytest",
        "pytestqt",
    ],
    noarchive=False,
)


# --------------------------------------------------
# Python Module Archive
# --------------------------------------------------

pyz = PYZ(a.pure)


# --------------------------------------------------
# Single Executable
# --------------------------------------------------

# Include all binaries and application resources
# directly in the executable.

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name=APP_NAME,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    disable_windowed_traceback=False,
)
