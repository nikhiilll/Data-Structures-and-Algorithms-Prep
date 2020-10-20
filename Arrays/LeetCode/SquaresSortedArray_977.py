def sortedSquares(A):

    for i in range(len(A)):
        A[i] = A[i] ** 2
    
    A.sort()
    return (A)

A = [-7,-3,2,3,11]
print(sortedSquares(A))


"""
sorted() would be O(n) in this case

Explanation from discussions: Python's builtin sort is timsort which works by aggregating increasing and 
decreasing runs and then merging them. Since the resultant array after squaring all the terms will be first strictly decreasing 
and then strictly increasing, timsort reverses the strictly decreasing segment and then merges both runs in O(N).
"""