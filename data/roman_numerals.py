
"""
Romanus - Roman Numeral Reference Data

Contains reference information for Roman numeral symbols,
their numerical values, and standard subtractive combinations.

Conversion algorithms are implemented separately in:
    services/roman_numeral_service.py

Supported range: 1-3999
Version: 0.3.0
"""

# Minimum and maximum supported values.
MIN_ROMAN_VALUE = 1
MAX_ROMAN_VALUE = 3999


# Primary Roman numeral symbols.
ROMAN_NUMERALS = [
    {
        "symbol": "I",
        "value": 1,
        "name": "Unus",
        "description": "Represents the value one."
    },
    {
        "symbol": "V",
        "value": 5,
        "name": "Quinque",
        "description": "Represents the value five."
    },
    {
        "symbol": "X",
        "value": 10,
        "name": "Decem",
        "description": "Represents the value ten."
    },
    {
        "symbol": "L",
        "value": 50,
        "name": "Quinquaginta",
        "description": "Represents the value fifty."
    },
    {
        "symbol": "C",
        "value": 100,
        "name": "Centum",
        "description": "Represents the value one hundred."
    },
    {
        "symbol": "D",
        "value": 500,
        "name": "Quingenti",
        "description": "Represents the value five hundred."
    },
    {
        "symbol": "M",
        "value": 1000,
        "name": "Mille",
        "description": "Represents the value one thousand."
    },
]


# Standard subtractive numeral combinations.
SUBTRACTIVE_NUMERALS = [
    {
        "symbol": "IV",
        "value": 4,
        "description": "One before five."
    },
    {
        "symbol": "IX",
        "value": 9,
        "description": "One before ten."
    },
    {
        "symbol": "XL",
        "value": 40,
        "description": "Ten before fifty."
    },
    {
        "symbol": "XC",
        "value": 90,
        "description": "Ten before one hundred."
    },
    {
        "symbol": "CD",
        "value": 400,
        "description": "One hundred before five hundred."
    },
    {
        "symbol": "CM",
        "value": 900,
        "description": "One hundred before one thousand."
    },
]


# Numeral values in descending order.
# This mapping will be useful for conversion services.
ROMAN_VALUES = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1,
}


# Standard notation ordered from largest to smallest.
# Includes subtractive combinations.
ROMAN_CONVERSION_TABLE = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]


def get_roman_numerals():
    """
    Return the primary Roman numeral reference dataset.

    Returns:
        list: A copy of the Roman numeral reference entries.
    """
    return [numeral.copy() for numeral in ROMAN_NUMERALS]


def get_subtractive_numerals():
    """
    Return the standard subtractive numeral combinations.

    Returns:
        list: A copy of the subtractive reference entries.
    """
    return [numeral.copy() for numeral in SUBTRACTIVE_NUMERALS]


def get_roman_symbol(symbol):
    """
    Retrieve information about a Roman numeral symbol.

    Args:
        symbol (str): A single Roman numeral symbol.

    Returns:
        dict | None: Symbol information or None if not found.
    """
    if not isinstance(symbol, str):
        return None

    symbol = symbol.upper()

    for numeral in ROMAN_NUMERALS:
        if numeral["symbol"] == symbol:
            return numeral.copy()

    return None


def get_subtractive_symbol(symbol):
    """
    Retrieve information about a subtractive combination.

    Args:
        symbol (str): A subtractive Roman numeral combination.

    Returns:
        dict | None: Combination information or None if not found.
    """
    if not isinstance(symbol, str):
        return None

    symbol = symbol.upper()

    for numeral in SUBTRACTIVE_NUMERALS:
        if numeral["symbol"] == symbol:
            return numeral.copy()

    return None
