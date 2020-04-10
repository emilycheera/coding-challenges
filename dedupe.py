def deduped(items):
    """Return new list from items with duplicates removed.

    >>> deduped([1, 1, 1])
    [1]

    >>> deduped([1, 2, 1, 1, 3])
    [1, 2, 3]

    >>> deduped([1, 2, 3])
    [1, 2, 3]

    >>> a = [1, 2, 3]
    >>> b = deduped(a)
    >>> a == b
    True

    >>> a is b
    False

    >>> deduped([])
    []
    """

    items_seen = set()

    duplicates_removed = []

    for item in items:
        if item not in items_seen:
            items_seen.add(item)
            duplicates_removed.append(item)

    return duplicates_removed


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    