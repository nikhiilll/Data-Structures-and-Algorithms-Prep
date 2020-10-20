from collections import deque

def sortArrayByParity(A):

    A_new = deque([])

    for num in A:
        if num % 2 == 0:
            A_new.appendleft(num)
        else:
            A_new.append(num)

    return list(A_new)

A = [3,1,2,4]
print(sortArrayByParity(A))


"""
class Solution:
    def sortArrayByParity(self, A):
        beg, end = 0, len(A) - 1
        
        while beg <= end:
            if A[beg] % 2 == 0:
                beg += 1
            else:
                A[beg], A[end] = A[end], A[beg]
                end -= 1
        return A


"""