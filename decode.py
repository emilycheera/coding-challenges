def decode(s):
    
    i = 0
    decoded_str = ""
    
    while i < len(s):
        num = int(s[i])
        j = i + num + 1
        decoded_str += s[j]
        i = (j + 1)
        
    return decoded_str
    
    





print("test 0h1ae2bcy -> hey")
print(decode("0h1ae2bcy"))
print("test 0h -> h")
print(decode("0h"))
