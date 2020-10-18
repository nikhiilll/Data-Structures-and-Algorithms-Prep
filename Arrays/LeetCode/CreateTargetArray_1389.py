def createTargetArray(nums, index):
    result = []

    for i in range(len(index)):
        result.insert(index[i], nums[i])
    
    return result

nums = [0,1,2,3,4]
index = [0,1,2,2,1]
print(createTargetArray(nums, index))