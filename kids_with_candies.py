"""For each kid check if there is a way to distribute extraCandies among the 
kids such that he or she can have the greatest number of candies among them."""

def kids_with_candies(candies):
        
    most = max(candies)
    
    for i, kid in enumerate(candies):
        candies[i] = True if kid + extraCandies >= most else False
    
    return candies