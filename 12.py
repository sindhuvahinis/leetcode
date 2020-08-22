import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def recur(coins, amount, index, dp):

            if amount == 0:
                return 0

            if index >= len(coins):
                return math.inf

            if dp[index][amount] != -1:
                return dp[index][amount]

            count1 = math.inf
            if coins[index] <= amount:
                count1 = recur(coins, amount - coins[index], index, dp)

                if count1 != math.inf:
                    count1 += 1

            count2 = recur(coins, amount, index + 1, dp)
            dp[index][amount] = min(count1, count2)
            return dp[index][amount]

        dp = [[-1 for _ in range(amount + 1)] for _ in range(len(coins))]
        res = recur(coins, amount, 0, dp)

        return -1 if res == math.inf else res