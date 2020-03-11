"""Write a function that takes in a string and a character limit 
(as an integer). It should print the contents of the string without 
going over the character limit and without breaking words. 

For example:

>>> fit_to_width('Hello, world! I love Python and Hackbright', 10)
Hello,
world! I
love
Python and
Hackbright"""


def fit_to_width(str, char_limit):
    """Print contents of string without going over limit or breaking words."""

    word_list = str.split(" ")
    
    while word_list:

        if len(word_list) == 1:
            print(word_list[0])
            break

        else:
            current_line = word_list[0]
            current_line_length = len(current_line)
            word_list.pop(0)

            while current_line_length + len(word_list[0]) + 1 <= char_limit:
                current_line += f" {word_list[0]}"
                word_list.pop(0)
                if len(word_list) == 0:
                 break
            
            print(current_line)







