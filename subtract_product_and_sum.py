def subtract_product_and_sum(n):
        
    digits = []
    
    while n > 0:
        digits.append(n % 10)
        n //= 10
        
    product = 1
    for digit in digits:
        product *= digit
        
    return product - sum(digits)
        