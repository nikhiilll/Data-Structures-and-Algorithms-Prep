"""
TC: O(n * c)
SC: O(n)
"""


def coinChange(coins, amount):

    if not coins or amount == 0:
        return 0

    minCoins = [float("inf") for _ in range(amount + 1)]
    minCoins[0] = 0
    for i in range(amount + 1):
        for coin in coins:
            if coin <= i:
                minCoins[i] = min(minCoins[i], minCoins[i - coin] + 1)

    return minCoins[-1] if minCoins[-1] != float("inf") else -1
