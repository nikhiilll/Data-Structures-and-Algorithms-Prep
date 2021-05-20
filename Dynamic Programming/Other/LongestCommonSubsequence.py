"""
TC: O(n * m)
SC: O(n * m)
"""


def longestCommonSubsequence(str1, str2):

    grid = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                grid[i][j] = grid[i - 1][j - 1] + 1
            else:
                grid[i][j] = max(grid[i - 1][j], grid[i][j - 1])

    return buildSequence(str1, str2, grid)


def buildSequence(str1, str2, grid):

    i, j = len(str1), len(str2)
    sequence = []
    while i > 0 and j > 0:
        if grid[i][j] == grid[i - 1][j]:
            i -= 1
        elif grid[i][j] == grid[i][j - 1]:
            j -= 1
        else:
            sequence.append(str1[i - 1])
            i -= 1
            j -= 1

    return [sequence[x] for x in range(len(sequence) - 1, -1, -1)]
