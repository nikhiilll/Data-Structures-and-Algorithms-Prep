def max_sum(arr):

    arrSum = 0
    currVal = 0
    n = len(arr)

    for i in range(n):
        arrSum = arrSum + arr[i]
        currVal = currVal + (i * arr[i])
    
    maxVal = currVal

    for j in range(1, n):
        currVal = currVal + arrSum - n * arr[n - j]
        if currVal > maxVal:
            maxVal = currVal
    
    print(maxVal)

arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
max_sum(arr)

