def product_except_self(nums):
    
    product_before = 1
    products_after = [1]
    
    for i in range(len(nums) - 1, 0, -1):
        products_after.append(products_after[-1] * nums[i])
        
    for i in range(len(nums)):
        temp = nums[i]
        nums[i] = product_before * products_after.pop()
        product_before *= temp
    
    return nums
    