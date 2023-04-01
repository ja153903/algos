class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        seen = set(nums)

        max_len = 0

        for num in nums:
            if num - 1 not in seen:
                current = num
                _len = 0

                while current in seen:
                    _len += 1
                    current += 1

                max_len = max(max_len, _len)

        return max_len
