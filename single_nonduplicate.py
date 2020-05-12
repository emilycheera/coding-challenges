def single_nonduplicate(nums):
                
    if len(nums) == 1:
        return nums[0]
    
    floor = 0
    ceiling = len(nums) - 1
    
    while floor <= ceiling:
        mid = ((ceiling - floor) // 2) + floor
        if mid == 0:
            if nums[mid + 1] != nums[mid]:
                return nums[mid]
        if mid == len(nums) - 1:
            if nums[mid - 1] != nums[mid]:
                return nums[mid]
        if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
            return nums[mid]
        
        if nums[mid] == nums[mid + 1]:
            if mid % 2 == 1:
                ceiling = mid - 1
            else:
                floor = mid + 1
            
        elif nums[mid] == nums[mid - 1]:
            if mid % 2 == 1:
                floor = mid + 1
            else:
                ceiling = mid - 1
            