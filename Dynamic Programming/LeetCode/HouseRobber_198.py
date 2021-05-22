"""
TC: O(n)
SC: O(n)
"""


def rob(nums):

    robbery = [0 for _ in range(len(nums) + 1)]
    robbery[1] = nums[0]

    for i in range(2, len(nums) + 1):
        robbery[i] = max(robbery[i - 1], robbery[i - 2] + nums[i - 1])

    return robbery[-1]
