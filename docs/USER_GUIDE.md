# Romanus — User Guide

**Version:** 1.0.0  
**Platform:** Windows  
**Application:** Greco-Roman Reference  
**Framework:** Python / PySide6

---

## 1. Introduction

Romanus is an educational desktop application designed to help users explore Greco-Roman languages, Roman numerals, mythology, and traditional astrology.

The application provides an organized interface for browsing reference information, converting Roman numerals, exploring zodiac profiles, and searching across available reference datasets.

Romanus is intended for students, educators, history enthusiasts, and anyone interested in classical studies.

## 2. System Requirements

### Supported Platform

- Windows desktop operating system
- Keyboard and mouse
- Sufficient storage for the application and its bundled dependencies

The packaged Windows application does not require a separate Python installation.

## 3. Installation

### 3.1 Download Romanus

1. Open the Romanus GitHub repository.
2. Navigate to **Releases**.
3. Select the latest stable release.
4. Download the Windows distribution archive.
5. Extract the archive to a folder of your choice.

*The GitHub download will become available once the stable release is published.*

### 3.2 Launch the Application

Open the extracted application directory:

```text
Romanus/
├── Romanus.exe
└── _internal/
```

Double-click `Romanus.exe` to launch the application.

**Important:** Do not move `Romanus.exe` away from its accompanying `_internal` directory. Both are required for the application to operate correctly.

### 3.3 Closing Romanus

Close the application using the standard Windows close button in the upper-right corner.

## 4. Application Interface

Romanus uses a sidebar navigation system and a central content area.

The sidebar provides access to seven pages:

| Page | Description |
|---|---|
| Home | Main application dashboard |
| Search | Unified reference search |
| Latin Alphabet | Latin alphabet reference |
| Greek Alphabet | Greek alphabet reference |
| Roman Numerals | Numeral reference and converter |
| Greek Astrology | Traditional astrology and Zodiac Explorer |
| Greco-Roman Deities | Classical deity reference |

The currently selected page is highlighted in the sidebar.

## 5. Home Dashboard

The Home dashboard provides the starting point for navigating Romanus.

To use it:

1. Launch Romanus.
2. The Home dashboard appears automatically.
3. Review the available reference categories.
4. Select a category to open its corresponding page.

You can return to Home at any time using the sidebar or `Ctrl+H`.

## 6. Latin Alphabet Reference

The Latin Alphabet page provides information about the Latin writing system.

### Instructions

1. Select **Latin Alphabet** from the sidebar.
2. Browse the alphabet reference.
3. Review the available letter information.

The application includes a modern 26-letter Latin alphabet reference.

## 7. Greek Alphabet Reference

The Greek Alphabet page provides a reference for Greek letters.

### Instructions

1. Select **Greek Alphabet**.
2. Browse the Greek alphabet entries.
3. Review the displayed letter information.

This section can be used alongside the Latin Alphabet page for educational comparison.

## 8. Roman Numeral Converter

The Roman Numerals page provides reference information and a bidirectional numeral converter.

### 8.1 Arabic to Roman Numerals

1. Select **Roman Numerals**.
2. Locate the Arabic-to-Roman conversion controls.
3. Enter an integer supported by the converter.
4. Activate the conversion control.
5. Review the resulting Roman numeral.

Example:

| Arabic numeral | Roman numeral |
|---|---|
| 4 | IV |
| 9 | IX |
| 42 | XLII |
| 100 | C |
| 2026 | MMXXVI |

### 8.2 Roman to Arabic Numerals

1. Locate the Roman-to-Arabic conversion controls.
2. Enter a valid Roman numeral.
3. Activate the conversion control.
4. Review the corresponding integer.

Example: `XLII` converts to `42`.

Invalid or unsupported inputs should be corrected according to the application's displayed feedback.

## 9. Greek Astrology

The Greek Astrology page provides traditional zodiac and planetary reference information.

### 9.1 Zodiac Reference

