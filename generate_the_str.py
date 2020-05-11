def generateTheString(n):

    """Given an integer n, return a string with n characters such that each 
       character in such string occurs an odd number of times."""
        
    if n % 2 == 0:
        return "a" * (n - 1) + "b"
    
    else:
        return "a" * n
    