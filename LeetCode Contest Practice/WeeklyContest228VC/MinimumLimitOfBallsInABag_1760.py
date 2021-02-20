def minimumSize(nums, maxOperations):
    """
    TC: O(nlog(maxN))
    SC: O(1)
    """
    left, right = 1, max(nums)

    while left < right:
        mid = (left + right) // 2
        if sum((num - 1) // mid for num in nums) > maxOperations:
            left = mid + 1
        else:
            right = mid

    return left