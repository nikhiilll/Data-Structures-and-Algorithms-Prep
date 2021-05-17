def removeIslands(matrix):

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):

            if matrix[row][col] != 1:
                continue

            isRowBorder = row == 0 or row == len(matrix) - 1
            isColBorder = col == 0 or col == len(matrix[row]) - 1
            isBorder = isColBorder or isRowBorder

            if not isBorder:
                continue

            changeAllBorderOnesToTwos(row, col, matrix)

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 2:
                matrix[row][col] = 1
            elif matrix[row][col] == 1:
                matrix[row][col] = 0

    return matrix


def changeAllBorderOnesToTwos(row, col, matrix):

    stack = [(row, col)]

    while stack:
        currentRow, currentCol = stack.pop()
        matrix[currentRow][currentCol] = 2

        neighbours = findNeighbours(currentRow, currentCol, matrix)
        for neighbour in neighbours:
            r, c = neighbour
            if matrix[r][c] != 1:
                continue
            stack.append(neighbour)


def findNeighbours(row, col, matrix):

    neighbours = []
    if row - 1 >= 0:
        neighbours.append((row - 1, col))
    if row + 1 < len(matrix):
        neighbours.append((row + 1, col))
    if col - 1 >= 0:
        neighbours.append((row, col - 1))
    if col + 1 < len(matrix[0]):
        neighbours.append((row, col + 1))

    return neighbours
