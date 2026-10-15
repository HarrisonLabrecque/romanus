**# Software Design Document (SDD)**



**## Greco-Roman Reference Application**



****Project Type:**** Desktop Reference Application  

****Programming Language:**** Python  

****GUI Framework:**** PySide6 / Qt 6  

****Document Version:**** 0.1  

****Application Version:**** Prototype v0.1  

****Status:**** Draft  



**---**



**# 1. Introduction**



**## 1.1 Purpose**



This Software Design Document defines the architecture, components, modules, data organization, user-interface structure, and implementation strategy for the Greco-Roman Reference Application.



The Software Requirements Specification (SRS) defines what the application is expected to accomplish. This document describes how those requirements will be implemented.



The SDD will serve as a technical reference throughout development and should be updated as the architecture evolves.



**## 1.2 Scope**



The Greco-Roman Reference Application is a Python desktop program developed using PySide6.



The application will provide reference information and interactive tools concerning:



- Latin alphabet

- Greek alphabet

- Roman numerals

- Greek and Hellenistic astrology

- Greek and Roman deities



The software is intended to operate primarily offline.



The architecture will emphasize:



- Modularity

- Maintainability

- Separation of concerns

- Extensibility

- Testability

- Clear organization of reference data



**---**



**# 2. Design Goals**



The primary design goals are:



**### DG-001 — Modular Architecture**



Features shall be divided into logical Python modules and packages rather than implemented within a single source file.



**### DG-002 — Separation of Concerns**



User-interface code, reference data, and application logic should remain separate whenever practical.



**### DG-003 — Extensibility**



New reference categories and tools should be addable without significant modification to unrelated features.



**### DG-004 — Maintainability**



Classes and modules should have clearly defined responsibilities.



**### DG-005 — Offline Operation**



Core application functionality should not depend upon an internet connection.



**### DG-006 — Testability**



Business logic, such as Roman numeral conversion, should be independent enough from the graphical interface to permit unit testing.



**### DG-007 — Unicode Support**



The architecture shall support Unicode content required for Greek characters and related historical terminology.



**---**



**# 3. System Architecture**



**## 3.1 Architectural Style**



The application will use a layered, modular architecture.



The primary layers are:



```text

┌─────────────────────────────┐

│       Application Layer     │

│          main.py            │

├─────────────────────────────┤

│      Presentation Layer     │

│       ui / PySide6          │

├─────────────────────────────┤

│    Logic / Service Layer    │

│      services / core        │

├─────────────────────────────┤

│         Data Layer          │

│           data              │

├─────────────────────────────┤

│       Resource Layer        │

│         resources           │

└─────────────────────────────┘

```



Not every layer must be fully implemented during Prototype v0.1.



Layers should be introduced when the application requires them rather than adding unnecessary abstraction prematurely.



**## 3.2 High-Level Data Flow**



Typical application interaction will follow this pattern:



```text

User

  │

  ▼

PySide6 Widget

  │

  ▼

Page / UI Component

  │

  ├──────────► Reference Data

  │

  └──────────► Service / Application Logic

                    │

                    ▼

                  Result

                    │

                    ▼

               UI Updated

```



For example, Roman numeral conversion should follow:



```text

User enters 24

       │

       ▼

NumeralsPage

       │

       ▼

RomanNumeralService

       │

       ▼

     XXIV

       │

       ▼

NumeralsPage displays XXIV

```



The conversion algorithm should not be implemented directly inside a button click handler.



**---**



**# 4. Project Directory Design**



The initial project architecture is:



