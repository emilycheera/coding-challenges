"""Given two strings: s1 and s2 with the same size, check if some permutation 
of string s1 can break some permutation of string s2 or vice-versa.

A string x can break string y (both of size n) if x[i] >= y[i] for all i between 
0 and n-1.
"""

def check_if_can_break(s1, s2):
        
    s1 = sorted(s1)
    s2 = sorted(s2)
    
    gt = lt = 0
    
    for i in range(len(s1)):
        if s1[i] <= s2[i]:
            lt += 1
        if s1[i] >= s2[i]:
            gt += 1
            
    return gt == len(s1) or lt == len(s1)
        
    