def num_special_equiv_groups(A):
        
    equiv_strings = set()
        
    for s in A:
        letters = (str(sorted(s[::2])), str(sorted(s[1::2])))            
        equiv_strings.add(letters)
    
    return len(equiv_strings)