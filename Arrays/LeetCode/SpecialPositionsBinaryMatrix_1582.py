def numSpecial(mat):

    count = 0
    rows = len(mat)
    columns = len(mat[0])

    for row in range(rows):
        for column in range(columns):
            if mat[row][column] == 1:
                if (sum(mat[row]) == 1) and (sum(mat[row][column] for row in range(rows)) == 1):
                    count += 1
    
    return count

mat = [[1,0,0],[0,1,0],[0,0,1]]
print(numSpecial(mat))