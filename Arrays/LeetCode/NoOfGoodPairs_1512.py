def numIdenticalPairs(nums):

    good_pairs = 0
    n = len(nums)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                good_pairs += 1
    
    return good_pairs


nums = [1,1,1,1]
print(numIdenticalPairs(nums))


"""
Optimized solution for TC: O(n)

dic = {}
count =0
        
for num in nums:
    if num in dic:
        count +=dic[num]
        dic[num] +=1
    else:
        dic[num] =1
return count

"""