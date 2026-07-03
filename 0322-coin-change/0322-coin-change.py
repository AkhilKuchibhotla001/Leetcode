class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount + 1)]

        dp[0] = 0  # to make amount 0 we need 0 coins.

        for i in range(1 , amount + 1):

            for coin in coins:

                if i >= coin:
                    dp[i] = min(dp[i] , 1 + dp[i - coin])

        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]


        