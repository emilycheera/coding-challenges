"""You are given a string s containing lowercase English letters, and a matrix 
shift, where shift[i] = [direction, amount]:

- direction can be 0 (for left shift) or 1 (for right shift). 
- amount is the amount by which string s is to be shifted.

A left shift by 1 means remove the first character of s and append it to the end.

Similarly, a right shift by 1 means remove the last character of s and add it to
the beginning.

Return the final string after all operations."""



def stringShift(s, shift):
    
    chars = [char for char in s]
    
    for direction, amount in shift:
        if direction == 0:
            for _ in range(amount):
                chars.append(chars.pop(0))
        else:
            for _ in range(amount):
                chars.insert(0, chars.pop())
    
    return "".join(chars)