def largestRange(array):
    """
    TC: O(n)
    SC: O(n)

    The sorting solution has TC: O(nlogn) | SC: O(1)
    """
    nums = {}
    longestRange = []
    longestLength = 0

    for num in array:
        nums[num] = False
    
    for num in array:
        if nums[num]:
            continue
        nums[num] = True
        currentLength = 0
        left = num - 1
        right = num + 1
        while left in nums:
            currentLength += 1
            nums[left] = True
            left -= 1
        while right in nums:
            currentLength += 1
            nums[right] = True
            right += 1
        if currentLength > longestLength:
            longestLength = currentLength
            longestRange = [left + 1, right - 1]
    
    return longestRange