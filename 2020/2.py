# Course Schedule II
# 210

import collections

class Solution:
    def findOrder(self, numCourses, prerequisites):

        indegree = collections.defaultdict(int)
        adj_list = collections.defaultdict(list)

        for i in range(numCourses):
            indegree[i] = 0

        for pre in prerequisites:
            adj_list[pre[1]] += pre[0],
            indegree[pre[0]] += 1

        queue = collections.deque([key for key, value in indegree.items() if value == 0])

        res = []
        while queue:

            course = queue.popleft()
            res.append(course)

            for adj in adj_list[course]:
                indegree[adj] -= 1

                if indegree[adj] == 0:
                    del indegree[adj]
                    queue.append(adj)

        if len(res) != numCourses:
            return []

        return res
