# 547. FREIND CIRCLES
# MEDIUM

class Solution:

    def DFS(self, M, visited, node):
        for adj in range(len(M)):
            if not visited[adj] and M[node][adj] == 1:
                visited[adj] = True
                self.DFS(M, visited, adj)

    def findCircleNum(self, M: List[List[int]]) -> int:

        N = len(M)

        visited = [False] * N
        count = 0

        for node in range(N):
            if not visited[node]:
                self.DFS(M, visited, node)
                count += 1

        return count