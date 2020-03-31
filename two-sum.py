def two_sum(nums, target):
    """Given an array of integers, return indices of the two numbers such 
    that they add up to a specific target.

    Assume that each input has exactly one solution. Do not use the same 
    element twice.
    """
        
    nums_dict = {}
    
    for i, num in enumerate(nums):
        nums_dict[num] = i
        
    for i, num in enumerate(nums):
        if nums_dict.get(target-num, None) and nums_dict.get(target-num) != i:
            return [i, nums_dict.get(target-num)]
        