class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        sumSoFar, maxSum = 0, float("-inf")
        
        for num in nums:
            sumSoFar = max(num, sumSoFar + num)
            maxSum = max(maxSum, sumSoFar)
        
        return maxSum