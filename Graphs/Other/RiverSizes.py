def riverSizes(matrix):

    m, n = len(matrix), len(matrix[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    rivers = []

    for i in range(m):
        for j in range(n):
            if not visited[i][j]:
                if matrix[i][j] == 0:
                    visited[i][j] = True
                else:
                    rivers.append(findRiverSizes(i, j, m, n, matrix, visited))

    return rivers


def findRiverSizes(row, col, m, n, matrix, visited):

    if row < 0 or row >= m or col < 0 or col >= n:
        return 0

    if visited[row][col]:
        return 0

    visited[row][col] = True
    if matrix[row][col] == 0:
        return 0

    riverSize = 1
    riverSize += findRiverSizes(row, col - 1, m, n, matrix, visited)
    riverSize += findRiverSizes(row - 1, col, m, n, matrix, visited)
    riverSize += findRiverSizes(row, col + 1, m, n, matrix, visited)
    riverSize += findRiverSizes(row + 1, col, m, n, matrix, visited)

    return riverSize
