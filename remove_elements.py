def remove_elements(nums, val):
    
    left_idx = 0
    right_idx = 1
    
    while right_idx < len(nums):
        if nums[left_idx] == val and nums[right_idx] != val:
            nums[left_idx], nums[right_idx] = nums[right_idx], nums[left_idx]
            left_idx += 1
        elif nums[left_idx] != val:
            left_idx += 1
        right_idx += 1
            
    length = 0
    
    for num in nums:
        if num == val:
            break
        length += 1
        
    return length