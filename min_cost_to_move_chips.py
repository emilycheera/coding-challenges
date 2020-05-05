def minCostToMoveChips(chips):
    """Return min cost needed to move all the chips to the same position.
    
    Position = chips[i].
    Moving by 2-units costs 0. Moving by 1-unit costs 1.
    """
        
    evens = 0
    odds = 0
    
    for pos in chips:
        if pos % 2 == 0:
            evens += 1
        else:
            odds += 1
    
    return min(evens, odds)
    