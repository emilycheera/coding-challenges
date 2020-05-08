def check_straight_line(coordinates):
        
    if len(coordinates) < 3:
        return True
    
    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]
    
    if (x2 - x1) == 0:
        slope = "undefined"
        
    else:
        slope = (y2 - y1) / (x2 - x1)
    
    for i in range(2, len(coordinates)):
        x, y = coordinates[i]
        
        if (x - x1) == 0:
            if slope != "undefined":
                return False
        
        else:
            if (y - y1) / (x - x1) != slope:
                return False
        
    return True