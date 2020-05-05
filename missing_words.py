def missing_words(s1, s2):
    """Quadratic solution."""

    s1_words = s1.split()
    s2_words = s2.split()

    missing_words = []

    for word in s1_words:
        if word not in s2_words:
            missing_words.append(word)

    return missing_words


def missing_words_2(s1, s2):
    """Linear solution"""

    s1_words = s1.split()
    s2_words = s2.split()

    missing_words = []

    i = j = 0

    while i < len(s1_words) and j < len(s2_words):
        if s1_words[i] == s2_words[j]:
            j += 1
        else:
            missing_words.append(s1_words[i])
        i += 1

    missing_words.extend(s1_words[i:])

    return missing_words


print("test 'I like cheese', 'like' -> ['I', 'cheese']")
print(missing_words_2("I like cheese", "like"))

print("test 'I am using HackerRank to improve programming',\
    'am HackerRank to improve' -> ['I', 'using', 'programming']")
print(missing_words_2("I am using HackerRank to improve programming", "am HackerRank to improve"))
