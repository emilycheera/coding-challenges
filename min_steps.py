"""Given two equal-size strings s and t. Return the minimum number of steps to 
   make t an anagram of s."""

def min_steps(s, t):
        
    s_counts = {}
    steps = 0
    
    for char in s:
        s_counts[char] = s_counts.get(char, 0) + 1
        
    for char in t:
        if s_counts.get(char):
            s_counts[char] -= 1
        else:
            steps += 1
            
    return steps