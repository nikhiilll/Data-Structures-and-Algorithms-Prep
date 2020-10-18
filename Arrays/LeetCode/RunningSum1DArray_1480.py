def runningSum(nums):
    running_sum = []
    sum = 0
    for num in nums:
        sum += num
        running_sum.append(sum)
    return running_sum

arr = [1,1,1,1,1]
print(runningSum(arr))