def group_anagrams(strs):

    anagram_dict = {}

    for word in strs:
        key = tuple(sorted(word))
        anagram_dict[key] = anagram_dict.get(key, []) + [word]
        
    return list(anagram_dict.values())


print("""test ["eat", "tea", "tan", "ate", "nat", "bat"] ->
     [["ate","eat","tea"], ["nat","tan"], ["bat"]]""")
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))