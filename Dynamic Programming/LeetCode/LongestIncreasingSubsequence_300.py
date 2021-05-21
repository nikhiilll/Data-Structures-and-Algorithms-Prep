"""
TC: O(n ^ 2)
SC: O(n)
"""


def lengthOfLIS(nums):

    if len(nums) <= 1:
        return len(nums)

    lisArray = [0 for _ in nums]
    lisArray[0] = 0
    maxLength = 0
    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[i] > nums[j]:
                lisArray[i] = max(lisArray[i], lisArray[j] + 1)
        maxLength = max(maxLength, lisArray[i])

    return maxLength + 1