```text

greco_roman_gui/

│

├── main.py

├── requirements.txt

├── README.md

├── .gitignore

│

├── docs/

│   ├── SRS.md

│   └── SDD.md

│

├── ui/

│   ├── \_\_init\_\_.py

│   ├── main_window.py

│   │

│   └── pages/

│       ├── \_\_init\_\_.py

│       ├── home_page.py

│       ├── latin_page.py

│       ├── greek_page.py

│       ├── numerals_page.py

│       ├── astrology_page.py

│       └── deities_page.py

│

├── data/

│   ├── \_\_init\_\_.py

│   ├── latin_alphabet.py

│   ├── greek_alphabet.py

│   ├── roman_numerals.py

│   ├── astrology.py

│   └── deities.py

│

├── services/

│   ├── \_\_init\_\_.py

│   └── roman_numeral_service.py

│

├── resources/

│   ├── icons/

│   ├── images/

│   └── styles/

│

└── tests/

    ├── \_\_init\_\_.py

    └── test_roman_numerals.py

```



Some directories will be introduced in later prototypes as required.



**---**



**# 5. Application Entry Point**



**## 5.1 `main.py`**



`main.py` will serve as the primary application entry point.



Responsibilities:



- Import required Qt classes.

- Create the `QApplication` instance.

- Create the main application window.

- Display the main window.

- Start the Qt event loop.

- Exit cleanly when the application terminates.



Conceptual structure:



```python

def main():

    app = QApplication(sys.argv)



    window = MainWindow()

    window.show()



    sys.exit(app.exec())

```



Application feature logic shall not be placed inside `main.py`.



**---**



**# 6. Main Window Design**



**## 6.1 `MainWindow`**



The primary window will inherit from:



```python

QMainWindow

```



`MainWindow` will act as the main application container.



Responsibilities include:



- Window configuration

- Navigation

- Page management

- Main application layout

- Switching between feature pages



**## 6.2 Main Layout**



The primary interface will initially use a two-column layout:



```text

┌─────────────────────────────────────────────────────┐

│                 Application Window                  │

├──────────────┬──────────────────────────────────────┤

│              │                                      │

│    Sidebar   │                                      │

│              │           Content Area               │

│    Home      │                                      │

│    Latin     │                                      │

│    Greek     │                                      │

│    Numerals  │                                      │

│    Astrology │                                      │

│    Deities   │                                      │

│              │                                      │

└──────────────┴──────────────────────────────────────┘

```



**## 6.3 Page Management**



Page navigation will use:



```python

QStackedWidget

```



Each major feature will have its own QWidget-based page.



Only one page will normally be displayed at a time.



The initial page order is:



```text

Index 0 → HomePage

Index 1 → LatinPage

Index 2 → GreekPage

Index 3 → NumeralsPage

Index 4 → AstrologyPage

Index 5 → DeitiesPage

```



Page switching should preferably reference widget instances instead of relying extensively on hard-coded numeric indexes.



**---**



**# 7. Page Design**



**## 7.1 Base Page Strategy**



Each major feature will be implemented as an independent QWidget-derived class.



Example:



```python

class LatinPage(QWidget):

    ...

```



Pages shall be responsible primarily for:



- Presenting information

- Collecting user input

- Displaying results

- Connecting UI events to appropriate application logic



Pages should not contain large static datasets or complex algorithms.



**---**



**# 8. Home Page**



**## 8.1 `HomePage`**



Purpose:



Provide the initial landing page for the application.



Responsibilities:



- Display application name.

- Provide a short introduction.

- Explain the major available reference categories.

- Potentially provide quick-access controls in future releases.



The home page should remain relatively lightweight.



**---**



**# 9. Latin Alphabet Module**



**## 9.1 `LatinPage`**



Purpose:



Display Latin alphabet reference information.



The interface may eventually use:



- `QTableWidget`

- `QListWidget`

- Custom reusable widgets



Possible information fields include:



```text

Letter

Name

Classical pronunciation

Modern usage notes

Historical notes

```



Not every field is required during early prototypes.



**## 9.2 Latin Data**



Latin alphabet data shall be stored outside the UI module.



Example conceptual representation:



```python

LATIN_ALPHABET = [

    {

        "uppercase": "A",

        "lowercase": "a",

        "name": "A"

    }

]

```



The final data structure may change as requirements develop.



**---**



**# 10. Greek Alphabet Module**



