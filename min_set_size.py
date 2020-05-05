"""Given an array arr.  You can choose a set of integers and remove all the 
occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of 
the array are removed.
"""

def min_set_size(arr):
            
    count_dict = {}
    
    for num in arr:
        count_dict[num] = count_dict.get(num, 0) + 1
    
    target_len = len(arr) / 2
    set_len = 0
    min_size_set = 0
    
    counts = sorted(count_dict.values())
    
    while target_len > set_len:
        set_len += counts.pop()
        min_size_set += 1
        
    return min_size_set
        
        