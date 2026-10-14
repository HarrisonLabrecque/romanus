
"""
Romanus - Greco-Roman Deity Reference Data

Contains structured reference information about major
Greek deities and their commonly associated Roman
counterparts.

Version: 0.4.0
"""


# Major Greek Olympian deities and their Roman counterparts.
#
# Greek and Roman religious traditions were distinct.
# The counterpart names below represent conventional
# associations rather than exact equivalences.

DEITIES = [
    {
        "id": 1,
        "greek_name": "Zeus",
        "roman_name": "Jupiter",
        "domain": "Sky, Thunder, and Kingship",
        "symbols": ["Thunderbolt", "Eagle", "Oak"],
        "description": (
            "Zeus is the ruler of the Olympian gods and the "
            "god of the sky, thunder, and divine authority. "
            "He is associated with justice, kingship, and "
            "the maintenance of cosmic order."
        ),
    },
    {
        "id": 2,
        "greek_name": "Hera",
        "roman_name": "Juno",
        "domain": "Marriage, Family, and Queenship",
        "symbols": ["Peacock", "Diadem", "Pomegranate"],
        "description": (
            "Hera is the queen of the Olympian gods and "
            "the goddess associated with marriage and "
            "legitimate family relationships. She is "
            "the wife of Zeus."
        ),
    },
    {
        "id": 3,
        "greek_name": "Poseidon",
        "roman_name": "Neptune",
        "domain": "Sea, Earthquakes, and Horses",
        "symbols": ["Trident", "Horse", "Dolphin"],
        "description": (
            "Poseidon is the god of the sea, earthquakes, "
            "and horses. He is a brother of Zeus and Hades "
            "and is frequently depicted holding a trident."
        ),
    },
    {
        "id": 4,
        "greek_name": "Demeter",
        "roman_name": "Ceres",
        "domain": "Agriculture, Grain, and Harvest",
        "symbols": ["Wheat", "Torch", "Cornucopia"],
        "description": (
            "Demeter is the goddess of agriculture, "
            "grain, and the fertility of cultivated land. "
            "Her mythology is closely connected with "
            "her daughter Persephone and the seasons."
        ),
    },
    {
        "id": 5,
        "greek_name": "Athena",
        "roman_name": "Minerva",
        "domain": "Wisdom, Strategy, and Crafts",
        "symbols": ["Owl", "Olive Tree", "Aegis"],
        "description": (
            "Athena is the goddess of wisdom, strategic "
            "warfare, and skilled crafts. She is the "
            "patron goddess of Athens and is often "
            "associated with the owl and olive tree."
        ),
    },
    {
        "id": 6,
        "greek_name": "Apollo",
        "roman_name": "Apollo",
        "domain": "Prophecy, Music, and Healing",
        "symbols": ["Lyre", "Laurel", "Bow"],
        "description": (
            "Apollo is associated with prophecy, music, "
            "healing, archery, and purification. His "
            "important sanctuary at Delphi was home "
            "to the famous oracle."
        ),
    },
    {
        "id": 7,
        "greek_name": "Artemis",
        "roman_name": "Diana",
        "domain": "Hunting, Wilderness, and Childbirth",
        "symbols": ["Bow", "Deer", "Cypress"],
        "description": (
            "Artemis is the goddess of hunting, wild "
            "animals, and wilderness. She is also "
            "associated with childbirth and the "
            "protection of young people."
        ),
    },
    {
        "id": 8,
        "greek_name": "Ares",
        "roman_name": "Mars",
        "domain": "War and Battle",
        "symbols": ["Spear", "Helmet", "Shield"],
        "description": (
            "Ares is the Greek god associated with "
            "the violence and conflict of warfare. "
            "His Roman counterpart Mars held a "
            "broader and more prominent civic role."
        ),
    },
    {
        "id": 9,
        "greek_name": "Aphrodite",
        "roman_name": "Venus",
        "domain": "Love, Beauty, and Desire",
        "symbols": ["Dove", "Rose", "Myrtle"],
        "description": (
            "Aphrodite is the goddess of love, beauty, "
            "and desire. She appears in numerous Greek "
            "myths involving gods, mortals, and "
            "relationships."
        ),
    },
    {
        "id": 10,
        "greek_name": "Hephaestus",
        "roman_name": "Vulcan",
        "domain": "Fire, Metalworking, and Craftsmanship",
        "symbols": ["Hammer", "Anvil", "Tongs"],
        "description": (
            "Hephaestus is the divine craftsman and "
            "god of metalworking and fire. He is "
            "associated with forging weapons, armor, "
            "and remarkable objects for the gods."
        ),
    },
    {
        "id": 11,
        "greek_name": "Hermes",
        "roman_name": "Mercury",
        "domain": "Travel, Trade, and Communication",
        "symbols": ["Caduceus", "Winged Sandals", "Tortoise"],
        "description": (
            "Hermes is the messenger of the gods and "
            "a deity associated with travelers, trade, "
            "boundaries, and communication. He also "
            "guides souls to the underworld."
        ),
    },
    {
        "id": 12,
        "greek_name": "Dionysus",
        "roman_name": "Bacchus",
        "domain": "Wine, Theater, and Ecstasy",
        "symbols": ["Grapevine", "Thyrsus", "Ivy"],
        "description": (
            "Dionysus is the god of wine, theater, "
            "festivity, and ecstatic religious experience. "
            "He is associated with transformation "
            "and the breaking of ordinary boundaries."
        ),
    },
]


def get_deities():
    """
    Return all deity reference records.

    Returns:
        list: Copies of the deity records.
    """
    return [
        {
            **deity,
            "symbols": deity["symbols"].copy(),
        }
        for deity in DEITIES
    ]


def get_deity_by_id(deity_id):
    """
    Retrieve a deity using its unique identifier.

    Args:
        deity_id (int): Unique deity identifier.

    Returns:
        dict | None: Deity information or None.
    """
    if type(deity_id) is not int:
        return None

    for deity in DEITIES:
        if deity["id"] == deity_id:
            return {
                **deity,
                "symbols": deity["symbols"].copy(),
            }

    return None


def get_deity_by_name(name):
    """
    Find a deity by its Greek or Roman name.

    Search is case-insensitive.

    Args:
        name (str): Greek or Roman deity name.

    Returns:
        dict | None: Matching deity information or None.
    """
    if not isinstance(name, str):
        return None

    name = name.strip().casefold()

    if not name:
        return None

    for deity in DEITIES:
        if (
            deity["greek_name"].casefold() == name
            or deity["roman_name"].casefold() == name
        ):
            return {
                **deity,
                "symbols": deity["symbols"].copy(),
            }

    return None


def search_deities(query):
    """
    Search deity names, domains, and descriptions.

    Args:
        query (str): Search term.

    Returns:
        list: Matching deity records.
    """
    if not isinstance(query, str):
        return []

    query = query.strip().casefold()

    if not query:
        return get_deities()

    results = []

    for deity in DEITIES:
        searchable_fields = [
            deity["greek_name"],
            deity["roman_name"],
            deity["domain"],
            deity["description"],
            *deity["symbols"],
        ]

        if any(
            query in field.casefold()
            for field in searchable_fields
        ):
            results.append(
                {
                    **deity,
                    "symbols": deity["symbols"].copy(),
                }
            )

    return results


def get_deity_count():
    """
    Return the total number of deity records.

    Returns:
        int: Number of deities.
    """
    return len(DEITIES)
