"""Given a list of words, return the word with the most anagrams.

For a list of ['act', 'cat', 'bill']:
- 'act' and 'cat' are anagrams, so they both have 2 matching words.
- 'bill' has no anagrams, so it has one matching word (itself).

Given that 'act' is the first instance of the most-anagrammed word,
we return that.

    >>> find_most_anagrams_from_wordlist(['act', 'cat', 'bill'])
    'act'

Let's use a file of words where each line is a word:
    >>> import os, sys
    >>> all_words = [w.strip() for w in open(os.path.join(sys.path[0],'words.txt'))]
    >>> find_most_anagrams_from_wordlist(all_words)
    'angor'

"""


def find_most_anagrams_from_wordlist(wordlist):
    """Given list of words, return the word with the most anagrams."""

    d = make_dict_of_words(wordlist)

    highest_count = 0
    most_anagrammed_word = ""

    for words in d.values():
        if len(words) > highest_count:
            highest_count = len(words)
            most_anagrammed_word = words[0]

    return most_anagrammed_word


def make_dict_of_words(words):

    d = {}

    for w in words:
        w_sort = "".join(sorted(w))
        d[w_sort] = d.get(w_sort, []) + [w]

    return d


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")
