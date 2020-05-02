def base_to_binary(base, num):
    
    digits = "0123456789ABCDEF"
    rem_stack = []

    while num > 0:
        rem = num % base
        rem_stack.append(rem)
        num = num // base

    result = ""
    while rem_stack:
        result += digits[rem_stack.pop()]

    return result


print("test 16, 43 -> 2B")
print(base_to_binary(16, 43))
