"""
TC: O(w * h)
SC: O(w * h)
"""


def numberOfWaysToTraverseGraph(width, height):

    grid = [[1 for _ in range(width)] for _ in range(height)]
    for h in range(height):
        grid[h][0] = 1

    for w in range(1, width):
        for h in range(1, height):
            grid[h][w] = grid[h - 1][w] + grid[h][w - 1]

    return grid[-1][-1]


def numberOfWaysToTraverseGraph2(width, height):

    odd = [1 for _ in range(width)]
    even = [1 for _ in range(width)]

    for i in range(1, height):
        if i % 2 == 0:
            current = even
            previous = odd
        else:
            current = odd
            previous = even
        for j in range(1, width):
            current[j] = current[j - 1] + previous[j]

    return even[-1] if height % 2 != 0 else odd[-1]
