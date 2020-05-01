"""Find the most frequent num(s) in nums.

Return the set of nums that are the mode::

    >>> mode([1]) == {1}
    True

    >>> mode([1, 2, 2, 2]) == {2}
    True

If there is a tie, return all::

    >>> mode([1, 1, 2, 2]) == {1, 2}
    True
"""


def mode(nums):
    """Find the most frequent num(s) in nums."""

    modes = set()
    dict_count = {}

    for num in nums:
        dict_count[num] = dict_count.get(num, 0) + 1

    max_count = max(dict_count.values())

    for num in dict_count:
        if dict_count[num] == max_count:
            modes.add(num)

    return modes


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. HOORAY!\n")
