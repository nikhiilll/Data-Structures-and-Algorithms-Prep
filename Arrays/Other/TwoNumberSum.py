def twoNumberSum(array, targetSum):
    """
    TC: O(n)
    SC: O(1)
    """
    numsSet = set()

    for num in array:
        if (targetSum - num) in numsSet:
            return [targetSum - num, num]
        numsSet.add(num)
    
    return []
