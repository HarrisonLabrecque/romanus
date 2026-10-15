
"""
Romanus - Zodiac Service

Determines Western zodiac signs from calendar dates
and retrieves traditional Greek astrology information.

Version: 0.7.0
"""

from datetime import date

from data.astrology import get_zodiac_signs


class ZodiacService:
    """Provide zodiac sign lookup and reference profiles."""

    # Conventional Western tropical zodiac date ranges.
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

    @staticmethod
    def get_sign_by_date(month, day):
        """
        Determine the zodiac sign for a month and day.

        Args:
            month (int): Birth month (1-12).
            day (int): Birth day.

        Returns:
            str: Zodiac sign name.

        Raises:
            ValueError: If the date is invalid.
        """

        # Use a leap year so February 29 is accepted.
        date(2000, month, day)

        sign = "Capricorn"

        for start_month, start_day, name in ZodiacService.ZODIAC_DATES:
            if (month, day) >= (start_month, start_day):
                sign = name

        return sign

    @staticmethod
    def get_sign_by_name(name):
        """
        Retrieve a zodiac sign by name.

        Args:
            name (str): Zodiac sign name.

        Returns:
            dict | None: Matching zodiac reference.
        """

        if not isinstance(name, str):
            return None

        for sign in get_zodiac_signs():
            if sign["name"].casefold() == name.strip().casefold():
                return sign.copy()

        return None

    @staticmethod
    def get_zodiac_profile(name):
        """
        Generate a traditional astrology reference profile.

        Args:
            name (str): Zodiac sign name.

        Returns:
            dict | None: Zodiac profile.
        """

        sign = ZodiacService.get_sign_by_name(name)

        if sign is None:
            return None

        return {
            "name": sign["name"],
            "greek_name": sign.get("greek_name", ""),
            "symbol": sign.get("symbol", ""),
            "element": sign.get("element", ""),
            "modality": sign.get("modality", ""),
            "ruling_planet": sign.get("ruling_planet", ""),
            "description": sign.get("description", ""),
        }

    @staticmethod
    def get_profile_by_date(month, day):
        """
        Generate a zodiac profile using a birth date.

        Returns:
            dict: Zodiac reference profile.
        """

        name = ZodiacService.get_sign_by_date(month, day)

        return ZodiacService.get_zodiac_profile(name)
