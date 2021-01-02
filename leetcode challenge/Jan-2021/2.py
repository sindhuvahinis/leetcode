# Palindrome Permutation
# Day 1
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = collections.Counter(s)
        print(counter)

        res = 0
        for _, count in counter.items():
            res += count % 2

        return res == 0 or res == 1

    # TC: O(N)
    # SC : O(N)