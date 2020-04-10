def recursive_index(needle, haystack):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.
    
    >>> recursive_index("hey", ["hey", "there", "you"])
    0

    >>> recursive_index("you", ["hey", "there", "you"])
    2

    >>> recursive_index("porcupine", ["hey", "there", "you"]) is None
    True
    """

    def _recursive_index(needle, haystack, idx):

        if idx == len(haystack):
            return None

        if haystack[idx] == needle:
            return idx

        return _recursive_index(needle, haystack, idx + 1)

    return _recursive_index(needle, haystack, 0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
