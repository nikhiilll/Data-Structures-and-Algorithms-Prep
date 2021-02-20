def minOperations(s):
    """
    TC: O(n)
    SC: O(1)
    """
    startZero = 0
    startOne = 0
        
    for i in range(0, len(s), 2):
        if s[i] != "0":
            startZero += 1
        if s[i] != "1":
            startOne += 1
        
    for i in range(1, len(s), 2):
        if s[i] != "0":
            startOne += 1
        if s[i] != "1":
            startZero += 1
    
    return min(startZero, startOne)