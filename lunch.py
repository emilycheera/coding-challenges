"""Leveret lunch count.

Check that garden is valid::

    >>> garden = [
    ...     [1, 1],
    ...     [1],
    ... ]

    >>> lunch_count(garden)
    Traceback (most recent call last):
    ...
    AssertionError: Garden not a matrix!

    >>> garden = [
    ...     [1, 1],
    ...     [1, 'a'],
    ... ]

    >>> lunch_count(garden)
    Traceback (most recent call last):
    ...
    AssertionError: Garden values must be ints!

Consider simple cases::

    >>> garden = [
    ...     [0, 0, 0],
    ...     [0, 0, 0],
    ...     [0, 0, 0]
    ... ]

    >>> lunch_count(garden)
    0

    >>> garden = [
    ...     [1, 1, 1],
    ...     [0, 1, 1],
    ...     [9, 1, 9]
    ... ]

    >>> lunch_count(garden)
    3

    >>> garden = [
    ...     [1, 1, 1],
    ...     [1, 1, 1],
    ...     [1, 1, 1]
    ... ]

    >>> lunch_count(garden)
    9

Make sure it works with even-sides
(this will start with the 4 and head east)::

    >>> garden = [
    ...     [9, 9, 9, 9],
    ...     [9, 3, 1, 0],
    ...     [9, 1, 4, 2],
    ...     [9, 9, 1, 0],
    ... ]

    >>> lunch_count(garden)
    6

Consider our most complex case::

    >>> garden = [
    ...     [2, 3, 1, 4, 2, 2, 3],
    ...     [2, 3, 0, 4, 0, 3, 0],
    ...     [1, 7, 0, 2, 1, 2, 3],
    ...     [9, 3, 0, 4, 2, 0, 3],
    ... ]

    >>> lunch_count(garden)
    15

"""


def lunch_count(garden):
    """Given a garden of nrows of ncols, return carrots eaten."""

    # Sanity check that garden is valid

    row_lens = [len(row) for row in garden]
    assert min(row_lens) == max(row_lens), "Garden not a matrix!"
    assert all(all(type(c) is int for c in row) for row in garden), \
        "Garden values must be ints!"

    nrows = len(garden)
    ncols = len(garden[0])

    # Get starting cell options
    starting_options = [((nrows - 0) // 2, (ncols - 0) // 2),
                        ((nrows - 1) // 2, (ncols - 0) // 2),
                        ((nrows - 0) // 2, (ncols - 1) // 2),
                        ((nrows - 1) // 2, (ncols - 1) // 2)]

    # Find starting cell from options
    starting_cell = None
    current_carrots = -1

    for i, j in starting_options:
        if garden[i][j] > current_carrots:
            current_carrots = garden[i][j]
            starting_cell = (i, j)

    i, j = starting_cell
    garden[i][j] = 0
    carrot_tally = current_carrots

    while current_carrots != 0:
        legal_cells = get_legal_cells(garden, i, j, ncols, nrows)
        next_cell = move_to_next_cell(garden, legal_cells)
        i, j = next_cell
        current_carrots = garden[i][j]
        garden[i][j] = 0
        carrot_tally += current_carrots

    return carrot_tally


# Get adjacent cells
def get_legal_cells(garden, i, j, ncols, nrows):
    
    cell_options = [(i, j - 1), (i - 1, j), (i, j + 1), (i + 1, j)]
    legal_cells = []

    for i, j in cell_options:
        if 0 <= i < nrows and 0 <= j < ncols:
            legal_cells.append((i, j))

    return legal_cells


# Move to adjacent cell that has most carrots
def move_to_next_cell(garden, legal_cells):
    carrot_count = -1
    next_cell = None

    for i, j in legal_cells:
        if garden[i][j] > carrot_count:
            carrot_count = garden[i][j]
            next_cell = (i, j)

    return next_cell


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASS! HOP ALONG NOW!\n")
