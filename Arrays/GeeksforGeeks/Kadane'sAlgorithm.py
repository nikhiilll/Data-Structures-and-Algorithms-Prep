def maxSubArraySum(a, size):

    maxSum, runningSum = float("-inf"), 0

    for num in a:
        runningSum = max(runningSum + num, num)
        maxSum = max(maxSum, runningSum)
    
    return maxSum