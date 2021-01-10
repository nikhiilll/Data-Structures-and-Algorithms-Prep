def removeIslands(matrix):

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):

            rowIsBorder = row == 0 or row == len(matrix) - 1
            colIsBorder = col == 0 or col == len(matrix[row]) - 1
            isBorder = rowIsBorder or colIsBorder

            if not isBorder:
                continue

            if matrix[row][col] != 1:
                continue
            
            changeOnesConnectedToBordersToTwos(row, col, matrix)

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):

            colour = matrix[row][col]

            if colour == 2:
                matrix[row][col] = 1
            elif colour == 1:
                matrix[row][col] = 0

    return matrix


def changeOnesConnectedToBordersToTwos(row, col, matrix):

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

    rowSize, colSize = len(matrix), len(matrix[0])
    neighbours = []

    if row - 1 >= 0:
        neighbours.append((row - 1, col))
    if row +1 < rowSize:
        neighbours.append((row + 1, col))
    if col - 1 >= 0:
        neighbours.append((row, col - 1))
    if col + 1 < colSize:
        neighbours.append((row, col + 1))

    return neighbours
    