**## 10.1 `GreekPage`**



Purpose:



Display Greek alphabet reference information.



Possible fields include:



```text

Uppercase

Lowercase

Name

Transliteration

Pronunciation

```



Example:



```text

Α    α    Alpha    a

Β    β    Beta     b

Γ    γ    Gamma    g

```



**## 10.2 Unicode**



Greek characters shall be represented using Unicode.



Source files shall use UTF-8 compatible encoding.



The selected GUI fonts must support required Greek characters.



**## 10.3 Greek Data**



Greek alphabet data shall reside in:



```text

data/greek_alphabet.py

```



The UI will read the data and create the appropriate visual representation.



**---**



**# 11. Roman Numeral Module**



The Roman numeral module will contain both reference information and interactive conversion functionality.



**## 11.1 `NumeralsPage`**



Responsibilities:



- Display Roman numeral reference information.

- Accept Arabic-number input.

- Accept Roman-numeral input.

- Display conversion results.

- Display validation errors.



Conceptual interface:



```text

Roman Numerals



Basic Symbols



I       1

V       5

X       10

L       50

C       100

D       500

M       1000





Arabic → Roman



[  24  ] [Convert]



Result: XXIV





Roman → Arabic



[ XXIV ] [Convert]



Result: 24

```



**## 11.2 Conversion Service**



Conversion logic shall be separated from `NumeralsPage`.



Proposed module:



```text

services/roman_numeral_service.py

```



Possible interface:



```python

class RomanNumeralService:



    @staticmethod

    def to_roman(number):

        pass



    @staticmethod

    def from_roman(numeral):

        pass

```



This separation allows the conversion logic to be tested without launching PySide6.



**## 11.3 Validation**



The service shall reject invalid input.



Examples include:



```text

Empty input

Non-numeric Arabic input

Values outside the supported range

Invalid Roman characters

Invalid Roman numeral ordering

Invalid repeated symbols

```



The supported numeric range shall be formally defined before the converter is considered complete.



**---**



**# 12. Astrology Module**



**## 12.1 `AstrologyPage`**



Purpose:



Provide reference information concerning selected ancient Greek and Hellenistic astrological traditions.



Possible categories include:



- Zodiac signs

- Classical planets

- Traditional associations

- Historical terminology

- Mythological associations



**## 12.2 Data Organization**



Astrology information will initially reside in:



```text

data/astrology.py

```



If the dataset becomes sufficiently large, it may later be migrated to structured JSON or a database.



**## 12.3 Content Separation**



Historical astrology shall be distinguished from modern scientific astronomy within descriptions where necessary.



The module is intended primarily as historical and cultural reference material.



**---**



**# 13. Deity Module**



**## 13.1 `DeitiesPage`**



Purpose:



Allow users to browse Greek and Roman deity information.



Potential information fields include:



```text

Name

Culture

Roman or Greek counterpart

Domain

Symbols

Description

Associated myths

```



**## 13.2 Deity Data Model**



A deity entry may conceptually resemble:



```python

{

    "name": "Zeus",

    "culture": "Greek",

    "counterpart": "Jupiter",

    "domains": [

        "sky",

        "thunder"

    ],

    "symbols": [

        "thunderbolt"

    ]

}

```



This is an architectural example rather than the final historical dataset.



**## 13.3 Greek/Roman Relationships**



The data model shall not assume every deity has a simple one-to-one equivalent.



The model should support:



```python

"counterpart": None

```



or potentially multiple associated counterparts if later research requires them.



This prevents the UI architecture from forcing historically complex relationships into an overly simple structure.



**---**



**# 14. Data Layer Design**



**## 14.1 Initial Data Storage**



Early prototypes will use Python data structures stored within modules under:



```text

data/

```



Advantages include:



- Simple implementation

- No database dependency

- Easy version control

- Fast offline access



**## 14.2 Future Data Storage**



As the dataset expands, reference information may be migrated to:



```text

JSON

```



or:



```text

SQLite

```



