def unique_morse_representations(words):
        
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    
    res = set()
    
    for w in words:
        m = []
        for c in w:
            m.append(morse[ord(c) - 97])
        res.add("".join(m))
            
    return len(res)