from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        return [num for num, _ in Counter(nums).most_common(k)]
