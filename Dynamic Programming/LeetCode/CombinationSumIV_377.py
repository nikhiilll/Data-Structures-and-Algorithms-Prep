"""
TC: O(n * m)
SC: O(n)
"""


def combinationSum4(nums, target):

    ways = [0 for _ in range(target + 1)]
    ways[0] = 1

    for i in range(target + 1):
        for num in nums:
            if num <= i:
                ways[i] += ways[i - num]

    return ways[-1]
