
def reverse_in_place(char_list):
    """Take in a list of characters and reverse the letters in place."""
    
    if len(list_of_chars) == 0:
        return list_of_chars

    middle_index = int(len(list_of_chars) / 2)
    
    for i in range (0, middle_index + 1):
        list_of_chars[i], list_of_chars[-i - 1] = list_of_chars[-i - 1], list_of_chars[i]
    
    return list_of_chars
