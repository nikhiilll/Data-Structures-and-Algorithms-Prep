class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [1] * len(nums)
        
        runningProduct = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= runningProduct
            runningProduct *= nums[i]
        
        runningProduct = 1
        for i in range(0, len(nums)):
            result[i] *= runningProduct
            runningProduct *= nums[i]
        
        return (result)
        