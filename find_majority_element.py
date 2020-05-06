def majority_element(nums):
    """Given an array of size n, find the majority element."""
        
    set_nums = set(nums)
    
    for num in set_nums:
        if nums.count(num) > len(nums) / 2:
            return num
       
    