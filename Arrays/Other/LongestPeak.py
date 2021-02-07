def longestPeak(array):
    """
    TC: O(n)
    SC: O(1)
    """
    length = 1
    maxLength = float("-inf")
    i = 1

    while i < len(array) - 1:
        if array[i - 1] < array[i]:
            length += 1
        
        if array[i - 1] < array[i] > array[i + 1]:
            while i < len(array) - 1 and array[i] > array[i + 1]:
                length += 1
                i += 1
            maxLength = max(maxLength, length)
            length = 1
        
        i += 1
    
    return maxLength

print(longestPeak([5, 4, 3, 2, 1, 2, 10, 12, -3, 5, 6, 7, 10]))