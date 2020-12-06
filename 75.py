import collections
import heapq
from itertools import combinations


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        heap = []

        for user, timestmp, web in zip(username, timestamp, website):
            heapq.heappush(heap, (timestmp, web, user))

        usermap = collections.defaultdict(list)
        while heap:
            _, web, user = heapq.heappop(heap)
            usermap[user].append(web)

        webmap = collections.defaultdict(int)
        maxCount = 0
        res = tuple()

        for user, li in usermap.items():
            comb = combinations(li, 3)

            for webcomb in set(comb):
                webmap[webcomb] += 1

                if webmap[webcomb] > maxCount:
                    res = webcomb
                    maxCount = webmap[webcomb]
                elif webmap[webcomb] == maxCount:
                    if webcomb < res:
                        res = webcomb

        return res
