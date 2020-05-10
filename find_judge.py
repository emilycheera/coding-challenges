def find_judge(N, trust):
        
    possibilities = [i for i in range(1, N + 1)]
    
    # First find the person that trusts no one
    for pair in trust:
        if pair[0] in possibilities:
            possibilities.remove(pair[0])
    
    # If there's not one person who trusts no one, return -1
    if not possibilities or len(possibilities) > 1:
        return -1
    
    # Then check that everyone else trusts that possible judge
    possible_judge = possibilities[0]
    all_trust = True
    others = [i for i in range(1, N + 1)]
    others.remove(possible_judge)
    for other in others:
        if [other, possible_judge] not in trust:
            all_trust = False
    
    if all_trust == True:
        return possible_judge
    
    return -1