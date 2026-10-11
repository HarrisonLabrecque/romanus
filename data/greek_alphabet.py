
"""
Romanus - Greek Alphabet Reference Data

Contains reference information for the 24 letters
of the standard Greek alphabet.

Pronunciations use approximate Classical Attic Greek
sound values, represented using IPA notation.

Version: 0.2.0
"""

# Greek alphabet reference data.
GREEK_ALPHABET = [
    {
        "uppercase": "Α",
        "lowercase": "α",
        "name": "Alpha",
        "transliteration": "a",
        "pronunciation": "a",
        "description": "First letter of the Greek alphabet. A vowel."
    },
    {
        "uppercase": "Β",
        "lowercase": "β",
        "name": "Beta",
        "transliteration": "b",
        "pronunciation": "b",
        "description": "A voiced bilabial stop in Classical Greek."
    },
    {
        "uppercase": "Γ",
        "lowercase": "γ",
        "name": "Gamma",
        "transliteration": "g",
        "pronunciation": "ɡ",
        "description": "A voiced velar consonant; nasal before certain consonants."
    },
    {
        "uppercase": "Δ",
        "lowercase": "δ",
        "name": "Delta",
        "transliteration": "d",
        "pronunciation": "d",
        "description": "A voiced dental stop."
    },
    {
        "uppercase": "Ε",
        "lowercase": "ε",
        "name": "Epsilon",
        "transliteration": "e",
        "pronunciation": "e",
        "description": "A short vowel, distinct from Eta."
    },
    {
        "uppercase": "Ζ",
        "lowercase": "ζ",
        "name": "Zeta",
        "transliteration": "z",
        "pronunciation": "zd / dz",
        "description": "A consonant whose precise Classical pronunciation is debated."
    },
    {
        "uppercase": "Η",
        "lowercase": "η",
        "name": "Eta",
        "transliteration": "ē",
        "pronunciation": "ɛː",
        "description": "A long open-mid front vowel in Classical Attic."
    },
    {
        "uppercase": "Θ",
        "lowercase": "θ",
        "name": "Theta",
        "transliteration": "th",
        "pronunciation": "tʰ",
        "description": "An aspirated dental stop in Classical Greek."
    },
    {
        "uppercase": "Ι",
        "lowercase": "ι",
        "name": "Iota",
        "transliteration": "i",
        "pronunciation": "i / iː",
        "description": "A vowel that may be short or long."
    },
    {
        "uppercase": "Κ",
        "lowercase": "κ",
        "name": "Kappa",
        "transliteration": "k",
        "pronunciation": "k",
        "description": "A voiceless velar stop."
    },
    {
        "uppercase": "Λ",
        "lowercase": "λ",
        "name": "Lambda",
        "transliteration": "l",
        "pronunciation": "l",
        "description": "A lateral consonant."
    },
    {
        "uppercase": "Μ",
        "lowercase": "μ",
        "name": "Mu",
        "transliteration": "m",
        "pronunciation": "m",
        "description": "A bilabial nasal consonant."
    },
    {
        "uppercase": "Ν",
        "lowercase": "ν",
        "name": "Nu",
        "transliteration": "n",
        "pronunciation": "n",
        "description": "An alveolar nasal consonant."
    },
    {
        "uppercase": "Ξ",
        "lowercase": "ξ",
        "name": "Xi",
        "transliteration": "x",
        "pronunciation": "ks",
        "description": "Represents a combination of K and S sounds."
    },
    {
        "uppercase": "Ο",
        "lowercase": "ο",
        "name": "Omicron",
        "transliteration": "o",
        "pronunciation": "o",
        "description": "A short vowel, distinct from Omega."
    },
    {
        "uppercase": "Π",
        "lowercase": "π",
        "name": "Pi",
        "transliteration": "p",
        "pronunciation": "p",
        "description": "A voiceless bilabial stop."
    },
    {
        "uppercase": "Ρ",
        "lowercase": "ρ",
        "name": "Rho",
        "transliteration": "r",
        "pronunciation": "r",
        "description": "Generally reconstructed as a trilled consonant."
    },
    {
        "uppercase": "Σ",
        "lowercase": "σ",
        "name": "Sigma",
        "transliteration": "s",
        "pronunciation": "s",
        "description": "A voiceless sibilant; uses ς at the end of words."
    },
    {
        "uppercase": "Τ",
        "lowercase": "τ",
        "name": "Tau",
        "transliteration": "t",
        "pronunciation": "t",
        "description": "A voiceless dental stop."
    },
    {
        "uppercase": "Υ",
        "lowercase": "υ",
        "name": "Upsilon",
        "transliteration": "y",
        "pronunciation": "y / yː",
        "description": "A rounded front vowel in Classical Attic Greek."
    },
    {
        "uppercase": "Φ",
        "lowercase": "φ",
        "name": "Phi",
        "transliteration": "ph",
        "pronunciation": "pʰ",
        "description": "An aspirated bilabial stop in Classical Greek."
    },
    {
        "uppercase": "Χ",
        "lowercase": "χ",
        "name": "Chi",
        "transliteration": "kh",
        "pronunciation": "kʰ",
        "description": "An aspirated velar stop in Classical Greek."
    },
    {
        "uppercase": "Ψ",
        "lowercase": "ψ",
        "name": "Psi",
        "transliteration": "ps",
        "pronunciation": "ps",
        "description": "Represents a combination of P and S sounds."
    },
    {
        "uppercase": "Ω",
        "lowercase": "ω",
        "name": "Omega",
        "transliteration": "ō",
        "pronunciation": "ɔː",
        "description": "A long open-mid back vowel in Classical Attic."
    },
]


def get_greek_alphabet():
    """
    Return the complete Greek alphabet reference dataset.

    Returns:
        list: A list of dictionaries containing Greek letter data.
    """
    return [letter.copy() for letter in GREEK_ALPHABET]


def get_greek_letter(character):
    """
    Retrieve reference information for a Greek letter.

    Args:
        character (str): A single Greek letter.

    Returns:
        dict | None: Letter information, or None if not found.
    """
    if not isinstance(character, str) or len(character) != 1:
        return None

    # Final sigma is an alternate lowercase form of Sigma.
    if character == "ς":
        character = "σ"

    for letter in GREEK_ALPHABET:
        if character in (
            letter["uppercase"],
            letter["lowercase"]
        ):
            return letter.copy()

    return None
