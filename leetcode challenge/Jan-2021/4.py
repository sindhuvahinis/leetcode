class Solution:
    def countArrangement(self, n: int) -> int:

        visited = [False] * (n + 1)
        self.count = 0
        self.backtrack(n, 1, visited)
        return self.count

    def backtrack(self, n, index, visited):
        if index > n:
            self.count += 1

        for num in range(1, n + 1):
            if not visited[num] and (num % index == 0 or index % num == 0):
                visited[num] = True
                self.backtrack(n, index + 1, visited)
                visited[num] = False