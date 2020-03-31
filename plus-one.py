def plus_one(digits):
        
    idx = len(digits) - 1
    nine_counter = 0
    
    while idx >= 0:
        if digits[idx] < 9:
            digits[idx] += 1
            if nine_counter > 0:
                for i in range(-nine_counter, 0):
                    digits[i] = 0
            return digits
        else:
            nine_counter += 1
            idx -= 1
    
    # Handle case if all digits were 9
    digits.insert(0, 1)
    for i in range(-nine_counter, 0):
        digits[i] = 0
    
    return digits