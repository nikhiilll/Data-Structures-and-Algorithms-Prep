def missingNumber(arr, N):
    """
    TC: O(k), where k is the missing positive number
    SC: O(N)
    """
    elements = set(arr)
    missingNumber = 1

    while True:
        if missingNumber in elements:
            missingNumber += 1
            continue
        break

    return missingNumber