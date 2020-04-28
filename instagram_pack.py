
"""Determine number of "instagram" packs needed to make a word.

    >>> instagram_pack("grass")
    2

    >>> instagram_pack("tagging")
    3

    >>> instagram_pack("git")
    1

    >>> instagram_pack("emily")
    -1

    >>> instagram_pack("aaaaa")
    3

"""

from math import ceil

def instagram_pack(word):

    insta_dict = {"i": 1, "n":1, "s":1, "t": 1, "a": 2, "g": 1, "r": 1, "m": 1}

    word_dict = {}
    for char in word:
        word_dict[char] = word_dict.get(char, 0) + 1

    packs_needed = 1

    for char, count in word_dict.items():
        if char not in insta_dict:
            return -1
        packs_needed = max(packs_needed, int(ceil(count/insta_dict[char])))

    return packs_needed


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; NICE JOB! ***\n") 
