class Solution:
    def calPoints(self, ops: List[str]) -> int:

        stack = []

        for op in ops:
            if (op.strip('-')).isnumeric():
                stack.append(int(op))
            elif op == '+':
                _sum = 0
                if len(stack) >= 1:
                    _sum += stack[-1]
                if len(stack) >= 2:
                    _sum += stack[-2]
                stack.append(_sum)
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                _sum = 0
                if len(stack) >= 1:
                    stack.append(stack[-1] * 2)

        return sum(stack)