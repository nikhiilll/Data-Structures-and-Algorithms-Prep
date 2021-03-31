def productSum(array, currentDepth = 1):
    """
    TC: O(n)
    SC: O(d)
    """
    currentSum = 0
    for i in range(len(array)):
        if isinstance(array[i], int):
            currentSum += array[i]
        else:
            currentSum += productSum(array[i], currentDepth + 1)
    
    return currentSum * currentDepth