def shuffle(nums, n):
    
    x_arr = nums[:n]
    y_arr = nums[n:]
    result = []

    if n < 1 or n > 500:
        return result

    if len(nums) != 2*n:
        return result

    for x, y in zip(x_arr, y_arr):
        result.append(x)
        result.append(y)

    return result

nums = [1,2,3,4,4,3,2,1]
n = 4
print(shuffle(nums, n))