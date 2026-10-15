
"""
Romanus - Latin Alphabet Reference Data

Contains reference information about the modern
26-letter Latin alphabet, including pronunciation,
historical origins, and letter descriptions.

The classical Latin alphabet originally contained
23 letters. J, U, and W developed later.

Version: 0.6.0
"""

# Modern 26-letter Latin alphabet reference data.
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
        "description": "Historically represented both vowel and consonantal sounds."
    },
    {
        "uppercase": "J",
        "lowercase": "j",
        "name": "J",
        "pronunciation": "dʒ / j",
        "description": (
            "Developed from the letter I. It became a "
            "distinct letter in later Latin-script alphabets."
        )
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
        "uppercase": "U",
        "lowercase": "u",
        "name": "U",
        "pronunciation": "u",
        "description": (
            "Developed as a distinct form of V. "
            "It represents a vowel in modern Latin-script alphabets."
        )
    },
    {
        "uppercase": "V",
        "lowercase": "v",
        "name": "V",
        "pronunciation": "w / v",
        "description": (
            "In Classical Latin, V represented both vowel "
            "and consonantal sounds. It later became distinct from U."
        )
    },
    {
        "uppercase": "W",
        "lowercase": "w",
        "name": "Double U",
        "pronunciation": "w",
        "description": (
            "Developed from doubled U or V forms in medieval "
            "European writing. It was not part of Classical Latin."
        )
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
    Return the complete 26-letter Latin alphabet.

    Returns:
        list[dict]: Copies of the Latin letter records.
    """
    return [letter.copy() for letter in LATIN_ALPHABET]


def get_latin_letter(character):
    """
    Retrieve information about a Latin letter.

    Args:
        character (str): A single Latin letter.

    Returns:
        dict | None: Matching letter information,
        or None if the character is not found.
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


def get_latin_letter_count():
    """
    Return the number of Latin alphabet letters.

    Returns:
        int: Total number of letters.
    """
    return len(LATIN_ALPHABET)
