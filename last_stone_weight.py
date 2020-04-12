def last_stone_weight(stones):
        
    while len(stones) > 1:
        stones.sort()
        y = stones.pop()
        x = stones.pop()
        if x < y:
            stones.append(y-x)
            
    return stones[0] if stones else 0