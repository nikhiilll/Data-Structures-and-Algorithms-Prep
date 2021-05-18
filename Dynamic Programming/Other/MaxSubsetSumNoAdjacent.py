"""
TC: O(n)
SC: O(1)
"""


def maxSubsetSumNoAdjacent(array):

    dp = [0] * (len(array) + 2)
    for i in range(2, len(dp)):
        dp[i] = max(dp[i - 1], dp[i - 2] + array[i - 2])

    return dp[-1]

    """
    SC: O(1)
    """
    # if not array:
    #     return 0
    # if len(array) == 1:
    #     return array[0]

    # first = array[0]
    # second = max(array[0], array[1])
    # for i in range(2, len(array)):
    #     current = max(first + array[i], second)
    #     first = second
    #     second = current

    # return second
