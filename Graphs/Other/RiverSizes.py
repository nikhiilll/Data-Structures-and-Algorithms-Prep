def riverSizes(matrix):
    """
    TC: O(w*h)
    SC: O(w*h)
    """
    visited = [[False for _ in matrix[0]] for _ in matrix]
    result = []

    for row in range(len(matrix)):
        for column in range(len(matrix[0])):

            if matrix[row][column] == 1 and not visited[row][column]:
                result.append(countRiver(row, column, matrix, visited))
    
    return result


def countRiver(row, column, matrix, visited):

    count = 1
    visited[row][column] = True

    if row + 1 < len(matrix) and column < len(matrix[0]) and matrix[row + 1][column] == 1 and not visited[row + 1][column]:
        count += countRiver(row + 1, column, matrix, visited)
    if row < len(matrix) and column + 1 < len(matrix[0]) and matrix[row][column + 1] == 1 and not visited[row][column + 1]:
        count += countRiver(row, column + 1, matrix, visited)
    if row - 1 >= 0 and column < len(matrix[0]) and matrix[row - 1][column] == 1 and not visited[row - 1][column]:
        count += countRiver(row - 1, column, matrix, visited)
    if row < len(matrix) and column - 1 >= 0 and matrix[row][column - 1] == 1 and not visited[row][column - 1]:
        count += countRiver(row, column - 1, matrix, visited)

    return count


array = [
  [1, 0, 0, 1, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0]
]
print(riverSizes(array))