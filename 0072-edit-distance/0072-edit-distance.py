class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [n - i for i in range(n + 1)]

        for i in range(len(word1) -1 , -1, -1):
            curr = [0] * (n + 1)

            curr[n] = m - i

            for j in range(len(word2) - 1, -1, -1):

                if word1[i] == word2[j]:
                    curr[j] = dp[j + 1]
                
                else:
                    curr[j] = 1 + min(dp[j] , curr[j + 1], dp[j + 1])

            dp = curr
        return dp[0]
       
