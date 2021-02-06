def smallestDifference(arrayOne, arrayTwo):
    """
    TC: O(nlogn + mlogm)
    SC: O(1)
    """
    arrayTwo.sort()
    result = []
    minDiff = float("inf")

    for num in arrayOne:
        low = 0
        high = len(arrayTwo) - 1
        mid = 0
        while low <= high:
            mid = (low + high) // 2
            if abs(arrayTwo[mid] - num) < minDiff:
                minDiff = abs(arrayTwo[mid] - num)
                result = [num, arrayTwo[mid]]
            if arrayTwo[mid] < num:
                low = mid + 1
            elif arrayTwo[mid] > num:
                high = mid - 1
            else:
                return result
    
    return result