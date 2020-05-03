"""Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings."""


def balanced_string_split(s):
        
    max_strs = 0
    
    r_count = 0
    l_count = 0
    
    for char in s:
        if char == "R":
            r_count += 1
        else:
            l_count += 1
            
        if r_count == l_count:
            max_strs += 1
            r_count = 0
            l_count = 0
            
    return max_strs