def countNegatives(grid):

    negative_nos = 0

    for i in range(len(grid)):

        k = len(grid[0])
        for j in range(k):
            if grid[i][j] < 0:
                negative_nos += k - j
                break
        
    return negative_nos

grid = [[3,2],[1,0]]
print(countNegatives(grid))
            