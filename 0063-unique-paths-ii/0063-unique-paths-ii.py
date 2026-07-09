class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0] * (n) for  _ in range(m)]

        if obstacleGrid[m -1][n -1] == 0:
            dp[m -1][n -1] = 1
        
        for i in range(m -1, -1, -1):
            for j in range(n -1, -1, -1):

                if i == m -1 and j == n -1:
                    continue

                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0

                else:
                    down , right = 0 , 0
                    
                    if i + 1 < m:
                        down = dp[i + 1][j]
                    if j + 1 < n:
                        right = dp[i][j + 1]

                    dp[i][j] = down + right

        return dp[0][0]

        