SQLite should be considered if the application eventually requires:



- Large datasets

- Advanced searches

- Relationships between entries

- Favorites

- User-generated information

- Efficient filtering



Migration should only occur when justified by application complexity.



**---**



**# 15. Resource Management**



Static application resources will reside within:



```text

resources/

```



Potential organization:



```text

resources/

├── icons/

├── images/

└── styles/

```



Resources may eventually include:



- Application icons

- Navigation icons

- Historical illustrations where licensing permits

- Stylesheets

- Decorative interface assets



Copyright and licensing requirements must be considered before third-party visual resources are distributed with the application.



**---**



**# 16. Styling Design**



The initial prototype may rely primarily on standard Qt widgets.



Future versions may introduce Qt Style Sheets.



Example location:



```text

resources/styles/main.qss

```



Styling should remain separate from application logic where practical.



A future stylesheet may define:



```text

Main window appearance

Navigation buttons

Headings

Tables

Input fields

Cards

Error states

```



The visual design should remain consistent throughout the application.



**---**



**# 17. Error Handling**



Expected user errors shall not cause the application to terminate unexpectedly.



UI components should validate user input before requesting operations where practical.



Application logic should raise or return clearly defined errors.



Example:



```python

try:

    result = RomanNumeralService.to_roman(number)

except ValueError:

    # Display user-friendly error.

    ...

```



Technical exception messages should generally not be displayed directly to end users.



**---**



**# 18. Testing Architecture**



Testing code will reside within:



```text

tests/

```



**## 18.1 Unit Tests**



Business logic should receive automated unit tests.



Roman numeral conversion is an early candidate.



Example:



```python

def test_convert_24_to_roman():

    assert RomanNumeralService.to_roman(24) == "XXIV"

```



Tests should cover normal input, boundary conditions, and invalid input.



**## 18.2 UI Testing**



During prototype development, the GUI may initially be tested manually.



Manual checks include:



- Application launches.

- Main window renders.

- Navigation works.

- Correct pages are displayed.

- Unicode characters render.

- Conversion results appear correctly.

- Invalid input produces appropriate feedback.

- Window resizing remains usable.



Automated Qt GUI testing may be introduced later if the project complexity justifies it.



**---**



**# 19. Logging**



A future version may use Python's standard:



```python

logging

```



module.



Logging could capture:



- Application startup

- Unexpected errors

- Data-loading failures

- Important application events



Debugging information should not unnecessarily clutter the graphical interface.



**---**



**# 20. Configuration**



Application configuration may eventually be separated from application logic.



Possible configuration includes:



- Window dimensions

- Theme

- Font settings

- User preferences

- Last opened page



Qt's settings facilities may be considered for user preferences.



**---**



**# 21. Persistence Design**



Prototype v0.1 does not require persistent user data.



If persistence becomes necessary, the preferred options are:



**### QSettings**



Suitable for:



- Window state

- Theme

- User preferences



**### JSON**



Suitable for:



- Simple saved data

- Favorites

- Small configuration datasets



**### SQLite**



Suitable for:



- Larger structured datasets

- Searchable content

- Relationships

- Significant persistent user information



The persistence mechanism should be selected according to the requirements of the feature rather than using one storage technology for every type of data.



**---**



**# 22. Dependency Management**



Third-party dependencies shall be recorded in:



```text

requirements.txt

```



The initial primary dependency is:



```text

PySide6

```



Development should occur within a Python virtual environment.



The virtual environment shall not be committed to Git.



**---**



**# 23. Version Control Design**



Git will be used for source control.



GitHub will be used as the remote repository host.



The primary stable development branch will be:



```text

main

```



Commit messages should describe meaningful changes.



Examples:



```text

Initial Greco-Roman GUI prototype v0.1



Add Latin alphabet reference page



Add Greek alphabet data model



Implement Roman numeral converter



Add Roman numeral unit tests



Update SRS and SDD for v0.3

```



Large unrelated changes should generally not be combined into a single commit.



