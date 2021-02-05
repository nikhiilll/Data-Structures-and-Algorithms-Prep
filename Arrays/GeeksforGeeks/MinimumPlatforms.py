def minimumPlatform(n, arr, dep):
    """
    TC: O(nlogn)
    SC: O(1)
    """
    arr.sort()
    dep.sort()
    result, currentPF = 0, 0
    i, j = 0, 0

    while i < n and j < n:

        if arr[i] <= dep[j]:
            currentPF += 1
            i += 1
        else:
            currentPF -= 1
            j += 1
        result = max(result, currentPF)
    
    return result