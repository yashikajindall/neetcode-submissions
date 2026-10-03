class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap_list = []
        for x,y in points:
            distance = (x*x) + (y*y)
            heap_list.append((distance, (x, y)))
        heapq.heapify(heap_list)

        result = []
        for i in range(k):
            distance, point = heapq.heappop(heap_list)
            result.append(point)

        return result
