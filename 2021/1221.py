# 1221. Split a String in Balanced Strings
# https://leetcode.com/problems/split-a-string-in-balanced-strings/
class Solution:
    def balancedStringSplit(self, s: str) -> int:

        res, count = 0, 0

        for c in s:
            count += 1 if c == 'L' else -1
            if count == 0:
                res += 1

        return res