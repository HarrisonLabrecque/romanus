
"""
Romanus - Zodiac Service Unit Tests

Tests zodiac date calculations, profile retrieval,
and invalid input handling.

Run with:
    python -m pytest

Version: 0.7.0
"""

import pytest

from services.zodiac_service import ZodiacService


# --------------------------------------------------
# Zodiac Sign Lookup Tests
# --------------------------------------------------

@pytest.mark.parametrize(
    "month, day, expected",
    [
        (1, 1, "Capricorn"),
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
        (12, 31, "Capricorn"),
    ],
)
def test_zodiac_sign_by_date(month, day, expected):
    """Verify zodiac signs are returned for valid dates."""

    result = ZodiacService.get_sign_by_date(month, day)

    assert result == expected


@pytest.mark.parametrize(
    "month, day, expected",
    [
        (1, 19, "Capricorn"),
        (2, 18, "Aquarius"),
        (3, 20, "Pisces"),
        (4, 19, "Aries"),
        (5, 20, "Taurus"),
        (6, 20, "Gemini"),
        (7, 22, "Cancer"),
        (8, 22, "Leo"),
        (9, 22, "Virgo"),
        (10, 22, "Libra"),
        (11, 21, "Scorpio"),
        (12, 21, "Sagittarius"),
    ],
)
def test_zodiac_dates_before_transition(month, day, expected):
    """Verify dates immediately before zodiac transitions."""

    result = ZodiacService.get_sign_by_date(month, day)

    assert result == expected


# --------------------------------------------------
# Calendar Validation Tests
# --------------------------------------------------

@pytest.mark.parametrize(
    "month, day",
    [
        (0, 10),
        (13, 10),
        (1, 0),
        (1, 32),
        (2, 30),
        (4, 31),
        (6, 31),
        (9, 31),
        (11, 31),
    ],
)
def test_invalid_calendar_dates(month, day):
    """Invalid dates must raise ValueError."""

    with pytest.raises(ValueError):
        ZodiacService.get_sign_by_date(month, day)


def test_february_29_is_supported():
    """February 29 should be valid for month/day lookup."""

    result = ZodiacService.get_sign_by_date(2, 29)

    assert result == "Pisces"


# --------------------------------------------------
# Zodiac Name Lookup Tests
# --------------------------------------------------

def test_get_sign_by_name():
    """Retrieve an existing zodiac sign."""

    sign = ZodiacService.get_sign_by_name("Aries")

    assert sign is not None
    assert sign["name"] == "Aries"
    assert sign["element"] == "Fire"


def test_get_sign_by_name_case_insensitive():
    """Sign lookup should ignore letter casing."""

    sign = ZodiacService.get_sign_by_name("aries")

    assert sign is not None
    assert sign["name"] == "Aries"


def test_unknown_zodiac_sign():
    """Unknown zodiac signs should return None."""

    result = ZodiacService.get_sign_by_name("Unknown")

    assert result is None


# --------------------------------------------------
# Zodiac Profile Tests
# --------------------------------------------------

def test_get_zodiac_profile():
    """A zodiac profile should contain the expected fields."""

    profile = ZodiacService.get_zodiac_profile("Aries")

    assert profile is not None
    assert profile["name"] == "Aries"
    assert profile["symbol"] == "♈"
    assert profile["element"] == "Fire"
    assert profile["modality"] == "Cardinal"
    assert profile["ruling_planet"] == "Mars"


def test_profile_contains_interpretation():
    """Profiles should contain a traditional interpretation."""

    profile = ZodiacService.get_zodiac_profile("Leo")

    assert profile is not None
    assert isinstance(profile["interpretation"], str)
    assert profile["interpretation"]


def test_profile_contains_planet_description():
    """Profiles should include traditional planetary information."""

    profile = ZodiacService.get_zodiac_profile("Taurus")

    assert profile is not None
    assert isinstance(profile["planet_description"], str)
    assert profile["planet_description"]


def test_unknown_profile():
    """Unknown zodiac profiles should return None."""

    result = ZodiacService.get_zodiac_profile("Unknown")

    assert result is None


def test_get_profile_by_date():
    """Birth-date lookup should return the complete zodiac profile."""

    profile = ZodiacService.get_profile_by_date(4, 10)

    assert profile is not None
    assert profile["name"] == "Aries"
    assert profile["ruling_planet"] == "Mars"


@pytest.mark.parametrize(
    "name",
    [
        "Aries",
        "Taurus",
        "Gemini",
        "Cancer",
        "Leo",
        "Virgo",
        "Libra",
        "Scorpio",
        "Sagittarius",
        "Capricorn",
        "Aquarius",
        "Pisces",
    ],
)
def test_all_zodiac_profiles(name):
    """Every zodiac sign should have a complete reference profile."""

    profile = ZodiacService.get_zodiac_profile(name)

    assert profile is not None
    assert profile["name"] == name
    assert profile["description"]
    assert profile["interpretation"]
    assert profile["planet_description"]
