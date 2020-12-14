class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        
        if not prices:
            return profit
        
        minPrice = prices[0]
        maxPrice = prices[0]
        
        for i in range(1, len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
                maxPrice = prices[i]
            if prices[i] > maxPrice:
                maxPrice = prices[i]
            profit = max(profit, maxPrice - minPrice)
        
        return profit