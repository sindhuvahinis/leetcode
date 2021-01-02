class Solution:

    def sort(self, key):
        a, b = key.split(' ', 1)
        if b[0].isdigit():
            return (1, None, None)
        else:
            return (0, b, a)

    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        logs.sort(key=self.sort)
        return logs