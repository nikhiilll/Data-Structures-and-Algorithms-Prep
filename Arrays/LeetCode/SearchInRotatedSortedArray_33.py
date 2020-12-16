class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums) - 1
        
        while left < right:
            
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        pivot = left
        left, right = 0, len(nums) - 1
        
        if nums[pivot] == target:
            return pivot
        
        if nums[pivot] <= target and target <= nums[right]:
            left = pivot
        else:
            right = pivot
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target: 
                return mid
            elif nums[mid] > target: 
                right = mid - 1
            else: 
                left = mid + 1
        
        return -1