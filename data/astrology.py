
"""
Romanus - Greek and Hellenistic Astrology Reference Data

Contains historical reference information about the
twelve zodiac signs, seven traditional planets,
and classical planetary rulerships.

Astrological associations are presented as historical
traditions, not scientifically established effects.

Version: 0.5.0
"""


# The twelve signs of the tropical zodiac.
ZODIAC_SIGNS = [
    {
        "id": 1,
        "name": "Aries",
        "greek_name": "Krios",
        "symbol": "♈",
        "element": "Fire",
        "modality": "Cardinal",
        "ruling_planet": "Mars",
        "description": (
            "Aries represents the ram and marks the beginning "
            "of the traditional tropical zodiac. In Hellenistic "
            "astrology, it is the domicile of Mars."
        ),
    },
    {
        "id": 2,
        "name": "Taurus",
        "greek_name": "Tauros",
        "symbol": "♉",
        "element": "Earth",
        "modality": "Fixed",
        "ruling_planet": "Venus",
        "description": (
            "Taurus represents the bull. It is traditionally "
            "associated with the earth element and is the "
            "domicile of Venus."
        ),
    },
    {
        "id": 3,
        "name": "Gemini",
        "greek_name": "Didymoi",
        "symbol": "♊",
        "element": "Air",
        "modality": "Mutable",
        "ruling_planet": "Mercury",
        "description": (
            "Gemini represents the twins. In traditional "
            "astrology, it belongs to the air element "
            "and is ruled by Mercury."
        ),
    },
    {
        "id": 4,
        "name": "Cancer",
        "greek_name": "Karkinos",
        "symbol": "♋",
        "element": "Water",
        "modality": "Cardinal",
        "ruling_planet": "Moon",
        "description": (
            "Cancer represents the crab. It is associated "
            "with the water element and is the traditional "
            "domicile of the Moon."
        ),
    },
    {
        "id": 5,
        "name": "Leo",
        "greek_name": "Leon",
        "symbol": "♌",
        "element": "Fire",
        "modality": "Fixed",
        "ruling_planet": "Sun",
        "description": (
            "Leo represents the lion. It is associated "
            "with the fire element and is the traditional "
            "domicile of the Sun."
        ),
    },
    {
        "id": 6,
        "name": "Virgo",
        "greek_name": "Parthenos",
        "symbol": "♍",
        "element": "Earth",
        "modality": "Mutable",
        "ruling_planet": "Mercury",
        "description": (
            "Virgo represents the maiden. It belongs "
            "to the earth element and is traditionally "
            "ruled by Mercury."
        ),
    },
    {
        "id": 7,
        "name": "Libra",
        "greek_name": "Zygos",
        "symbol": "♎",
        "element": "Air",
        "modality": "Cardinal",
        "ruling_planet": "Venus",
        "description": (
            "Libra represents the scales. It is associated "
            "with the air element and is the traditional "
            "domicile of Venus."
        ),
    },
    {
        "id": 8,
        "name": "Scorpio",
        "greek_name": "Skorpios",
        "symbol": "♏",
        "element": "Water",
        "modality": "Fixed",
        "ruling_planet": "Mars",
        "description": (
            "Scorpio represents the scorpion. In traditional "
            "astrology, it belongs to the water element "
            "and is ruled by Mars."
        ),
    },
    {
        "id": 9,
        "name": "Sagittarius",
        "greek_name": "Toxotes",
        "symbol": "♐",
        "element": "Fire",
        "modality": "Mutable",
        "ruling_planet": "Jupiter",
        "description": (
            "Sagittarius represents the archer. It belongs "
            "to the fire element and is traditionally "
            "ruled by Jupiter."
        ),
    },
    {
        "id": 10,
        "name": "Capricorn",
        "greek_name": "Aigokeros",
        "symbol": "♑",
        "element": "Earth",
        "modality": "Cardinal",
        "ruling_planet": "Saturn",
        "description": (
            "Capricorn represents the sea-goat. It is "
            "associated with the earth element and "
            "is traditionally ruled by Saturn."
        ),
    },
    {
        "id": 11,
        "name": "Aquarius",
        "greek_name": "Hydrochoos",
        "symbol": "♒",
        "element": "Air",
        "modality": "Fixed",
        "ruling_planet": "Saturn",
        "description": (
            "Aquarius represents the water-bearer. "
            "Despite its imagery, it belongs to the "
            "air element and is traditionally ruled "
            "by Saturn."
        ),
    },
    {
        "id": 12,
        "name": "Pisces",
        "greek_name": "Ichthyes",
        "symbol": "♓",
        "element": "Water",
        "modality": "Mutable",
        "ruling_planet": "Jupiter",
        "description": (
            "Pisces represents the fishes. It is "
            "associated with the water element "
            "and is traditionally ruled by Jupiter."
        ),
    },
]


