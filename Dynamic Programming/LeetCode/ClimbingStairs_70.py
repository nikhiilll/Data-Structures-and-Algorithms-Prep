def climbStairs(n):

    # if n <= 2:
    #     return n

    # stairs = [0 for _ in range(n)]
    # stairs[0] = 1
    # stairs[1] = 2

    # for i in range(2, n):
    #     stairs[i] = stairs[i - 1] + stairs[i - 2]

    # return stairs[-1]
    """
    TC: O(n)
    SC: O(1)
    """
    if n <= 2:
        return n

    a, b = 1, 2

    for i in range(2, n):
        a, b = b, a + b

    return b
