"""Given an array of ints, return count that have an even number of digits."""

def find_numbers(nums):
        
    even_digits = 0
    
    for num in nums:
        num_digits = 0
        while num > 0:
            num //= 10
            num_digits += 1
        
        if num_digits % 2 == 0:
            even_digits += 1
            
    return even_digits