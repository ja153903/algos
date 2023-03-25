import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]) -> None:
        self._heap = []
        self._k = k

        for num in nums:
            self._add(num)

    def add(self, val: int) -> int:
        self._add(val)

        return self._heap[0]

    def _add(self, val: int) -> None:
        heapq.heappush(self._heap, val)
        if len(self._heap) > self._k:
            heapq.heappop(self._heap)
