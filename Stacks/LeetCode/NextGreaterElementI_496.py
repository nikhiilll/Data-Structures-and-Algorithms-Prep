def nextGreaterElement(nums1, nums2):

    # result = []

    # for num in nums1:
    #     index = nums2.index(num)
    #     large = -1
    #     for i in range(index + 1, len(nums2)):
    #         if nums2[i] > num:
    #             large = nums2[i]
    #             break
    #     result.append(large)
    
    # return result

    cache, stack = {}, []
    result = []

    for num in nums2:
        if len(stack) == 0:
            stack.append(num)
        elif stack[-1] >= num:
            stack.append(num)
        elif stack[-1] < num:
            while stack and stack[-1] < num:
                cache[stack.pop()] = num
            stack.append(num)
    
    for num in nums1:
        if num in cache:
            result.append(cache[num])
        else:
            result.append(-1)
    
    return result


nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(nextGreaterElement(nums1, nums2))


"""
def nextGreaterElement(self, findNums, nums):

        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]

        cache, st = {}, []
        for x in nums:
            if len(st) == 0:
                st.append(x)
            elif x <= st[-1]:
                st.append(x)
            else:
                while st and st[-1] < x:
                    cache[st.pop()] = x
                st.append(x)
        result = []
        for x in findNums:
            if x in cache:
                result.append(cache[x])
            else:
                result.append(-1)
        return result



"""