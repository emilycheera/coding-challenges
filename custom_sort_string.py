
def custom_sort_string(S, T):
    """Permute the letters of T so that they match the sorted order of S."""
    
    new_T = ""
    
    for char in S:
        if char in T:
            for _ in range(T.count(char)):
                new_T += char
            
    for char in T:
        if char not in S:
            new_T += char
            
    return new_T
        
    