def is_happy(n):
        
    mem = set()
    
    while n != 1:
        num_str = str(n)
        n = 0
        for digit in num_str:
            n += int(digit) ** 2
        if n in mem:
            return False
        mem.add(n)
        
    return True


print("Test 19 -> True")
print(is_happy(19))
print("Test 21 -> False")
print(is_happy(21))