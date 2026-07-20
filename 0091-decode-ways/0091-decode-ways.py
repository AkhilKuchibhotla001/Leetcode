class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        
        a , b = 1 , 1
        for i in range(1 , len(s)):
            curr = 0

            if s[i] != "0":
                curr += b
            if 10 <= int(s[i - 1 : i + 1]) <= 26:
                curr += a

            a , b = b , curr
        return b

        