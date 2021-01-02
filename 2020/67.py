from collections import deque


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        n = len(graph)
        colors = [0] * n

        # blue = 1
        # red = -1

        # there could be disconnected graphs
        # hence looping through each vertex

        for i in range(n):
            if colors[i] != 0:
                continue
            queue = deque()
            queue.append(i)
            colors[i] = 1

            while queue:
                vertex = queue.popleft()
                # get the neighbors of the current node
                for neigh in graph[vertex]:
                    if colors[neigh] == 0:
                        colors[neigh] = -colors[vertex]
                        queue.append(neigh)
                    else:
                        if colors[neigh] != -colors[vertex]:
                            return False

        return True