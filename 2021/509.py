# https://leetcode.com/problems/fibonacci-number/
# 509. Fibonacci Number

class Solution:
    def fib(self, n: int) -> int:

        if n == 0 or n == 1:
            return n

        prev1 = 0
        prev2 = 1
        res = 0

        for _ in range(2, n + 1):
            res = prev1 + prev2
            prev1 = prev2
            prev2 = res

        return res

    # Time complexity : O(n)
    # space complexity : O(1)