"""Reverse word order, keeping spaces.

As a simple case, an empty string returns an empty string:

    >>> rev("")
    ''

A simple word is also the same:

    >>> rev("hello")
    'hello'

Here, we reverse the order of the words, preserving the space between:

    >>> rev("hello world")
    'world hello'

Here, we reverse the worlds, preserving space---so it it should start with
the 3 spaces that came after world, etc:

    >>> rev(" hello  world   ")
    '   world  hello '

To prove the alternate solution works:

    >>> rev(" hello  world   ")
    '   world  hello '

"""


def rev(s):
    """Reverse word-order in string, preserving spaces."""

    new_string = ""
    i = len(s) - 1

    while i >= 0:
        if s[i] == " ":
            new_string += s[i]
            i -= 1
        else:
            end_idx = i
            while s[i] != " " and i >= 0:
                i -= 1
            new_string += s[i + 1:end_idx + 1]

    return new_string








if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; NICE JOB! ***\n")
