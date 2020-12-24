class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # sort the intervals based on start time
        # end of prev is greater start of next interval - overlapping

        # start and end of prev interval
        # append start and end to result only if there is no overlap

        intervals.sort(key=lambda x: x[0])

        start, end = intervals[0][0], intervals[0][1]

        res = []

        for i in range(1, len(intervals)):
            if end >= intervals[i][0]:
                end = max(end, intervals[i][1])
            else:
                res.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]

        res.append([start, end])

        return res