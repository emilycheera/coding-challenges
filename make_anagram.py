def make_anagram(a, b):

    char_counts = {}
    del_count = 0

    for char in a:
        char_counts[char] = char_counts.get(char, 0) + 1

    for char in b:
        if char_counts.get(char):
            char_counts[char] -= 1
        else:
            del_count += 1

    for val in char_counts.values():
        del_count += abs(val)

    return del_count
