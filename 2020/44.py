# 221. Maximal Square
# https://leetcode.com/problems/maximal-square/
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        n = len(matrix)
        m = len(matrix[0])
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        maxLen = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j - 1], dp[i - 1][j]) + 1
                    maxLen = max(maxLen, dp[i][j])

        return maxLen * maxLen