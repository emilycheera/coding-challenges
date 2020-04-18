"""Write a function that encrypts a string with a variable rotary cipher.

The function should take in a number and string and shift the string's
characters by that number:

>>> rot_encode(1, 'abcxyz')
'bcdyza'

It should be able to shift characters by any number:

>>> rot_encode(3, 'abcxyz')
'defabc'

It should preserve capitalization, whitespace, and any special characters:

>>> rot_encode(1, 'Wow! This is 100% amazing.')
'Xpx! Uijt jt 100% bnbajoh.'
"""


def rot_encode(shift, txt):
    """Encode `txt` by shifting its characters to the right."""

    chars = list(txt)

    for i in range(len(chars)):
        char_val = ord(chars[i])
        if 65 <= char_val <= 90 or 97 <= char_val <= 122:
            new_char_val = char_val + (shift % 26)
            if (char_val <= 90 and new_char_val > 90) or (
                char_val <= 122 and new_char_val > 122
            ):
                new_char_val -= 26
            chars[i] = chr(new_char_val)

    return "".join(chars)


if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n✨ ALL TESTS PASSED!\n")
