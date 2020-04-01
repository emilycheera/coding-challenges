
def find_largest_smaller_than(nums, xnumber):
    """Given an ordered list of numbers and a number, return the index of the 
    largest number in the list that is smaller than that number."""
    
    if nums[0] > xnumber:
        return None
    
    if nums[-1] < xnumber:
        return len(nums) - 1
    
    for i in range(len(nums) - 1):
        if nums[i + 1] >= xnumber:
            return i




print("test [-3, 2, 8, 14, 29], 8 -> 1")
print(find_largest_smaller_than([-3, 2, 8, 14, 29], 8))
print("test [3, 4, 5, 6], 2 -> None")
print(find_largest_smaller_than([3, 4, 5, 6], 2))
print("test [4, 6, 9, 23, 44], 90 -> 4")
print(find_largest_smaller_than([4, 6, 9, 23, 44], 90))