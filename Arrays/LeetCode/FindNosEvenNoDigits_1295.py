def findNumbers(nums):

    result = 0
    
    for num in nums:
        if(len(str(num)) % 2 == 0):
            result += 1
    
    return result

nums = [12,345,2,6,7896]
print(findNumbers(nums))