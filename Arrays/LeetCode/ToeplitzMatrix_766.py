def isToeplitzMatrix(matrix):

    m = len(matrix)
    n = len(matrix[0])

    for i in range(n - 1):
        tracker = []
        j = 0
        while (i + j < n) and (j < m):
            tracker.append(matrix[j][i + j])
            print(tracker)
            j += 1
        if tracker.count(tracker[0]) != len(tracker):
            return False
    
    for i in range(m - 1):
        tracker = []
        j = 0
        while (i + j < m) and (j < n):
            tracker.append(matrix[i + j][j])
            print(tracker)
            j += 1
        if tracker.count(tracker[0]) != len(tracker):
            return False

    return True

matrix = [[1,2],[2,2]]
print(isToeplitzMatrix(matrix))


"""
def isToeplitzMatrix(self, m):
        for i in range(len(m) - 1):
            for j in range(len(m[0]) - 1):
                if m[i][j] != m[i + 1][j + 1]:
                    return False
        return True



"""
    
