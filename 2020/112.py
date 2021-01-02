class Solution:

    # catsdogscats
    # c + atsdogscats
    # cat + dogs + cats

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        dp = {}
        d = set(words)

        def dfs(word):
            if word in dp:
                return dp[word]

            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]

                if prefix in d and suffix in d:
                    dp[word] = True
                    return True
                if prefix in d and dfs(suffix):
                    dp[word] = True
                    return True

            dp[word] = False
            return False

        res = []
        for word in words:
            if dfs(word):
                res.append(word)

        return res