**---**



**# 24. Packaging and Distribution**



Development versions will initially run using:



```text

python main.py

```



A future release may be packaged into a standalone executable using PyInstaller or another suitable Python packaging solution.



Potential distribution structure:



```text

Source Code

     │

     ▼

Python Application

     │

     ▼

Packaging Tool

     │

     ▼

Desktop Executable

     │

     ▼

Release Package

```



Packaging will be addressed closer to the first stable release.



**---**



**# 25. Security Considerations**



The initial application has a relatively small security surface because core functionality operates locally.



The application should:



- Validate user input.

- Avoid executing user-provided text as Python code.

- Avoid unnecessary network connections.

- Avoid storing sensitive information.

- Keep third-party dependencies updated when practical.



If online functionality is introduced later, additional security requirements shall be documented.



**---**



**# 26. Performance Considerations**



Reference datasets are expected to remain relatively small during initial development.



Data may therefore initially be loaded directly into memory.



Optimization should only be introduced when measurable performance issues exist.



The application should avoid:



- Repeatedly loading identical data.

- Creating unnecessary windows.

- Blocking the Qt UI thread with expensive operations.

- Rebuilding complex widgets unnecessarily.



**---**



**# 27. Accessibility Considerations**



The application should use:



- Readable fonts

- Clear labels

- Logical navigation

- Adequate text size

- Understandable error messages



Controls should use meaningful text rather than relying exclusively on icons.



Additional accessibility improvements may be introduced as the application approaches version 1.0.



**---**



**# 28. Prototype v0.1 Component Design**



Prototype v0.1 consists of:



```text

main.py

   │

   ▼

MainWindow

   │

   ├── HomePage

   ├── LatinPage

   ├── GreekPage

   ├── NumeralsPage

   ├── AstrologyPage

   └── DeitiesPage

```



At this stage:



- Navigation is functional.

- Pages are independent widgets.

- Most feature pages contain placeholder content.

- Reference datasets are not yet fully implemented.

- Conversion services are not yet required.

- Persistent storage is not required.



The primary objective is validating the application architecture and navigation system.



**---**



**# 29. Planned v0.2 Design**



Prototype v0.2 will focus on the alphabet modules.



Expected component relationships:



```text

LatinPage

    │

    ▼

latin_alphabet.py





GreekPage

    │

    ▼

greek_alphabet.py

```



The page classes shall render data supplied by their corresponding data modules.



The same architecture can then be reused for later reference modules.



**---**



**# 30. Planned Roman Numeral Architecture**



Prototype v0.3 is expected to introduce the first significant service component:



```text

                 ┌──────────────────────┐

                 │    NumeralsPage      │

                 └──────────┬───────────┘

                            │

             ┌──────────────┴──────────────┐

             ▼                             ▼

    Roman Numeral Data          RomanNumeralService

                                          │

                                ┌─────────┴─────────┐

                                ▼                   ▼

                           to_roman()          from_roman()

```



Unit tests will communicate directly with `RomanNumeralService` rather than interacting with the GUI.



This pattern should be reused for future features containing substantial application logic.



**---**



**# 31. Design Principles**



Development should follow several general principles.



**### Single Responsibility**



A class or module should have a clear primary purpose.



**### Don't Repeat Yourself**



Shared logic should not be unnecessarily duplicated across multiple pages.



**### Keep UI and Logic Separate**



Complex calculations and validation should not be buried inside Qt event handlers.



**### Build Incrementally**



Architecture should grow alongside actual requirements.



Unnecessary frameworks, databases, and abstraction layers should not be introduced simply because they may potentially be useful later.



**### Favor Readability**



Code clarity is preferred over unnecessarily clever implementations.



**---**



**# 32. Design Decisions**



**## DD-001 — PySide6**



****Decision:**** Use PySide6 for the desktop graphical interface.



****Reason:**** Provides Python bindings for Qt 6 and supports development of modern desktop interfaces.



