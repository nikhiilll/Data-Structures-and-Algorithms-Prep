class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # for i in range(len(nums) - 1, 0, -1):
        #     if nums[i] < nums[i - 1]:
        #         return nums[i]
        
        # return nums[0]

         """
        TC: O(logn) | SC: O(1)
         """       
        left, right = 0, len(nums) - 1
    
        while left < right:
            
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]
            
        