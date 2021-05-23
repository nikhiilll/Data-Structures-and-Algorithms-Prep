"""
TC: O(m * n)
SC: O(n)
"""


def uniquePaths(m, n):

    # grid = [[1 for _ in range(n)] for _ in range(m)]
    # for i in range(m):
    #     grid[i][0] = 1

    # for i in range(1, m):
    #     for j in range(1, n):
    #         grid[i][j] = grid[i][j - 1] + grid[i - 1][j]

    # return grid[-1][-1]

    even = [1 for _ in range(n)]
    odd = [1 for _ in range(n)]

    for i in range(1, m):
        if i % 2 == 0:
            current = even
            previous = odd
        else:
            current = odd
            previous = even
        for j in range(1, n):
            current[j] = current[j - 1] + previous[j]

    return even[-1] if m % 2 != 0 else odd[-1]


print(uniquePaths(3, 7))
