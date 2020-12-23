from collections import defaultdict
from collections import deque


class Solution:

    def BFS(self, adjmatrix, source, destination):
        queue = deque()
        queue.append((source, 1.0))

        visited = set()
        visited.add(source)

        while queue:
            vertex, weight = queue.popleft()

            if vertex == destination:
                return weight

            for adjvertex, adjweight in adjmatrix[vertex].items():
                if adjvertex not in visited:
                    queue.append((adjvertex, weight * adjweight))
                    visited.add(adjvertex)

        return -1.0

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        # building graph, build adjancency matrix

        adjmatrix = defaultdict(defaultdict)

        for (dividend, divisor), value in zip(equations, values):
            adjmatrix[dividend][divisor] = value
            adjmatrix[divisor][dividend] = 1 / value

            adjmatrix[dividend][dividend] = 1.0
            adjmatrix[divisor][divisor] = 1.0

        # evaluating each query
        # if any of the operand is not available in the matrix, add -1
        # BFS search

        res = []

        for dividend, divisor in queries:
            if dividend in adjmatrix and divisor in adjmatrix:
                currres = self.BFS(adjmatrix, dividend, divisor)
                res.append(currres)
            else:
                res.append(-1.0)

        return res

