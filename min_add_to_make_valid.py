def min_add_to_make_valid(S):
        
    to_add = 0
    
    parens_stack = []
    
    for paren in S:
        if paren == "(":
            parens_stack.append(paren)
            
        else:
            if parens_stack:
                parens_stack.pop()
            else:
                to_add += 1
                
    to_add += len(parens_stack)
    
    return to_add
        