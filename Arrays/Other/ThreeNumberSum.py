def threeNumberSum(array, targetSum):
    """
    TC: O(n^2)
    SC: O(n)
    """
    array.sort()
    triplets = []

    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
			currentSum = array[i] + array[left] + array[right]
            if currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
            else:
                triplets.append([array[i], array[left], array[right]])
				left += 1
				right -= 1
    
    return triplets