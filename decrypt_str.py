def freq_alphabets(s):
        
    chars = ""
    i = len(s) - 1
        
    while i >= 0:
        if s[i] == "#":
            num = s[i - 2: i]
            chars += chr(int(num) + 96)
            i -= 3
        else:
            chars += chr((int(s[i]) + 96))
            i -= 1
            
    return chars[::-1]