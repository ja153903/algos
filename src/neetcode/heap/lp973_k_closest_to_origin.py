import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        h = []

        for point in points:
            heapq.heappush(h, (-point[0] ** 2 - point[1] ** 2, point))
            if len(h) > k:
                heapq.heappop(h)

        return [point for _, point in h]
