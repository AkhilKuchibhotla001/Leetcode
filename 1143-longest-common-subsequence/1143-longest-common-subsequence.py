class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [0] * (n + 1)
        for i in range(len(text1) - 1 , -1 , -1):
            curr = [0] * (n + 1)
            for j in range(len(text2) - 1, -1 , -1):
                if text1[i] == text2[j]:
                    curr[j] = 1 + dp[ j + 1]
                else:
                    curr[j] = max(dp[j] , curr[j + 1])
            dp = curr
        return dp[0]
    

        