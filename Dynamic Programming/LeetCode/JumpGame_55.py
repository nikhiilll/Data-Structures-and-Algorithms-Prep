"""
TC: O(n)
SC: O(1)
"""


def canJump(nums):

    maxJump = 0

    for i in range(len(nums)):
        if i > maxJump:
            return False
        maxJump = max(maxJump, i + nums[i])

    return True


print(canJump([3, 2, 1, 0, 4]))
