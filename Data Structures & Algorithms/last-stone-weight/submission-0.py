class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) >= 2:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            if x != y:
                heapq.heappush(heap, -(x-y))

        if not heap:
            return 0
        else:
            return -heap[0]
        