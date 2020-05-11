def to_lowercase(str):
        
    lower_str = ""
    
    for s in str:
        if 65 <= ord(s) <= 90:
            lower_str += (chr(ord(s) + 32))
        else:
            lower_str += s
            
    return lower_str
    