def findPath(arr, n):
    """
    TC: O((N^2)^4)
    SC: O(L * X), L = length of path and X = number of paths
    """
    paths = []
    visited = [[False for _ in arr[0]] for _ in arr]

    pathFinder(0, 0, visited, paths, arr, "")
    return paths

def pathFinder(row, col, visited, paths, arr, currentPath):

    rows = len(arr)
    cols = len(arr[0])

    if row == rows - 1 and col == cols - 1:
        paths.append(currentPath)
        return
    
    visited[row][col] = True
    
    #Visit down
    if row + 1 < rows and arr[row + 1][col] == 1 and not visited[row + 1][col]:
        pathFinder(row + 1, col, visited, paths, arr, currentPath + "D")
    #Visit left
    if col - 1 > 0 and arr[row][col - 1] == 1 and not visited[row][col - 1]:
        pathFinder(row, col - 1, visited, paths, arr, currentPath + "L")
    #Visit right
    if col + 1 < cols and arr[row][col + 1] == 1 and not visited[row][col + 1]:
        pathFinder(row, col + 1, visited, paths, arr, currentPath + "R")
    #Visit up
    if row - 1 >= 0 and arr[row - 1][col] == 1 and not visited[row - 1][col]:
        pathFinder(row - 1, col, visited, paths, arr, currentPath + "U")

    
    visited[row][col] = False
    return


