def maxSum(a, n):

    cumulativeSum = 0
    for i in range(n):
        cumulativeSum += a[i]
    
    currentValue = 0
    for i in range(n):
        currentValue += (i * a[i])
    
    result = currentValue

    for i in range(n - 1):
        nextValue = currentValue - (cumulativeSum - a[i]) + a[i] * (n - 1)
        currentValue = nextValue
        result = max(result, currentValue)
    
    return result