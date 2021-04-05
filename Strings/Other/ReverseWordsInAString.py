def reverseWordsInString(string):
    """
    TC: O(n)
    SC: O(1)
    """
    finalString = currentWord = ""
    n = len(string)
    i = 0

    while i < n:
        if string[i] == " ":
            finalString = currentWord + finalString
            while i < n and string[i] == " ":
                finalString = " " + finalString
                i += 1
            currentWord = ""
        else:
            currentWord += string[i]
            i += 1
    
    finalString = currentWord + finalString
    return finalString