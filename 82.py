# 682. Basketball Game
# EASY

class Solution:
    def calPoints(self, ops: List[str]) -> int:

        # Stack
        stack = []

        for op in ops:
            if op == 'C':
                stack.pop()
            elif op == 'D':
                val = stack[-1]
                stack.append(2 * int(val))
            elif op == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))

        _sum = 0
        while stack:
            _sum += stack.pop()

        return _sum