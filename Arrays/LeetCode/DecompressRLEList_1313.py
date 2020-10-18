def decompressRLElist(nums):
    result = []
    for i in range(0, len(nums), 2):
        freq = nums[i]
        number = nums[i + 1]
        result = result + [number] * freq
    
    return result

nums = [1,2,3,4]
print(decompressRLElist(nums))
         