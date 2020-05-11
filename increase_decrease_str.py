def sort_string(s):
        
    char_dict = {}
    for char in s:
        char_dict[char] = char_dict.get(char, 0) + 1
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    res = ""
    
    while set(char_dict.values()) != {0}:
        for char in alphabet:
            if char_dict.get(char):
                res += char
                char_dict[char] -= 1
        
        for char in alphabet[::-1]:
            if char_dict.get(char):
                res += char
                char_dict[char] -= 1
                
    return res
        