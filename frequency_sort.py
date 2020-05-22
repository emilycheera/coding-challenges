from collections import Counter
    
def frequency_sort(s):
    """Sort string in decreasing order based on the frequency of characters."""

    char_counts = Counter(s)
    counts = sorted(set(char_counts.values()), reverse=True)
    
    result = ""
    
    for count in counts:
        for char in char_counts:
            if char_counts[char] == count:
                result += (char * count)
                
    return result