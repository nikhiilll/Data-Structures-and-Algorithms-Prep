def findLucky(arr):

    # lucky_int = []

    # for num in arr:
    #     if num == arr.count(num):
    #         lucky_int.append(num)
    
    # if len(lucky_int) == 0:
    #     return -1
    # else:
    #     lucky_int.sort()
    #     return lucky_int[-1]

    lucky_int = {}
    max_res = -1

    for num in arr:
        if num not in lucky_int:
            lucky_int[num] = 1
        else:
            lucky_int[num] += 1
    
    for lucky in lucky_int:
        if lucky_int[lucky] == lucky:
            max_res = max(max_res, lucky_int[lucky])
    
    return max_res



arr = [2,2,3,4]
print(findLucky(arr))