def commonChars(A):

    charFreq = [float('inf')] * 26
    print (charFreq)

    result = []

    for value in A:

        charFreqValue = [0] * 26

        for c in value:
            charFreqValue[ord(c) - ord('a')] += 1

        for i in range(26):
            charFreq[i] = min(charFreq[i], charFreqValue[i])
        
    for index, frequency in enumerate(charFreq):

        while frequency > 0:
            result.append(chr(index + ord('a')))
    
    return result

A = ["bella","label","roller"]
print(commonChars(A))