from collections import defaultdict

def generateDocument(characters, document):
    """
    TC: O(n + m)
    SC: O(n)
    """
    if len(document) > len(characters):
        return False
    
    freqChars = defaultdict(int)
    for char in characters:
        freqChars[char] += 1
    
    for c in document:
        if freqChars[c] == 0:
            return False
        freqChars[c] -= 1
    
    return True