# Changelog

All notable changes to **Romanus**, an offline-first Greco-Roman reference application built with Python and PySide6, are documented here.

The project uses version numbers in the form MAJOR.MINOR.PATCH. Dates are omitted where release dates have not been confirmed.


## [0.8.0] - Unreleased

### Added
- Global QSS styling system.
- Accessible names and descriptions for navigation buttons.
- Navigation tooltips and keyboard focus support.
- Ctrl+H shortcut for Home navigation.
- Alt+Left shortcut for returning to Home.
- Automated tests for accessibility and stylesheet configuration.

### Changed
- Improved sidebar layout and navigation appearance.
- Added active-page highlighting.
- Improved focus indicators for interactive controls.
- Standardized visual styling across the application.

### Testing
- 138 automated tests passing.
- Added GUI navigation and accessibility regression coverage.
- Final manual GUI verification pending.



## [Unreleased]

### Planned
- v0.8.0: Interface and accessibility improvements.
- v0.9.0: Packaging and distribution preparation.
- v1.0.0: Initial stable release.

## [0.7.0] — Interactive Zodiac Explorer and Pytest

### Added
- Third **Zodiac Explorer** tab in the Greek Astrology page.
- Direct selection of all twelve zodiac signs.
- Month/day lookup using approximate conventional tropical sign boundaries.
- Historical reference profiles with symbols, Greek names, elements, modalities, traditional rulers, interpretations, and planetary descriptions.
- `services/zodiac_service.py` for calendar validation and profile assembly.
- Pytest configuration and `tests/test_zodiac_service.py` test suite covering sign boundaries, invalid dates, leap day, lookups, and profiles (pending local execution).

### Changed
- Expanded the existing Astrology page while retaining both reference tabs.
- Updated SRS and SDD for Zodiac Explorer and automated service testing.

### Notes
- Interpretations describe historical traditions, not scientifically established traits or predictions.
- The feature works offline.
- Test results and release verification are not yet recorded.

## [0.6.0] — Unified Search

### Added
- Unified search across Latin, Greek, Roman numerals, deities, and astrology.
- Search service, Search page, category filtering, result details, and reference-page navigation.
- Sidebar Search entry, Ctrl+F shortcut, and Home dashboard search access.

### Fixed
- Handled optional or missing Roman numeral record fields when building search results.

## [0.5.0] — Greek and Hellenistic Astrology

### Added
- Twelve-sign zodiac dataset and seven traditional planetary records.
- Searchable zodiac and planetary reference tables and detail views.
- Home dashboard statistics and reference navigation.

## [0.4.0] — Greco-Roman Deities

### Added
- Deity reference dataset, searchable browser, and detailed descriptions.

## [0.3.0] — Roman Numerals

### Added
- Roman numeral reference data and two-way Arabic/Roman conversion service.
- Input validation and interactive conversion interface.

## [0.2.0] — Alphabet References

### Added
- Latin and Greek alphabet reference data and browsing interfaces.
- Unicode Greek character support.

### Changed
- Latin alphabet reference subsequently expanded to the modern 26-letter set.

## [0.1.0] — Application Foundation

### Added
- PySide6 main window, Home page, sidebar navigation, and six initial reference pages.
- Modular project structure and initial technical documentation.