# Seven traditional astrological planets.
#
# In historical astrology, the Sun and Moon are counted
# among the seven planets, or wandering celestial bodies.
TRADITIONAL_PLANETS = [
    {
        "name": "Sun",
        "greek_name": "Helios",
        "symbol": "☉",
        "rulerships": ["Leo"],
        "description": (
            "The Sun was associated with light, authority, "
            "and visibility in ancient astrological traditions."
        ),
    },
    {
        "name": "Moon",
        "greek_name": "Selene",
        "symbol": "☽",
        "rulerships": ["Cancer"],
        "description": (
            "The Moon was associated with change, cycles, "
            "growth, and the rhythms of earthly life."
        ),
    },
    {
        "name": "Mercury",
        "greek_name": "Hermes",
        "symbol": "☿",
        "rulerships": ["Gemini", "Virgo"],
        "description": (
            "Mercury was associated with communication, "
            "reasoning, trade, and interpretation."
        ),
    },
    {
        "name": "Venus",
        "greek_name": "Aphrodite",
        "symbol": "♀",
        "rulerships": ["Taurus", "Libra"],
        "description": (
            "Venus was associated with harmony, affection, "
            "beauty, and social relationships."
        ),
    },
    {
        "name": "Mars",
        "greek_name": "Ares",
        "symbol": "♂",
        "rulerships": ["Aries", "Scorpio"],
        "description": (
            "Mars was associated with conflict, force, "
            "competition, and warfare."
        ),
    },
    {
        "name": "Jupiter",
        "greek_name": "Zeus",
        "symbol": "♃",
        "rulerships": ["Sagittarius", "Pisces"],
        "description": (
            "Jupiter was associated with justice, "
            "prosperity, authority, and beneficence."
        ),
    },
    {
        "name": "Saturn",
        "greek_name": "Kronos",
        "symbol": "♄",
        "rulerships": ["Capricorn", "Aquarius"],
        "description": (
            "Saturn was associated with boundaries, "
            "time, restriction, and endurance."
        ),
    },
]


def get_zodiac_signs():
    """Return copies of all zodiac sign records."""
    return [sign.copy() for sign in ZODIAC_SIGNS]


def get_zodiac_sign(name):
    """
    Find a zodiac sign by name.

    Returns None if the sign does not exist.
    """
    if not isinstance(name, str):
        return None

    name = name.strip().casefold()

    for sign in ZODIAC_SIGNS:
        if sign["name"].casefold() == name:
            return sign.copy()

    return None


def get_traditional_planets():
    """Return copies of the traditional planet records."""
    return [
        {
            **planet,
            "rulerships": planet["rulerships"].copy(),
        }
        for planet in TRADITIONAL_PLANETS
    ]


def get_traditional_planet(name):
    """Find a traditional planet by name."""
    if not isinstance(name, str):
        return None

    name = name.strip().casefold()

    for planet in TRADITIONAL_PLANETS:
        if planet["name"].casefold() == name:
            return {
                **planet,
                "rulerships": planet["rulerships"].copy(),
            }

    return None


def search_zodiac_signs(query):
    """
    Search zodiac signs by name, element,
    modality, ruler, or description.
    """
    if not isinstance(query, str):
        return []

    query = query.strip().casefold()

    if not query:
        return get_zodiac_signs()

    results = []

    for sign in ZODIAC_SIGNS:
        fields = [
            sign["name"],
            sign["greek_name"],
            sign["element"],
            sign["modality"],
            sign["ruling_planet"],
            sign["description"],
        ]

        if any(query in field.casefold() for field in fields):
            results.append(sign.copy())

    return results


def search_traditional_planets(query):
    """
    Search planets by name, Greek association,
    rulership, or description.
    """
    if not isinstance(query, str):
        return []

    query = query.strip().casefold()

    if not query:
        return get_traditional_planets()

    results = []

    for planet in TRADITIONAL_PLANETS:
        fields = [
            planet["name"],
            planet["greek_name"],
            planet["description"],
            *planet["rulerships"],
        ]

        if any(query in field.casefold() for field in fields):
            results.append(
                {
                    **planet,
                    "rulerships": planet["rulerships"].copy(),
                }
            )

    return results


def get_zodiac_count():
    """Return the number of zodiac signs."""
    return len(ZODIAC_SIGNS)


def get_planet_count():
    """Return the number of traditional planets."""
    return len(TRADITIONAL_PLANETS)
