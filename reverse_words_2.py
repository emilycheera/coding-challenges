"""Given a string, reverse the order of characters in each word within a
   sentence while still preserving whitespace and initial word order."""

def reverse_words(s):
            
    return " ".join(word[::-1] for word in s.split())