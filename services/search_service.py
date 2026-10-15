
"""
Romanus - Unified Search Service

Searches across the Latin alphabet, Greek alphabet,
Roman numerals, Greco-Roman deities, and Greek astrology.

Version: 0.6.0
"""

from data.latin_alphabet import get_latin_alphabet
from data.greek_alphabet import get_greek_alphabet

from data.roman_numerals import (
    get_roman_numerals,
    get_subtractive_numerals,
)

from data.deities import get_deities

from data.astrology import (
    get_zodiac_signs,
    get_traditional_planets,
)


class SearchService:
    """Provide unified searching across Romanus datasets."""

    @staticmethod
    def get_records():
        """
        Build normalized search records from all datasets.

        Returns:
            list[dict]: Reference records with consistent fields.
        """

        records = []

        # -----------------------------------------
        # Latin Alphabet
        # -----------------------------------------

        for letter in get_latin_alphabet():
            records.append({
                "category": "Latin Alphabet",
                "title": letter["uppercase"],
                "subtitle": letter["name"],
                "description": letter.get("description", ""),
                "page": "latin",
                "keywords": [
                    letter["uppercase"],
                    letter["lowercase"],
                    letter["name"],
                    letter.get("pronunciation", ""),
                ],
            })

        # -----------------------------------------
        # Greek Alphabet
        # -----------------------------------------

        for letter in get_greek_alphabet():
            records.append({
                "category": "Greek Alphabet",
                "title": letter["name"],
                "subtitle": (
                    f"{letter['uppercase']} "
                    f"{letter['lowercase']}"
                ),
                "description": letter.get("description", ""),
                "page": "greek",
                "keywords": [
                    letter["uppercase"],
                    letter["lowercase"],
                    letter["name"],
                    letter.get("transliteration", ""),
                    letter.get("pronunciation", ""),
                ],
            })

        # -----------------------------------------
        # Roman Numerals
        # -----------------------------------------

        numerals = (
            get_roman_numerals()
            + get_subtractive_numerals()
        )

        for numeral in numerals:
            records.append({
                "category": "Roman Numerals",
                "title": numeral["symbol"],
                "subtitle": str(numeral["value"]),
                "description": numeral.get("description", ""),
                "page": "numerals",
                "keywords": [
                    numeral["symbol"],
                    str(numeral["value"]),
                    numeral.get("name", ""),
                ],
            })

        # -----------------------------------------
        # Greco-Roman Deities
        # -----------------------------------------

        for deity in get_deities():
            records.append({
                "category": "Greco-Roman Deities",
                "title": deity["greek_name"],
                "subtitle": deity["roman_name"],
                "description": deity.get("description", ""),
                "page": "deities",
                "keywords": [
                    deity["greek_name"],
                    deity["roman_name"],
                    deity.get("domain", ""),
                    *deity.get("symbols", []),
                ],
            })

        # -----------------------------------------
        # Greek Astrology - Zodiac Signs
        # -----------------------------------------

        for sign in get_zodiac_signs():
            records.append({
                "category": "Greek Astrology",
                "title": sign["name"],
                "subtitle": (
                    f"{sign['symbol']} | "
                    f"{sign['element']}"
                ),
                "description": sign.get("description", ""),
                "page": "astrology",
                "keywords": [
                    sign["name"],
                    sign.get("greek_name", ""),
                    sign["symbol"],
                    sign.get("element", ""),
                    sign.get("modality", ""),
                    sign.get("ruling_planet", ""),
                ],
            })

        # -----------------------------------------
        # Greek Astrology - Traditional Planets
        # -----------------------------------------

        for planet in get_traditional_planets():
            records.append({
                "category": "Greek Astrology",
                "title": planet["name"],
                "subtitle": (
                    f"{planet['symbol']} | "
                    f"{planet['greek_name']}"
                ),
                "description": planet.get("description", ""),
                "page": "astrology",
                "keywords": [
                    planet["name"],
                    planet.get("greek_name", ""),
                    planet["symbol"],
                    *planet.get("rulerships", []),
                ],
            })

        return records

    @staticmethod
    def search(query, category="All Categories"):
        """
        Search all reference records.

        Args:
            query (str): Text entered by the user.
            category (str): Selected reference category.

        Returns:
            list[dict]: Matching reference records.
        """

        # Reject unsupported query types.
        if not isinstance(query, str):
            return []

        # Normalize text for case-insensitive searching.
        query = query.strip().casefold()

        results = []

        # Retrieve normalized reference records.
        records = SearchService.get_records()

        for record in records:

            # Apply category filtering.
            if (
                category != "All Categories"
                and record["category"] != category
            ):
                continue

            # Collect searchable fields.
            fields = [
                record["title"],
                record["subtitle"],
                record["description"],
                *record["keywords"],
            ]

            # An empty query returns all records
            # within the selected category.
            if not query:
                results.append(record)
                continue

            # Check whether the query matches any field.
            if any(
                query in str(field).casefold()
                for field in fields
            ):
                results.append(record)

        return results

    @staticmethod
    def get_categories():
        """
        Return available reference categories.

        Returns:
            list[str]: Category names used by the search UI.
        """

        return [
            "All Categories",
            "Latin Alphabet",
            "Greek Alphabet",
            "Roman Numerals",
            "Greco-Roman Deities",
            "Greek Astrology",
        ]
