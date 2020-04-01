def compress_string(s):
    
    comp_str = ''
    letter_count = 0
    current_char = s[0]
    
    for char in s:
        if char == current_char:
            letter_count += 1
        else:
            comp_str += (current_char + str(letter_count))
            current_char = char
            letter_count = 1
    
    comp_str += (current_char + str(letter_count))
            
    return min(comp_str, s, key=len)



print("test 'aabbaabb' -> 'a2b2a2b2'")
print(compress_string('aabbaabb'))
print("test 'abc' -> 'abc'")
print(compress_string('abc'))