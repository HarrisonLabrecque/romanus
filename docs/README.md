# Romanus

**Version 1.0.0 — Stable Release**

Romanus is an open-source educational desktop application developed in Python using PySide6. It provides an interactive reference for exploring Greco-Roman languages, Roman numerals, mythology, and traditional astrology.

## Features

- **Latin Alphabet:** Explore the Latin alphabet and its reference information.
- **Greek Alphabet:** Browse Greek letters and their corresponding information.
- **Roman Numerals:** Study Roman numeral notation and convert between Roman and Arabic numerals.
- **Greco-Roman Deities:** Explore reference information about classical deities.
- **Traditional Astrology:** Browse zodiac signs and traditional planetary associations.
- **Zodiac Explorer:** Look up zodiac profiles using sign selection or calendar dates.
- **Unified Search:** Search across the application's reference datasets.
- **Accessible Navigation:** Use keyboard shortcuts, tooltips, and keyboard-focusable navigation controls.

## Technology Stack

- Python
- PySide6
- Qt Style Sheets (QSS)
- pytest
- pytest-qt
- PyInstaller

## Installation

### Windows Executable

1. Obtain the Romanus Windows distribution from the project's GitHub Releases page when published.
2. Extract the distribution archive.
3. Open the `Romanus` folder.
4. Double-click `Romanus.exe`.

Keep the executable and its accompanying `_internal` directory together.

A separate Python installation is not required for the packaged application.

### Run from Source

Clone the repository and navigate to the project directory.

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

Launch Romanus:

```powershell
python main.py
```

## Keyboard Shortcuts

| Shortcut | Action |
|---|---|
| Ctrl+F | Open Search |
| Ctrl+H | Open Home |
| Alt+Left | Return to Home |

## Testing

Romanus uses pytest and pytest-qt for automated testing.

Run the complete test suite:

```powershell
python -m pytest -v
```

**Stable release verification:** 179 automated tests passed, and final manual release checks were completed.

## Windows Packaging

Romanus uses PyInstaller to generate its Windows distribution.

Build the application using:

```powershell
python -m PyInstaller --clean --noconfirm Romanus.spec
```

The packaged application is generated inside `dist/Romanus/`.

## Project Documentation

Additional documentation is available in the `docs/` directory:

- `SRS.md` — Software Requirements Specification
- `SDD.md` — Software Design Document
- `CHANGELOG.md` — Version history

- [User Guide](docs/USER_GUIDE.md) — Installation, features, and usage instructions.

## Release History

| Version | Milestone |
|---|---|
| v0.1.0–v0.5.0 | Core reference features |
| v0.6.0 | Unified search |
| v0.7.0 | Zodiac Explorer |
| v0.8.0 | UI and accessibility improvements |
| v0.9.0 | Windows packaging |
| v1.0.0 | First stable release |

## Future Development

Future improvements may include additional reference content, interface refinements, and expanded educational functionality.

## License

See the repository's `LICENSE` file for the applicable license terms.