def phoneNumberMnemonics(phoneNumber):
    """
    TC: O(4^n * n)
    SC: O(4^n * n)
    """
    keypad = {"0": "0", "1": "1", "2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"], 
    "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}

    currentStrings = [""]

    for num in phoneNumber:
        newStrings = []
        for c in keypad[num]:
            for s in currentStrings:
                newStrings.append(s + c)
        currentStrings = newStrings
    
    return currentStrings