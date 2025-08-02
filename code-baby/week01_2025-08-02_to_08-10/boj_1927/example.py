import heapq

heap = []

# 값 넣기
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 5)

# 항상 가장 작은 값부터 나옴
print(heapq.heappop(heap))  # 1
print(heapq.heappop(heap))  # 3
print(heapq.heappop(heap))  # 5

import heapq

max_heap = []

# 값 넣기 (음수로 변환)
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -5)

# 가장 큰 값부터 꺼내기
print(-heapq.heappop(max_heap))  # 5
print(-heapq.heappop(max_heap))  # 3
print(-heapq.heappop(max_heap))  # 1
