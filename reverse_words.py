def reverse_words(message):

    # Decode the message by reversing the words
    
    message = reverse_chars(message, 0, len(message) - 1)

    first_index = 0

    for i, char in enumerate(message):
        
        if char == " ":
            last_index = i - 1
            message = reverse_chars(message, first_index, last_index)
            first_index = last_index + 2
        
        if i == len(message) - 1:
            message = reverse_chars(message, first_index, len(message) -1)
            
    return message


def reverse_chars(message, left_index, right_index):
        
        while left_index < right_index:
            message[left_index], message[right_index] = message[right_index], message[left_index]
            
            left_index += 1
            right_index -= 1
            
        return message