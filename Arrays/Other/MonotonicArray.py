def isMonotonic(array):
    """
    TC: O(n)
    SC: O(1)
    """
    if len(array) <= 2:
        return True
    
    isIncreasing = True
    isDecreasing = True

    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            isIncreasing = False
        if array[i] < array[i + 1]:
            isDecreasing = False
    
    return isIncreasing or isDecreasing
    