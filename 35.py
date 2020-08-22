import heapq
list = [1, 2, 3, 10, 9, 8]

heapq.heapify(list)

print(heapq.heappop(list))
print(heapq.heappop(list))
print(heapq.heappop(list))
print(heapq.heappop(list))
print(heapq.heappop(list))
print(heapq.heappop(list))
print()
list = [1, 2, 3, 10, 9, 8]

heapq._heapify_max(list)
print(heapq._heappop_max(list))
print(heapq._heappop_max(list))
print(heapq._heappop_max(list))

heapq._heappush_max(list, 12)

print(heapq._heappop_max(list))
print(heapq._heappop_max(list))
print(heapq._heappop_max(list))
