"""Given num_people in circle, kill [kill_every]th person, return survivor.

    >>> find_survivor(4, 2)
    1

    >>> find_survivor(41, 3)
    31

As a sanity case, if never skip anyone, the last person will be our survivor:

    >>> find_survivor(10, 1)
    10

"""



def find_survivor(num_people, kill_every):
    """Given num_people in circle, kill [kill_every]th person, return survivor."""

    people = list(range(1, num_people + 1))

    start_idx = 0

    while len(people) > 1:
        idx_to_remove = ((start_idx + kill_every - 1) % len(people))
        people.pop(idx_to_remove)
        start_idx = idx_to_remove

    return people[0]



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. W00T!\n")
