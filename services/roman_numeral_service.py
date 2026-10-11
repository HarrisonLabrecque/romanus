
"""
Romanus - Roman Numeral Conversion Service

Converts integers to Roman numerals and Roman numerals
back to integers using standard modern notation.

Supported range: 1-3999
"""

from data.roman_numerals import (
    MIN_ROMAN_VALUE,
    MAX_ROMAN_VALUE,
    ROMAN_VALUES,
    ROMAN_CONVERSION_TABLE,
)


class RomanNumeralService:
    """Provide Roman numeral conversion and validation."""

    @staticmethod
    def to_roman(number):
        """
        Convert an integer into a Roman numeral.

        Args:
            number (int): Integer between 1 and 3999.

        Returns:
            str: Roman numeral representation.

        Raises:
            TypeError: If the input is not an integer.
            ValueError: If the integer is outside the supported range.
        """

        # Reject non-integer values, including booleans.
        if type(number) is not int:
            raise TypeError("Input must be an integer.")

        # Check the supported numeric range.
        if not MIN_ROMAN_VALUE <= number <= MAX_ROMAN_VALUE:
            raise ValueError(
                f"Number must be between "
                f"{MIN_ROMAN_VALUE} and {MAX_ROMAN_VALUE}."
            )

        result = []

        # Process values from largest to smallest.
        for value, symbol in ROMAN_CONVERSION_TABLE:
            count, number = divmod(number, value)

            # Append the symbol as many times as needed.
            result.append(symbol * count)

        return "".join(result)

    @staticmethod
    def from_roman(numeral):
        """
        Convert a Roman numeral into an integer.

        Args:
            numeral (str): Roman numeral in standard notation.

        Returns:
            int: Equivalent integer.

        Raises:
            TypeError: If input is not a string.
            ValueError: If the numeral is invalid.
        """

        if not isinstance(numeral, str):
            raise TypeError("Roman numeral must be a string.")

        # Accept lowercase input and surrounding whitespace.
        numeral = numeral.strip().upper()

        if not numeral:
            raise ValueError("Roman numeral cannot be empty.")

        total = 0
        index = 0

        # Read symbols from left to right.
        while index < len(numeral):
            current = ROMAN_VALUES.get(numeral[index])

            if current is None:
                raise ValueError(
                    f"Invalid Roman numeral symbol: {numeral[index]}"
                )

            # Look ahead for a possible subtractive pair.
            if index + 1 < len(numeral):
                next_value = ROMAN_VALUES.get(numeral[index + 1])

                if next_value is None:
                    raise ValueError(
                        "Invalid Roman numeral symbol: "
                        f"{numeral[index + 1]}"
                    )

                if current < next_value:
                    total += next_value - current
                    index += 2
                    continue

            total += current
            index += 1

        # Reject values outside the supported range.
        if not MIN_ROMAN_VALUE <= total <= MAX_ROMAN_VALUE:
            raise ValueError(
                "Roman numeral is outside the supported range."
            )

        # Convert back to Roman notation to ensure validity.
        # This rejects invalid forms such as IIII, IC, VX, and IIV.
        if RomanNumeralService.to_roman(total) != numeral:
            raise ValueError(
                "Invalid Roman numeral notation."
            )

        return total

    @staticmethod
    def is_valid_roman(numeral):
        """
        Check whether a Roman numeral uses valid notation.

        Args:
            numeral (str): Roman numeral to validate.

        Returns:
            bool: True if valid, otherwise False.
        """

        try:
            RomanNumeralService.from_roman(numeral)
            return True
        except (TypeError, ValueError):
            return False
