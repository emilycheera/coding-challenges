def number_of_steps (num):
        
    count = 0
    
    while num:
        if num % 2 == 0:
            num /= 2
        else:
            num -= 1
        count += 1
            
    return count
    