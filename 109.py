class Solution:
    def reorganizeString(self, S: str) -> str:

        heap = [(-S.count(key), key) for key in set(S)]

        for count, key in heap:
            if -count > (len(S) + 1) // 2:
                return ''

        heapq.heapify(heap)

        ans = []
        while len(heap) > 1:
            count1, key1 = heapq.heappop(heap)
            count2, key2 = heapq.heappop(heap)

            ans.append(key1)
            ans.append(key2)

            if count1 + 1 < 0:
                heapq.heappush(heap, (count1 + 1, key1))

            if count2 + 1 < 0:
                heapq.heappush(heap, (count2 + 1, key2))

        if heap:
            count, key = heapq.heappop(heap)
            ans.append(key)

        return ''.join(ans)