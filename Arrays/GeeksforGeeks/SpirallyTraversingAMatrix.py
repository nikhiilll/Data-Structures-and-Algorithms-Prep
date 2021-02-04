def spirallyTraverse(matrix, r, c):
    """
    TC: O(r*c)
    SC: O(r*c)
    """
    fr, fc = 0, 0
    result = []

    while fr < r and fc < c:

        #Print first row
        for i in range(fc, c):
            result.append(matrix[fr][i])
        fr += 1

        #Print last column
        for i in range(fr, r):
            result.append(matrix[i][c - 1])
        c -= 1

        #Print last row
        if fr < r:
            for i in range(c - 1, fc - 1, -1):
                result.append(matrix[r - 1][i])
            r -= 1
        
        #Print first column
        if fc < c:
            for i in range(r - 1, fr - 1, -1):
                result.append(matrix[i][fc])
            fc += 1
    
    return result

