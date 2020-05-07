"""Given the array nums, for each nums[i] find out how many numbers in the 
array are smaller than it. That is, for each nums[i] you have to count the 
number of valid j's such that j != i and nums[j] < nums[i]. Return the answer 
in an array."""

def smallerNumbersThanCurrent(nums):
        
    nums_sorted = sorted(nums)
    
    for i, num in enumerate(nums):
        nums[i] = nums_sorted.index(num)
        
    return nums
    