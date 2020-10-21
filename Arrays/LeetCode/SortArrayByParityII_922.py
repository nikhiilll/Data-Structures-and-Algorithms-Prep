def sortArrayByParityII(A):

    n = len(A)
    odd_ptr = 1
    even_ptr = 0
    sorted_A = A[:]

    for i in range(n):
        if i % 2 == 0:
            if A[i] % 2 != 0:
                sorted_A[odd_ptr] = A[i]
                odd_ptr += 2
            else:
                sorted_A[even_ptr] = A[i]
                even_ptr += 2
        else:
            if A[i] % 2 != 0:
                sorted_A[odd_ptr] = A[i]
                odd_ptr += 2
            else:
                sorted_A[even_ptr] = A[i]
                even_ptr += 2
    
    return sorted_A



A = [4,2,5,7]
print(sortArrayByParityII(A))


"""

In-place solution that I knew could be done but could not come up with it.

def sortArrayByParityII(self, A):
        i, j, L = 0, 1, len(A)              # i - even index, j - odd index, L - length of A
        while j < L:                          # (L - 1) is odd, j can reach the last element, so this condition is enough
            if A[j] % 2 == 0:              # judge if the value on odd indices is odd
                A[j], A[i] = A[i], A[j]     # if it is even, exchange the values between index j and i
                i += 2                         # even indices get a right value, then i pointer jump to next even index
            else:
                j += 2                         # if it is odd, odd indices get a right value, then j pointer jump to next odd index
        return A


"""