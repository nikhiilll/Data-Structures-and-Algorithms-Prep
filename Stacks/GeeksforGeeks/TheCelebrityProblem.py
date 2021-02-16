def celebrity(M, n):
    """
    TC: O(n)
    SC: O(1)
    """
    a = 0
    b = n - 1

    while a < b:
        if M[a][b]:
            a += 1
        else:
            b -= 1

    for i in range(n):
        if (i != a) and (M[a][i] or not M[i][a]):
            return -1

    return a  
        