**## DD-002 — QStackedWidget Navigation**



****Decision:**** Use `QStackedWidget` for primary page navigation.



****Reason:**** Only one major page needs to be visible at a time, and stacked widgets provide a straightforward mechanism for managing this behavior.



**## DD-003 — Separate Data Modules**



****Decision:**** Store static reference information separately from UI classes.



****Reason:**** Improves maintainability and allows information to be reused by other components.



**## DD-004 — Service Layer for Complex Logic**



****Decision:**** Place significant application logic in service or core modules.



****Reason:**** Improves testability and prevents UI classes from becoming responsible for unrelated business logic.



**## DD-005 — Local-First Architecture**



****Decision:**** Core features shall operate using locally available data.



****Reason:**** The application's primary purpose does not require continuous network connectivity.



**## DD-006 — Incremental Persistence**



****Decision:**** No database will be required during the initial prototype.



****Reason:**** Introducing a database before the application requires one would increase complexity without providing a meaningful benefit.



**---**



**# 33. Technical Debt Management**



Temporary implementation decisions made during prototype development should be documented when they are expected to require future changes.



Technical debt may include:



- Placeholder UI layouts

- Temporary hard-coded data

- Missing tests

- Temporary styling

- Incomplete validation

- Simplified data models



Technical debt should be addressed progressively rather than allowing prototype shortcuts to silently become permanent architecture.



**---**



**# 34. Documentation**



The repository should eventually contain:



```text

README.md



docs/

├── SRS.md

├── SDD.md

└── TEST_PLAN.md

```



The README should provide developer and user-facing project information.



The SRS shall describe what the software must do.



The SDD shall describe how the software is designed.



The test plan shall define how requirements and major components will be verified.



**---**



**# 35. Design Review Milestones**



The architecture should be reviewed at major development milestones.



Recommended reviews:



```text

v0.1  → Initial architecture review



v0.3  → Logic and testing architecture review



v0.5  → Data architecture review



v0.8  → Pre-release architecture review



v1.0  → Release design review

```



These reviews should determine whether the existing architecture continues to support the application's requirements without unnecessary complexity.



**---**



**# 36. Definition of Done — Prototype v0.1**



Prototype v0.1 is architecturally complete when:



1. `main.py` successfully launches the application.

2. `MainWindow` controls the primary application interface.

3. Major pages are implemented as separate classes.

4. `QStackedWidget` manages page navigation.

5. Navigation buttons successfully switch between pages.

6. The project uses a logical directory structure.

7. Python virtual-environment files are excluded from Git.

8. The SRS documents the current requirements.

9. The SDD documents the current architecture.

10. The working prototype and documentation are committed to Git.



**---**



**# 37. Document Maintenance**



This SDD is a living technical document.



It shall be updated when significant architectural decisions are made, including:



- Addition of major modules

- Changes to project structure

- Introduction of persistent storage

- Introduction of major services

- Changes to navigation architecture

- Significant data-model changes

- Packaging architecture changes



The SDD version should be incremented when substantial design changes occur.



Git history should provide an additional record of how the application's architecture evolved over time.

---

# Appendix A — Architecture Updates Through v0.7.0

This appendix records the current design beyond the original v0.1 prototype. Earlier sections are retained as the project's design history; this appendix takes precedence where the initial architecture or testing strategy has evolved.

## A.1 Updated component structure

```text
Romanus/
├── main.py
├── data/
│   ├── latin_alphabet.py
│   ├── greek_alphabet.py
│   ├── roman_numerals.py
│   ├── deities.py
│   └── astrology.py
├── services/
│   ├── roman_numeral_service.py
│   ├── search_service.py
│   └── zodiac_service.py
├── ui/
│   ├── main_window.py
│   └── pages/
│       ├── home_page.py
│       ├── latin_page.py
│       ├── greek_page.py
│       ├── numerals_page.py
│       ├── astrology_page.py
│       ├── deities_page.py
│       └── search_page.py
├── tests/
│   ├── __init__.py
│   └── test_zodiac_service.py
└── pytest.ini
```

