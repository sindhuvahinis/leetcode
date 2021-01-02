class Solution:

    def union(self, x, y):
        xParent = self.findParent(x)
        yParent = self.findParent(y)

        if xParent != yParent:
            # second becomes the parent of first
            self.parent[xParent] = yParent

    def findParent(self, vertex):
        if self.parent[vertex] == -1:
            return vertex
        else:
            return self.findParent(self.parent[vertex])

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Union Find

        self.parent = [-1] * n
        adjlist = collections.defaultdict(list)

        for edge in edges:
            adjlist[edge[0]].append(edge[1])
            adjlist[edge[1]].append(edge[0])

        for vertex in range(n):
            vertexparent = self.findParent(vertex)

            for adj in adjlist[vertex]:
                adjparent = self.findParent(adj)

                if vertexparent != adjparent:
                    self.union(vertex, adj)

        nComponents = 0
        for vertex in self.parent:
            if vertex == -1:
                nComponents += 1

        return nComponents
