def backspace_compare(S, T):
        
    def build_str(string):
        final_str = []
        for char in string:
            if char != "#":
                final_str.append(char)
            else:
                if final_str:
                    final_str.pop()
    
        return final_str
    
    return build_str(S) == build_str(T)

print("test S = 'ab##', T = 'c#d#' -> True")
print(backspace_compare("ab##", "c#d#"))