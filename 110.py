class Solution:

    def recur(self, jobs, d, index, dp):

        if d == 0 and index == len(jobs):
            return 0

        if d == 0 or index == len(jobs):
            return math.inf

        if dp[d][index] != -1:
            return dp[d][index]

        currmax = jobs[index]
        minDifficulty = math.inf

        # all possibilities for the day 1
        for i in range(index, len(jobs)):
            currmax = max(jobs[i], currmax)
            remDaysMax = self.recur(jobs, d - 1, i + 1, dp)
            if remDaysMax != math.inf:
                minDifficulty = min(minDifficulty, currmax + remDaysMax)

        dp[d][index] = minDifficulty
        return dp[d][index]

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # days and index of job difficulty
        dp = [[-1] * len(jobDifficulty) for _ in range(d + 1)]
        res = self.recur(jobDifficulty, d, 0, dp)
        return res if res != math.inf else -1