
def remove_anagrams(word_list):

    sorted_words = set()
    result_list = []

    for word in word_list:
        if "".join(sorted(word)) not in sorted_words:
            result_list.append(word)
            sorted_words.add("".join(sorted(word)))

    return result_list

print(remove_anagrams(["code", "deco", "silent", "listen", "list"]))
