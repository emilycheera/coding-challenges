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
    word_list.reverse()
    
    while word_list:

        if len(word_list) == 1:
            print(word_list[-1])
            break

        else:
            current_line = word_list[-1]
            current_line_length = len(current_line)
            word_list.pop()

            while current_line_length + len(word_list[-1]) + 1 <= char_limit:
                current_line += f" {word_list.pop()}"
                if len(word_list) == 0:
                 break
            
            print(current_line)








