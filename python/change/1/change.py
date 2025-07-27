def find_fewest_coins(coins, target):
    if target < 0: raise ValueError("target can't be negative")
    dp = {0: []}
    for i in range(1, target+1):
        dp[i] = None
        for coin in coins:
            lower_amount = i - coin
            if lower_amount < 0 or dp[lower_amount] is None: continue
            combination = dp[lower_amount] + [coin]
            if dp[i] is None or len(dp[lower_amount]) < len(dp[i]):
                dp[i] = combination

    if dp[target] is None: raise ValueError("can't make target with given coins")
    return dp[target]