def moveElementToEnd(array, toMove):
    """
    TC: O(n)
    SC: O(1)
    """
    left = 0
    right = len(array) - 1
    while left < right:
        if array[right] == toMove:
            right -= 1
            continue
        if array[left] == toMove:
            array[left], array[right] = array[right], array[left]
        left += 1
    
    return array