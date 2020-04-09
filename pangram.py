
def is_pangram(sentence):
    """Given a string, return True if it is a pangram, False otherwise.
    
    >>> is_pangram("The quick brown fox jumps over the lazy dog!")
    True

    >>> is_pangram("I like cats, but not mice")
    False

    """

    sentence_set = {char.lower() for char in sentence if char.isalpha()}

    return len(sentence_set) == 26


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; GREAT JOB!\n")