class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # Time Complexity: O(n log n) where n is the max(piles)
        left, right = 1, max(piles)

        # outer loop is O(log n)
        while left < right:
            mid = left + (right - left) // 2

            # this check is O(n) so we do O(n) work log n times
            if self._can_finish_bananas(piles, h, mid):
                right = mid
            else:
                left = mid + 1

        return left

    def _can_finish_bananas(self, piles: list[int], h: int, k: int) -> bool:
        h_necessary = 0

        for pile in piles:
            h_necessary += pile // k
            if pile % k != 0:
                h_necessary += 1

        return h_necessary <= h