1. Select **Greek Astrology**.
2. Open the zodiac reference section.
3. Browse the available zodiac signs.
4. Review their traditional associations.

### 9.2 Planetary Reference

1. Open the planetary reference section.
2. Browse the traditional planets.
3. Review the available descriptions and associations.

The astrology content is presented as historical and educational reference material.

## 10. Zodiac Explorer

The Zodiac Explorer provides interactive access to zodiac profiles.

### 10.1 Search by Zodiac Sign

1. Open **Greek Astrology**.
2. Select the **Zodiac Explorer** tab.
3. Choose a zodiac sign.
4. View the corresponding profile.

The profile includes available traditional interpretations and planetary associations.

### 10.2 Search by Calendar Date

1. Open Zodiac Explorer.
2. Locate the month and day input controls.
3. Enter a valid calendar date.
4. Activate the lookup control.
5. Review the resulting zodiac profile.

The date lookup uses the application's predefined zodiac date ranges.

## 11. Greco-Roman Deities

The Deities page provides reference information about classical gods and goddesses.

### Instructions

1. Select **Greco-Roman Deities**.
2. Browse the available deity entries.
3. Review their descriptions and associations.

This section is intended as an educational mythology reference.

## 12. Unified Search

Romanus includes a unified search feature for finding information across its reference datasets.

### Instructions

1. Select **Search** from the sidebar, or press `Ctrl+F`.
2. Enter a search term.
3. Use the search controls to retrieve matching entries.
4. Review the displayed results.
5. Select a supported result to navigate to its reference page.

Search results depend on the reference information included in the application.

## 13. Keyboard Shortcuts

Romanus supports the following keyboard shortcuts:

| Shortcut | Function |
|---|---|
| `Ctrl+F` | Open Search |
| `Ctrl+H` | Return to Home |
| `Alt+Left` | Return to Home |
| `Tab` | Move keyboard focus |
| `Shift+Tab` | Move focus backward |
| `Enter` or `Space` | Activate a focused navigation button |

**Note:** `Alt+Left` returns to Home; it does not currently navigate through previously visited pages.

## 14. Accessibility Features

Romanus includes several interface accessibility features:

- Keyboard-focusable sidebar navigation
- Accessible names and descriptions for navigation buttons
- Tooltips for navigation controls
- Visible keyboard focus indicators
- Active-page highlighting
- Consistent interface styling

These features help users navigate the application using different input methods.

## 15. Troubleshooting

### Romanus Does Not Launch

Verify that the entire distribution archive was extracted and that `Romanus.exe` remains alongside the `_internal` directory.

If the application still fails, try extracting a fresh copy of the distribution.

### Interface Styling Is Missing

Ensure the packaged application contains all its bundled resources. Avoid deleting or moving files from the distribution directory.

### Search Returns No Results

Try a different keyword or a broader search term. The search feature operates on the reference information available in Romanus.

### Roman Numeral Conversion Fails

Verify that the input uses a supported integer or valid Roman numeral notation.

### Keyboard Shortcuts Do Not Work

Ensure the Romanus window is active and has keyboard focus.

## 16. Running Automated Tests

This section is intended for users working with the source code.

Install the project's dependencies and run:

```powershell
python -m pytest -v
```

At the time of v1.0.0 release preparation, Romanus completed **179 automated tests successfully**.

## 17. Updates and Releases

New versions of Romanus may introduce additional reference content, interface improvements, and bug fixes.

Check the project's GitHub repository for release announcements and available updates.

## 18. Additional Documentation

The project includes the following technical documentation:

- `README.md` — Project overview and installation instructions
- `docs/SRS.md` — Software Requirements Specification
- `docs/SDD.md` — Software Design Document
- `docs/CHANGELOG.md` — Development and release history

## 19. License

Refer to the `LICENSE` file in the Romanus repository for the applicable software license.

---

**Romanus v1.0.0 — Greco-Roman Reference Application**

*End of User Guide*