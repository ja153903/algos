class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []

        self._backtrack(nums, result, [], 0)

        return result

    def _backtrack(
        self, nums: list[int], result: list[list[int]], current: list[int], start: int
    ) -> None:
        result.append(list(current))

        for i in range(start, len(nums)):
            current.append(nums[i])
            self._backtrack(nums, result, current, i + 1)
            current.pop()