The tests directory and pytest configuration are the intended v0.7.0 additions; confirm their presence in the repository before declaring the release complete.

## A.2 Unified Search Service (v0.6.0)

`SearchService` in `services/search_service.py` normalizes locally stored reference records for searching. `SearchPage` displays matching entries, filters by category, and offers navigation to reference pages. `MainWindow` exposes the Search page via sidebar navigation and Ctrl+F.

## A.3 Zodiac Explorer Design (v0.7.0)

`AstrologyPage` in `ui/pages/astrology_page.py` retains the searchable **Zodiac Signs** and **Traditional Planets** tabs and adds **Zodiac Explorer**. Its PySide6 controls include `QComboBox`, month/day `QSpinBox` inputs, `QPushButton`, `QLabel`, and read-only `QTextEdit`.

| AstrologyPage method | Responsibility |
|---|---|
| `setup_explorer_tab()` | Construct widgets and connect events |
| `show_selected_profile()` | Retrieve the chosen sign profile |
| `show_date_profile()` | Validate date via service and handle errors |
| `display_explorer_profile(profile)` | Present a profile or unavailable state |

`ZodiacService` in `services/zodiac_service.py` has the following methods:

| Method | Responsibility |
|---|---|
| `get_sign_by_date(month, day)` | Validate date and map to conventional sign |
| `get_sign_by_name(name)` | Delegate case-insensitive sign lookup |
| `get_zodiac_profile(name)` | Combine sign data, interpretation, and planetary description |
| `get_profile_by_date(month, day)` | Combine date lookup with profile generation |

`ZODIAC_DATES` defines approximate tropical sign boundaries. `INTERPRETATIONS` contains symbolic historical associations. The service reads from `data/astrology.py` and is independent of Qt.

### Data flow

```text
User input (sign or month/day)
        |
        v
AstrologyPage (presentation)
        |
        v
ZodiacService (validation / lookup / profile)
        |
        v
data/astrology.py (local sign and planet records)
        |
        v
AstrologyPage (read-only profile display)
```

Invalid calendar dates cause `ValueError` in the service and are caught by `AstrologyPage`, which displays a readable error. Unknown names produce `None`. No network connection or persistent storage is required.

## A.4 Pytest Unit Testing Architecture

`pytest` is the chosen test runner. Service tests are kept in `tests/`, with filenames matching `test_*.py`. `pytest.ini` configures test discovery and output.

`tests/test_zodiac_service.py` exercises:
- All twelve conventional sign transitions and preceding dates
- Invalid dates and February 29
- Name lookup, case-insensitivity, and missing names
- Complete profiles, interpretations, and planetary descriptions

Parameterized tests reduce duplication and make date-boundary expectations explicit. Tests import `ZodiacService` directly without starting `QApplication`.

### Local commands

```bash
python -m pip install pytest
python -m pytest
python -m pytest tests/test_zodiac_service.py -v
```

**Verification policy:** Report actual pytest results only after execution. Continue manual GUI regression checks for PySide6 pages, navigation, and visible error handling.

## A.5 Design decisions

**DD-007 — Reuse reference data:** The explorer consumes the existing `data/astrology.py` records rather than maintaining a second sign dataset.

**DD-008 — Service-layer calculation:** Zodiac date validation and profile assembly belong in `ZodiacService`, not Qt event handlers.

**DD-009 — Extend existing page:** The explorer is a third tab in `AstrologyPage`, avoiding an additional top-level navigation page.

**DD-010 — Pytest for service verification:** Unit tests focus on deterministic, UI-independent behavior; manual testing remains responsible for GUI verification.

**DD-011 — Cultural framing:** Interpretations are labeled as historical astrological associations, not scientific personality findings.

## A.6 Release verification

The v0.7.0 release is ready for documentation sign-off after the new service tests pass, the GUI is manually checked, and the SRS/SDD/changelog reflect the implemented behavior.
