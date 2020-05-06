"""Given the number k, return the minimum number of Fibonacci numbers whose 
sum is equal to k."""

def findMinFibonacciNumbers(k):
        
    fibs = [1, 1]
    x = 1
    
    while x < k:
        x = fibs[-1] + fibs[-2]
        if x <= k:
            fibs.append(x)
            
    count = 0
    current_sum = k
    
    for i in range(len(fibs) - 1, -1, -1):
        if fibs[i] <= current_sum:
            current_sum -= fibs[i]
            count += 1
    
    return count
    