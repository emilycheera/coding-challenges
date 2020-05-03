def can_construct(ransom_note, magazine):
        
    # Make dictionary of magazine letter counts
    mag_letters = {}
    for letter in magazine:
        mag_letters[letter] = mag_letters.get(letter, 0) + 1
    
    for letter in ransom_note:
        # If letter not in magazine or count is zero, return false
        if mag_letters.get(letter, 0) == 0: # If key not found, .get returns 0
            return False
        
        else:
            mag_letters[letter] -= 1

    # All ransom note letters found in magazine, so return true
    return True 
    