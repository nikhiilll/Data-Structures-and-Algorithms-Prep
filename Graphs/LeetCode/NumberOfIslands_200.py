def numIslands(grid):

    if not grid:
        return 0


    #Function to get neighbours
    def getNeighbours(row, col, grid):

        neighbours = []

        if row - 1 >= 0:
            neighbours.append((row - 1, col))
        if row + 1 < len(grid):
            neighbours.append((row + 1, col))
        if col - 1 >= 0:
            neighbours.append((row, col - 1))
        if col + 1 < len(grid[0]):
            neighbours.append((row, col + 1))

        return neighbours

    #Function to check if island
    def isIsland(row, col, grid, visited):

        if grid[row][col] == "0":
            return True
        
        visited[row][col] = True
        neighbours = getNeighbours(row, col, grid)

        for n in neighbours:
            if not visited[n[0]][n[1]] and not isIsland(n[0], n[1], grid, visited):
                return False
        
        return True


    
    visited = [[False for _ in grid[0]] for _ in grid]
    noOfIslands = 0

    for row in range(len(grid)):
        for col in range(len(row)):
            if grid[row][col] == "1" and not visited[row][col] and isIsland(row, col, grid, visited):
                noOfIslands += 1
    
    return noOfIslands



    #Simple code from LeetCode discussion section
    
    def numIslands(grid):
        if not grid:
            return 0
            
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1
        return count

    def dfs(grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        dfs(grid, i+1, j)
        dfs(grid, i-1, j)
        dfs(grid, i, j+1)
        dfs(grid, i, j-1)