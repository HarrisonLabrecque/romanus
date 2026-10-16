
"""
Romanus - Zodiac Service

Provides zodiac sign lookup, date validation, and historical
astrology profile information.

Version: 0.7.0
"""

from datetime import date

from data.astrology import (
    get_zodiac_sign,
    get_traditional_planet,
)


class ZodiacService:
    """
    Service responsible for zodiac calculations and profile retrieval.

    Uses conventional Western tropical zodiac date ranges.
    These ranges are approximate and intended for historical
    reference rather than astronomical calculations.
    """

    # --------------------------------------------------
    # Zodiac Date Boundaries
    # --------------------------------------------------

    ZODIAC_DATES = [
        (1, 20, "Aquarius"),
        (2, 19, "Pisces"),
        (3, 21, "Aries"),
        (4, 20, "Taurus"),
        (5, 21, "Gemini"),
        (6, 21, "Cancer"),
        (7, 23, "Leo"),
        (8, 23, "Virgo"),
        (9, 23, "Libra"),
        (10, 23, "Scorpio"),
        (11, 22, "Sagittarius"),
        (12, 22, "Capricorn"),
    ]

    # --------------------------------------------------
    # Traditional Zodiac Interpretations
    # --------------------------------------------------

    INTERPRETATIONS = {
        "Aries": (
            "Traditionally associated with initiative, "
            "action, and beginnings."
        ),
        "Taurus": (
            "Traditionally associated with stability, "
            "cultivation, and resources."
        ),
        "Gemini": (
            "Traditionally associated with communication, "
            "learning, and exchange."
        ),
        "Cancer": (
            "Traditionally associated with home, "
            "care, and protection."
        ),
        "Leo": (
            "Traditionally associated with leadership, "
            "expression, and creativity."
        ),
        "Virgo": (
            "Traditionally associated with analysis, "
            "organization, and practical work."
        ),
        "Libra": (
            "Traditionally associated with harmony, "
            "balance, and cooperation."
        ),
        "Scorpio": (
            "Traditionally associated with intensity, "
            "persistence, and transformation."
        ),
        "Sagittarius": (
            "Traditionally associated with exploration, "
            "philosophy, and learning."
        ),
        "Capricorn": (
            "Traditionally associated with discipline, "
            "responsibility, and structure."
        ),
        "Aquarius": (
            "Traditionally associated with community, "
            "principles, and independence."
        ),
        "Pisces": (
            "Traditionally associated with imagination, "
            "compassion, and reflection."
        ),
    }

    # --------------------------------------------------
    # Zodiac Date Lookup
    # --------------------------------------------------

    @staticmethod
    def get_sign_by_date(month, day):
        """
        Determine the zodiac sign for a calendar month and day.

        Args:
            month (int): Calendar month (1-12).
            day (int): Calendar day.

        Returns:
            str: Zodiac sign name.

        Raises:
            ValueError: If the calendar date is invalid.
        """

        # Use a leap year so February 29 is supported.
        date(2000, month, day)

        # Capricorn spans the end and beginning of the year.
        sign_name = "Capricorn"

        # Find the latest zodiac boundary that has been reached.
        for start_month, start_day, name in ZodiacService.ZODIAC_DATES:
            if (month, day) >= (start_month, start_day):
                sign_name = name

        return sign_name

    # --------------------------------------------------
    # Zodiac Name Lookup
    # --------------------------------------------------

    @staticmethod
    def get_sign_by_name(name):
        """
        Retrieve zodiac reference data using a sign name.

        Args:
            name (str): Zodiac sign name.

        Returns:
            dict | None: Zodiac data if found.
        """

        return get_zodiac_sign(name)

    # --------------------------------------------------
    # Complete Zodiac Profile
    # --------------------------------------------------

    @staticmethod
    def get_zodiac_profile(name):
        """
        Retrieve a complete historical zodiac profile.

        The returned dictionary includes the original zodiac
        reference data, a traditional interpretation, and
        information about the traditional ruling planet.

        Args:
            name (str): Zodiac sign name.

        Returns:
            dict | None: Complete profile if found.
        """

        # Retrieve the zodiac sign from the reference dataset.
        sign = get_zodiac_sign(name)

        # Return None if the requested sign does not exist.
        if sign is None:
            return None

        # Retrieve the traditional ruling planet.
        ruler = get_traditional_planet(
            sign["ruling_planet"]
        )

        # Retrieve the sign's traditional interpretation.
        interpretation = ZodiacService.INTERPRETATIONS.get(
            sign["name"],
            ""
        )

        # Retrieve the ruling planet's description.
        planet_description = (
            ruler["description"]
            if ruler is not None
            else ""
        )

        # Combine all reference information into one profile.
        profile = {
            **sign,
            "interpretation": interpretation,
            "planet_description": planet_description,
        }

        return profile

    # --------------------------------------------------
    # Zodiac Profile by Date
    # --------------------------------------------------

    @staticmethod
    def get_profile_by_date(month, day):
        """
        Retrieve a complete zodiac profile using a calendar date.

        Args:
            month (int): Calendar month.
            day (int): Calendar day.

        Returns:
            dict: Complete zodiac profile.

        Raises:
            ValueError: If the date is invalid.
        """

        # Determine the zodiac sign from the provided date.
        sign_name = ZodiacService.get_sign_by_date(
            month,
            day
        )

        # Return the complete profile for the identified sign.
        return ZodiacService.get_zodiac_profile(sign_name)
