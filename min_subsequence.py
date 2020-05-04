"""Given the array nums, obtain a subsequence of the array whose sum of 
elements is strictly greater than the sum of the non included elements 
in such subsequence. """

def min_subsequence(nums):

    nums.sort()

    threshold = sum(nums) / 2
    result = []
    result_sum = 0
    
    while result_sum <= threshold:
        largest = nums.pop()
        result.append(largest)
        result_sum += largest
        
    return result
    