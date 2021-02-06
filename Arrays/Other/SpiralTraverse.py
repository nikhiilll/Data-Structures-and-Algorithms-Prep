def spiralTraverse(array):

    result = []
    fr, fc = 0, 0
    lr, lc = len(array), len(array[0])

    while fr < lr and fc < lc:

        for i in range(fc, lc):
            result.append(array[fr][i])
        fr += 1

        for i in range(fr, lr):
            result.append(array[i][lc - 1])
        lc -= 1

        if fr < lr:
            for i in range(lc - 1, fc - 1, -1):
                result.append(array[lr - 1][i])
            lr -= 1

        if fc < lc:
            for i in range(lr - 1, fr - 1, -1):
                result.append(array[i][fc])
            fc += 1
    
    return result