# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
# 1249. Minimum Remove to Make Valid Parentheses
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stack = []
        index = set()

        for i, c in enumerate(s):
            if c == '(':
                stack.append(('(', i))

            if not stack:
                if c == ')':
                    index.add(i)
            elif stack and c == ')':
                stack.pop()

        while stack:
            top = stack.pop()
            index.add(top[1])

        res = ''
        for i, c in enumerate(s):
            if i not in index:
                res += c

        return res