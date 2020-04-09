def pig_latin(phrase):
    """Turn a phrase into pig latin.

    There will be no uppercase letters or punctuation in the phrase.

        >>> pig_latin('hello awesome programmer')
        'ellohay awesomeyay rogrammerpay'
    """

    vowels = set("aeiou")

    words = phrase.split(" ")

    for i, word in enumerate(words):
        if word[0] in vowels:
            words[i] = word + "yay"
        else:
            words[i] = word[1:] + word[0] + "ay"

    return " ".join(words)\



if __name__ == "__main__":
    import doctest
    doctest.testmod()
