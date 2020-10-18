def smallerNumbersThanCurrent(nums):

    #Copied Solution from Discussion. The first solution would have been O(n^2) solution. Remember to use dictionary in places,
    #decrease the runtime.
    ans:int = {}

    for i, num in enumerate(sorted(nums)):
        if num not in ans:
            ans[num] = i

    return [ans[num] for num in nums]