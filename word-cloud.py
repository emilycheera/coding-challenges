import unittest

class WordCloudData(object):

    def __init__(self, input_string):

        # Count the frequency of each word

        self.words_to_counts = {}
        self.populate_words_to_counts(input_string)
        

    def populate_words_to_counts(self, input_string):
            
        current_word_start_index = 0
        current_word_length = 0
            
        for i, char in enumerate(input_string):
            if char.isalpha() or (current_word_length != 0 and (char == "-" or char == "'")):
                if current_word_length == 0:
                    current_word_start_index = i
                current_word_length += 1
            else:
                if current_word_length > 0:
                    word = input_string[current_word_start_index:current_word_start_index + current_word_length]
                    self.add_word_to_dictionary(word)
                current_word_length = 0

        if current_word_length > 0:
            word = input_string[current_word_start_index:current_word_start_index + current_word_length]
            self.add_word_to_dictionary(word)
    

    def add_word_to_dictionary(self, word):

        if self.words_to_counts.get(word):
            self.words_to_counts[word] += 1
            
        elif self.words_to_counts.get(word.lower()):
            self.words_to_counts[word.lower()] += 1
            
        elif self.words_to_counts.get(word.capitalize()):
            del self.words_to_counts[word.capitalize()]
            self.words_to_counts[word.lower()] = 2
            
        else:
            self.words_to_counts[word] = 1



