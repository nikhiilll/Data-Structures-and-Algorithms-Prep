def isPossible(grid):

    def isReachable(row, col, grid, visited):

        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or visited[row][col] or grid[row][col] == 0:
            return False
        if grid[row][col] == 2:
            return True
        
        visited[row][col] = True
        if isReachable(row - 1, col, grid, visited):
            return True
        if isReachable(row + 1, col, grid, visited):
            return True
        if isReachable(row, col - 1, grid, visited):
            return True
        if isReachable(row, col + 1, grid, visited):
            return True
        
        return False

    visited = [[False for _ in grid[0]] for _ in grid]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                if isReachable(row, col, grid, visited):
                    return 1
                else:
                    return 0
    
    return 0

grid = [[1, 3], [3, 2]]
print(isPossible(grid))