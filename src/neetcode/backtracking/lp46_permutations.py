class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []

        self._backtrack(nums, ans, [])

        return ans

    def _backtrack(self, nums: list[int], ans: list[list[int]], cur: list[int]) -> None:
        if len(cur) == len(nums):
            ans.append(list(cur))
        else:
            for num in nums:
                if num in cur:
                    continue

                cur.append(num)
                self._backtrack(nums, ans, cur)
                cur.pop()
