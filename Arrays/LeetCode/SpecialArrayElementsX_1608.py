def countSquares(matrix):

    max_square_len = min(len(matrix), len(matrix[0]))
    result = 0

    for side_length in range(max_square_len):
        for column in range(len(matrix[0]) - side_length):
            for row in range(len(matrix) - side_length):
                for i in range(side_length):
                    print(matrix[row + i][column + i])
                    if matrix[row + i][column + i] != 1:
                        break
                else:
                    result += 1
    
    return result

matrix =[[0,1,1,1],[1,1,1,1],[0,1,1,1]]
print(countSquares(matrix))