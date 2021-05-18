def minNumberOfCoinsForChange(n, denoms):

    dp = [float("inf")] * (n + 1)
    dp[0] = 0

    for i in range(n + 1):
        for coin in denoms:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[n] if dp[n] != float("inf") else -1
