class Solution:

    def __init__(self):
        self.lettermap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

    def DFS(self, digits, index, curr):
        if index == len(digits):
            self.res.append(''.join(curr))
            return

        s = self.lettermap[digits[index]]
        for c in s:
            curr.append(c)
            self.DFS(digits, index + 1, curr)
            curr.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        self.res = []

        if len(digits) == 0:
            return self.res

        self.DFS(digits, 0, [])
        return self.res