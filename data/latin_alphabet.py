
"""
Romanus - Latin Alphabet Reference Data

This module contains reference information about the
23-letter classical Latin alphabet.

The data is separated from the PySide6 interface so
it can be reused throughout the application.

Version: 0.2.0
"""

# Classical Latin alphabet reference data.
LATIN_ALPHABET = [
    {
        "uppercase": "A",
        "lowercase": "a",
        "name": "A",
        "pronunciation": "a",
        "description": "A Latin vowel with short and long forms."
    },
    {
        "uppercase": "B",
        "lowercase": "b",
        "name": "Be",
        "pronunciation": "b",
        "description": "A voiced consonant."
    },
    {
        "uppercase": "C",
        "lowercase": "c",
        "name": "Ce",
        "pronunciation": "k",
        "description": "Generally pronounced as a hard K in Classical Latin."
    },
    {
        "uppercase": "D",
        "lowercase": "d",
        "name": "De",
        "pronunciation": "d",
        "description": "A voiced consonant."
    },
    {
        "uppercase": "E",
        "lowercase": "e",
        "name": "E",
        "pronunciation": "e",
        "description": "A Latin vowel with short and long forms."
    },
    {
        "uppercase": "F",
        "lowercase": "f",
        "name": "Ef",
        "pronunciation": "f",
        "description": "A voiceless consonant."
    },
    {
        "uppercase": "G",
        "lowercase": "g",
        "name": "Ge",
        "pronunciation": "g",
        "description": "Generally pronounced as a hard G in Classical Latin."
    },
    {
        "uppercase": "H",
        "lowercase": "h",
        "name": "Ha",
        "pronunciation": "h",
        "description": "Represented an aspirated sound in Classical Latin."
    },
    {
        "uppercase": "I",
        "lowercase": "i",
        "name": "I",
        "pronunciation": "i / j",
        "description": "Used for both vowel and consonantal sounds."
    },
    {
        "uppercase": "K",
        "lowercase": "k",
        "name": "Ka",
        "pronunciation": "k",
        "description": "An uncommon letter in Classical Latin."
    },
    {
        "uppercase": "L",
        "lowercase": "l",
        "name": "El",
        "pronunciation": "l",
        "description": "A lateral consonant."
    },
    {
        "uppercase": "M",
        "lowercase": "m",
        "name": "Em",
        "pronunciation": "m",
        "description": "A nasal consonant."
    },
    {
        "uppercase": "N",
        "lowercase": "n",
        "name": "En",
        "pronunciation": "n",
        "description": "A nasal consonant."
    },
    {
        "uppercase": "O",
        "lowercase": "o",
        "name": "O",
        "pronunciation": "o",
        "description": "A Latin vowel with short and long forms."
    },
    {
        "uppercase": "P",
        "lowercase": "p",
        "name": "Pe",
        "pronunciation": "p",
        "description": "A voiceless consonant."
    },
    {
        "uppercase": "Q",
        "lowercase": "q",
        "name": "Qu",
        "pronunciation": "kʷ",
        "description": "Usually appears with U to represent a labiovelar sound."
    },
    {
        "uppercase": "R",
        "lowercase": "r",
        "name": "Er",
        "pronunciation": "r",
        "description": "Typically pronounced with a trilled R."
    },
    {
        "uppercase": "S",
        "lowercase": "s",
        "name": "Es",
        "pronunciation": "s",
        "description": "Generally pronounced as a voiceless S."
    },
    {
        "uppercase": "T",
        "lowercase": "t",
        "name": "Te",
        "pronunciation": "t",
        "description": "A voiceless consonant."
    },
    {
        "uppercase": "V",
        "lowercase": "v",
        "name": "V",
        "pronunciation": "u / w",
        "description": "Represented both vowel U and consonantal W sounds."
    },
    {
        "uppercase": "X",
        "lowercase": "x",
        "name": "Ex",
        "pronunciation": "ks",
        "description": "Represents a combination of K and S sounds."
    },
    {
        "uppercase": "Y",
        "lowercase": "y",
        "name": "Y Graeca",
        "pronunciation": "y",
        "description": "Introduced primarily for words borrowed from Greek."
    },
    {
        "uppercase": "Z",
        "lowercase": "z",
        "name": "Zeta",
        "pronunciation": "z",
        "description": "Used primarily in Greek loanwords."
    }
]


def get_latin_alphabet():
    """
    Return the complete Latin alphabet reference dataset.

    Returns:
        list: A list of dictionaries containing letter data.
    """
    return [letter.copy() for letter in LATIN_ALPHABET]


def get_latin_letter(character):
    """
    Retrieve information about a Latin letter.

    Args:
        character (str): A single Latin letter.

    Returns:
        dict | None: Letter information if found, otherwise None.
    """
    if not isinstance(character, str) or len(character) != 1:
        return None

    for letter in LATIN_ALPHABET:
        if character in (
            letter["uppercase"],
            letter["lowercase"]
        ):
            return letter.copy()

    return None
