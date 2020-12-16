class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        TC: O(n) | SC: O(1)
        """
                
        maxArea = float("-inf")
        left, right = 0, len(height) - 1
        
        while left < right:
            if height[left] > height[right]:
                maxArea = max(maxArea, (right - left) * height[right])
                right -= 1
            else:
                maxArea = max(maxArea, (right - left) * height[left])
                left += 1
        
        return maxArea




        """
        TC: O(n^2) | SC: O(1)
        """
        maxArea = float("-inf")
        
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                
                currentArea = min(height[j], height[i]) * (j - i)
                maxArea = max(maxArea, currentArea)
        
        return maxArea