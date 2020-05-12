def max_number_of_balloons(text):
    
    char_counts = {}
    
    for char in text:
        if char in "balon":
            char_counts[char] = char_counts.get(char, 0) + 1
    
    if char_counts.get("l"):
        char_counts["l"] //= 2
    
    if char_counts.get("o"):
        char_counts["o"] //= 2
    
    if len(char_counts.keys()) == 5:
        return min(char_counts.values())
    
    return 0