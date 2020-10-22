def check_value(nums, startValue):

    for num in nums:
        startValue += num
        if startValue < 1:
            return False
    
    return True


def minStartValue(nums):

    startValue = 1

    while startValue:
        if check_value(nums, startValue):
            return startValue
        startValue += 1




nums = [-3,2,-3,4,2]
print(minStartValue(nums))