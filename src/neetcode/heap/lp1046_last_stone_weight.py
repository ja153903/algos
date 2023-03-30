import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            first, second = -heapq.heappop(heap), -heapq.heappop(heap)
            if first == second:
                continue

            heapq.heappush(heap, -abs(first - second))

        return -heapq.heappop(heap) if len(heap) == 1 else 0
