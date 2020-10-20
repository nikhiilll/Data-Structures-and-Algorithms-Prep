def finalPrices(prices):

    final_prices = prices.copy()
    n = len(prices)    

    for i in range(n - 1):
        for j in range(i + 1, n):
            if prices[j] <= prices[i]:
                final_prices[i] -= prices[j]
                break
    
    return final_prices

prices = [8,4,6,2,3]
print(finalPrices(prices))


"""
One Pass

def finalPrices(self, A):
        stack = []
        for i, a in enumerate(A):
            while stack and A[stack[-1]] >= a:
                A[stack.pop()] -= a
            stack.append(i)
        return A

"""

