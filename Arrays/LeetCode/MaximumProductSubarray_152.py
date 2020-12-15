class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxProd, minProd, ans = nums[0], nums[0], nums[0]
        
        for i in range(1, len(nums)):
            temp1 = max(nums[i], maxProd * nums[i], minProd * nums[i])
            temp2 = min(nums[i], maxProd * nums[i], minProd * nums[i])
            maxProd, minProd = temp1, temp2
            ans = max(maxProd, ans)
        
        return ans