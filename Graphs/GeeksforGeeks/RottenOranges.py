from collections import deque


class Solution:
    def orangesRotting(self, grid):

    if not grid:
        return -1

    def isValid(x, y, grid):
        if x >= 0 and y >= 0 and x < len(grid) and y < len(grid[x]) and grid[x][y] == 1:
            grid[x][y] = 2
            return True
        return False

    def checkAll(grid):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return False

        return True

    queue = deque()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 2:
                queue.append((i, j))

    if not queue:
        return -1
    timeFrames = -1
    flag = True

    while queue:

        for _ in range(len(queue)):
            i, j = queue.popleft()
            if isValid(i - 1, j, grid):
                queue.append((i - 1, j))
            if isValid(i + 1, j, grid):
                queue.append((i + 1, j))
            if isValid(i, j - 1, grid):
                queue.append((i, j - 1))
            if isValid(i, j + 1, grid):
                queue.append((i, j + 1))
        timeFrames += 1

    if timeFrames == 0:
        return -1

    if not checkAll(grid):
        return -1
    return timeFrames
