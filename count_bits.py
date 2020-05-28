def count_bits(num):
    """For all integers from 0 to num, count 1s in its binary representation."""
        
    result = []
    
    for i in range(num + 1):
        result.append(bin(i).count("1"))
    
    return result