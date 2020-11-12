class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                excludeleft = s[left + 1:right + 1]
                excluderight = s[left:right]
                return excludeleft == excludeleft[::-1] or excluderight == excluderight[::-1]
            left += 1
            right -= 1

        return True