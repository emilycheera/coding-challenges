"""Convert a hexadecimal string, like '1A', into it's decimal equivalent.

    >>> hex_convert('6')
    6

    >>> hex_convert('10')
    16

    >>> hex_convert('FF')
    255

    >>> hex_convert('FFFF')
    65535
"""


def hex_convert(hex_in):
    """Convert a hexadecimal string, like '1A', into it's decimal equivalent."""

    # loop through hex_in in reverse order
    # multipler *= 16 each time I loop
    # result += multiplier * value (if value in vals, value = vals[value])
    # return result

    vals = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    result = 0

    for i, digit in enumerate(hex_in):
        if digit.isalpha():
            digit = vals[digit]
        else:
            digit = int(digit)
        multiplier = 16 ** (len(hex_in) - i - 1)
        result += (digit * multiplier)

    return result



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS. YOU'RE TERRIFIC!\n")
