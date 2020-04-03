max_sublist(nums):
    
    current = 0
    result = nums[0]
    
    for num in nums:
        current += num
        result = max(current,result)
        current = max(0,current)
        
    return result