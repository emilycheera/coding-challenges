"""Convert a decimal number to binary representation.

For example::

    >>> dec2bin(0)
    '0'

    >>> dec2bin(1)
    '1'

    >>> dec2bin(2)
    '10'

    >>> dec2bin(4)
    '100'

    >>> dec2bin(15)
    '1111'

"""


def dec2bin(num):
    """Convert a decimal number to binary representation."""

    if num == 0:
        return "0"

    rem_stack = []

    while num > 0:
        rem = num % 2
        rem_stack.append(rem)
        num = num // 2

    bin_str = ""

    while rem_stack:
        bin_str += str(rem_stack.pop())

    return bin_str


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. W00T!\n")
