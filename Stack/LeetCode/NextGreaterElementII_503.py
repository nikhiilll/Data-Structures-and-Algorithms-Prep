def nextGreaterElements(nums):

    n = len(nums)
    result = [-1] * n
    stack = []

    for i in range(n):
        if len(stack) == 0:
            stack.append(i)
        else:
            if nums[i] > nums[stack[-1]]:
                while stack and nums[i] > nums[stack[-1]]:
                    result[stack.pop()] = nums[i]
            stack.append(i)
    
    for i in range(n):
        if stack:
            if nums[i] > nums[stack[-1]]:
                while stack and nums[i] > nums[stack[-1]]:
                    result[stack.pop()] = nums[i]
        else:
            break
    
    return result

nums = [1,2,1]
print(nextGreaterElements(nums))