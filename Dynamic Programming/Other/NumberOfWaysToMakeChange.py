def numberOfWaysToMakeChange(n, denoms):

    dp = [1] + [0] * n

    for coin in denoms:
        for i in range(n + 1):
            if coin <= i:
                dp[i] += dp[i - coin]

    return dp[n]
