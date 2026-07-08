class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * (n) for _ in range(m)]    # ( because the last row and last column takes only 1 path so every value in lat row and last column is 1's)

        for i in range(m - 2 , -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i][j + 1] + dp[i + 1][j]
        return dp[0][0]
        