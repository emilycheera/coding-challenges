"""Given a string s and a non-empty string p, find all the start indices of p's 
   anagrams in s."""

def find_anagrams(s, p):
        
    start_indices = []
    
    p_chars = sorted(p)
        
    for i in range(len(s) - len(p) + 1):
        s_chars = sorted(s[i:i + len(p)])
        if s_chars == p_chars:
            start_indices.append(i)
            
    return start_indices 