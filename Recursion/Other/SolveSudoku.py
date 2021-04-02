def solveSudoku(board):

    solvePartialSudoku(board, 0, 0)
    return board

def solvePartialSudoku(board, row, col):

    currentRow = row
    currentCol = col

    if currentCol == len(board[row]):
        currentCol = 0
        currentRow += 1
        if currentRow == len(board):
            return True
    
    if board[currentRow][currentCol] == 0:
        return tryDigitsAtPosition(board, currentRow, currentCol)
    
    return solvePartialSudoku(board, currentRow, currentCol + 1)

def tryDigitsAtPosition(board, row, col):

    for digit in range(1, 10):
        if isValidAtPosition(digit, row, col, board):
            board[row][col] = digit
            if solvePartialSudoku(board, row, col + 1):
                return True

    board[row][col] = 0
    return False

def isValidAtPosition(digit, row, col, board):

    rowIsValid = digit not in board[row]
    columnIsValid = digit not in map(lambda r: r[col], board)

    if not rowIsValid or not columnIsValid:
        return False
    
    subgridRowStart = (row // 3) * 3
    subgridColStart = (col // 3) * 3

    for i in range(3):
        for j in range(3):
            if digit == board[subgridRowStart + i][subgridColStart + j]:
                return False

    return True
