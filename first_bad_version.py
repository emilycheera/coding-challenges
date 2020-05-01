def firstBadVersion(self, n):
        
    start = 1
    end = n
            
    while start <= end:
        guess = ((end - start) // 2) + start
        if isBadVersion(guess) == True:
            if guess == 1 or isBadVersion(guess - 1) == False:
                return guess
            else:
                end = guess - 1
        else:
            start = guess + 1
            