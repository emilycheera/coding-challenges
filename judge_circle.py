"""There is a robot starting at position (0, 0), the origin, on a 2D plane.
   Given a sequence of its moves, judge if this robot ends up at (0, 0) after 
   it completes its moves."""

def judge_circle(moves):
    
    x = y = 0
    
    for move in moves:
        if move == "R":
            x += 1
        elif move == "L":
            x -= 1
        elif move == "U":
            y += 1
        else:
            y -= 1
            
    return x == y == 0