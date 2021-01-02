# 210. Course Schedule II
# MEDIUM

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # topological sort

        # Calculate the indegree of each course
        indegree = [0] * numCourses
        adjlist = collections.defaultdict(list)

        for pair in prerequisites:
            indegree[pair[0]] += 1
            adjlist[pair[1]].append(pair[0])

        # add all the courses with indegree 0 to the queue
        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        # loop through queue until empty
        # 1. dequeue the course and add it to the res
        # 2. loop through the courses that are dependent on the course is dequeued
        # 3. if the indegree of the dependent courses is 0, add it to the queue

        res = []
        while queue:
            course = queue.popleft()
            res.append(course)

            for adj in adjlist[course]:
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    queue.append(adj)

        # check if the len of the result is equal to the number of courses
        return res if len(res) == numCourses else []