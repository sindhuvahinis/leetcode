# 253. Meeting rooms II
# MEDIUM

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        if not intervals:
            return 0

        # sort the intervals based on start time of intervals
        intervals.sort(key=lambda x: x[0])

        heap = []
        heapq.heappush(heap, intervals[0][1])

        # compare the heap top interval with curr interval
        # if the top intervals end time < curr start time, pop the top element
        # if not, add the interval's end time into heap.
        # return the size of the heap

        for i in range(1, len(intervals)):
            curr = intervals[i]
            if heap[0] <= curr[0]:
                heapq.heappop(heap)

            heapq.heappush(heap, curr[1])

        return len(heap)