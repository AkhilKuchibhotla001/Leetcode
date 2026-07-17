class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [0] * n

        if obstacleGrid[m - 1][n - 1] == 0:
            dp[n -1] = 1

        for i in range(m -1 , -1, -1):
            curr = [0] * n
            for j in range(n - 1, -1, -1):

                if i == m - 1 and j == n -1:
                    curr[j] = dp[j]
                elif obstacleGrid[i][j] == 1:
                    curr[j] = 0
                else:
                    down = dp[j]
                    right = 0
                    if j + 1 < n:
                        right = curr[j + 1]
                    
                    curr[j] = down + right
            dp = curr
        return dp[0]

        