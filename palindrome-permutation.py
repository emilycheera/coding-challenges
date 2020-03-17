def has_palindrome_permutation(the_string):

    # Check if any permutation of the input is a palindrome in O(n) time.
        
    set_of_chars = set()
        
    for char in the_string:
        if char not in set_of_chars:
            set_of_chars.add(char)
        else:
            set_of_chars.remove(char)
            
    if len(set_of_chars) <= 1:
        return True

    return False