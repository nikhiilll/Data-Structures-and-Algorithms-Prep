def stockBuySell(A, n):

    result = []
    minIdx = 0
    currentPair = []
    for i in range(1, n):
        if A[i] <= A[minIdx]:
            minIdx = i
            if currentPair:
                result.append(currentPair)
        else:
            currentPair = [minIdx, i]
                    
                    
    result.append(currentPair)
    return result