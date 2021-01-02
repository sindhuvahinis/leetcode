# https://leetcode.com/problems/add-strings/
from collections import deque


class Solution:
    
    def addStrings(self, num1: str, num2: str) -> str:

        carry = 0
        res = deque()

        i = len(num1) - 1
        j = len(num2) - 1

        while i >= 0 or j >= 0:
            a = ord(num1[i]) - ord('0') if i >= 0 else 0
            b = ord(num2[j]) - ord('0') if j >= 0 else 0

            s = a + b + carry
            carry = s // 10
            s = s % 10
            res.appendleft(str(s))

            i -= 1
            j -= 1

        if carry:
            res.appendleft(str(carry))

        return ''.join(res)
