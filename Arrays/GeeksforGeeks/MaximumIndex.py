def maxIndexDiff(arr, n):
    """
    TC: O(n)
    SC: O(n)
    """
    leftMin = [0] * n
    rightMax = [0] * n
    leftMin[0], rightMax[n - 1] = arr[0], arr[n - 1]
    for i in range(1, n):
        leftMin[i] = min(leftMin[i - 1], arr[i])
    for i in range(n - 2, -1, -1):
        rightMax[i] = max(rightMax[i + 1], arr[i])
    
    i, j = 0, 0
    maxDiff = float("-inf")
    while i < n and j < n:
        if leftMin[i] < rightMax[j]:
            maxDiff = max(maxDiff, j - i)
            j += 1
        else:
            i += 1
    
    return maxDiff