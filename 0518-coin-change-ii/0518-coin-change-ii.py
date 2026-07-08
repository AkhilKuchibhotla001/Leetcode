class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1  # no of ways to make amount 0 is 1 (by taking no coins)

        for coin in coins:
            for i in range(coin , amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]

