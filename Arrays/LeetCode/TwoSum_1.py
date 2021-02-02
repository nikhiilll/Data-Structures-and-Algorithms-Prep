class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    """
    TC: O(n)
    SC: O(n)
    """
        numdict = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in numdict:
                return ([numdict[diff], i])
            numdict[nums[i]] = i