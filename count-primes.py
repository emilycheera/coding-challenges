def primes(count):
    """Return count number of prime numbers, starting at 2.
    
    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]

    >>> primes(15)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

    """

    prime_nums = [2]
    prime = 3

    for i in range(1, count):

        while prime not in [3, 5, 7] and (
            prime % 3 == 0 or prime % 5 == 0 or prime % 7 == 0
        ):
            prime += 2

        prime_nums.append(prime)
        prime += 2

    return prime_nums


if __name__ == "__main__":
    import doctest

    doctest.testmod()
