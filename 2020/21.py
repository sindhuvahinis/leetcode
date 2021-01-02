class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        wordSet = set(wordDict)
        dp = dict()

        def recur(s):
            if s in dp:
                return dp[s]

            if s in wordDict:
                return True

            for end in range(1, len(s) + 1):
                if s[:end] in wordSet and recur(s[end:]):
                    dp[s[:end]] = True
                    return True

            dp[s] = False
            return False

        return recur(s)