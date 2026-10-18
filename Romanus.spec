
# -*- mode: python ; coding: utf-8 -*-

"""
Romanus - PyInstaller Build Configuration

Packages the Romanus desktop application with
its Python modules, PySide6 dependencies, and
stylesheet resources.

Version: 0.9.0
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

# Bundle the stylesheet into the same relative
# directory expected by get_resource_path().
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
# available inside the packaged executable.

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
# Executable
# --------------------------------------------------

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name=APP_NAME,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    disable_windowed_traceback=False,
)


# --------------------------------------------------
# Distribution Folder
# --------------------------------------------------

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    name=APP_NAME,
)
