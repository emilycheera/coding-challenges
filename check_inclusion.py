"""Given two strings s1 and s2, write a function to return true if s2 contains 
   the permutation of s1."""

def check_inclusion(s1, s2):
        
    s1 = sorted(s1)
    
    for i in range(len(s2) - len(s1) + 1):
        curr_str = sorted(s2[i:i + len(s1)])
        if s1 == curr_str:
            return True
    
    return False
        