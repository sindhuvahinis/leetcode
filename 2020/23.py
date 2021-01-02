class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)

        dp = [[False for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        start = 0
        maxLength = 1
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                maxLength = 2

        for k in range(3, n + 1):
            for i in range(0, n - k + 1):
                j = i + k - 1

                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True

                    if k > maxLength:
                        maxLength = k
                        start = i

        return s[start:start + maxLength]