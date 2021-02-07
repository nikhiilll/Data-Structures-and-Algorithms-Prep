def firstDuplicateValue(array):
    """
    TC: O(n)
    SC: O(n)
    """
    seen = set()
    for num in array:
        if num in seen:
            return num
        seen.add(num)
    
    return -1
    
    """
    TC: O(n)
    SC: O(1)
    """
    for num in array:
        absNum = abs(num)
        if array[absNum - 1] < 0:
            return absNum
        array[absNum - 1] *= (-1)

    return -1