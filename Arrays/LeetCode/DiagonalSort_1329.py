def diagonalSort(mat):

    return_mat = mat.copy()

    for i in range(len(mat[0]) - 1):

        sorted_diagonal = []

        for j in range(len(mat) - i):
            sorted_diagonal.append(mat[i + j][j])
            
        sorted_diagonal.sort()
        
        for j in range(len(mat) - i):
            print(sorted_diagonal[j])
            return_mat[i + j][j] = sorted_diagonal[j]

        
    for i in range(1, len(mat) - 1):

        sorted_diagonal = []

        for j in range(len(mat[0]) - 1 - i):
            sorted_diagonal.append(mat[j][i + j])
        sorted_diagonal.sort()
        for j in range(len(mat[0]) - 1 - i):
            return_mat[j][i + j] = sorted_diagonal[j]
    
    return return_mat

mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
print(diagonalSort(mat))
    
        
