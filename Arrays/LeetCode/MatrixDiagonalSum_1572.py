def diagonalSum(mat):

    n = len(mat)
    sum = 0

    for i in range(n):
        sum += mat[i][i]
        sum += mat[i][n - i - 1]
    
    if n % 2 != 0:
        sum -= mat[(n - 1)//2][(n - 1)//2]
    
    return sum

mat = [[1,2,3], [4,5,6], [7,8,9]]
print(diagonalSum(mat))