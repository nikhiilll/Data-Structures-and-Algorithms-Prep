def canMakeArithmeticProgression(arr):

    arr.sort()
    common_diff = arr[1] - arr[0]

    if len(arr) == 2:
        return True

    for i in range(1, len(arr) - 1):
        if (arr[i + 1] - arr[i]) != common_diff:
            return False
    
    return True

arr = [1,2,4]
print(canMakeArithmeticProgression(arr))

        