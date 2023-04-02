from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        queue = deque()
        result = []

        for i, num in enumerate(nums):
            # remove the element that is out of the range of k
            while queue and queue[0] <= i - k:
                queue.popleft()

            # remove the element that is less than the current element
            while queue and nums[queue[-1]] < num:
                queue.pop()

            queue.append(i)

            if i >= k - 1:
                result.append(nums[queue[0]])

        return result
