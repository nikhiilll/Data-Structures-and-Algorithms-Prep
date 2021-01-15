class Solution:
	
    def findMaxArea(self, grid):
        """
        TC: O(n * m)
        SC: O(1)
        """
        if not grid:
            return 0
        
        maxSum = float("-inf")
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    maxSum = max(maxSum, self.countArea(row, col, grid))
        
        return maxSum
    
    def countArea(self, row, col, grid):

        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[row]) or grid[row][col] != 1:
            return 0
        
        grid[row][col] = "#"
        sum = 1
        sum += self.countArea(row, col - 1, grid)
        sum += self.countArea(row - 1, col - 1, grid)
        sum += self.countArea(row - 1, col, grid)
        sum += self.countArea(row - 1, col + 1, grid)
        sum += self.countArea(row, col + 1, grid)
        sum += self.countArea(row + 1, col + 1, grid)
        sum += self.countArea(row + 1, col, grid)
        sum += self.countArea(row + 1, col - 1, grid)

        return sum