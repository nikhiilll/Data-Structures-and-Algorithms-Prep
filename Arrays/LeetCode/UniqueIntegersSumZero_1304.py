def sumZero(n):
    
    # l = [0] * n

    # if n == 0:
    #     return [0]
    # elif n % 2 == 0:
    #     for i in range(1, n//2 + 1):
    #         l[i] = -i
    #         l[-i] = i
    # else:
    #     l[(n//2) + 1] = 0
    #     for i in range(1, n//2 + 1):
    #         l[i] = -i
    #         l[-i] = i
    
    # return l

    return list(range(1 - n, n, 2))

n = 2
print(sumZero(n))