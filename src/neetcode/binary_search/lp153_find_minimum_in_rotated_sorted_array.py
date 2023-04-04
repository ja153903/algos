class Solution:
    def findMin(self, nums: list[int]) -> int:
        # if we know that the array is rotated, but was previously in sorted order
        # then we can still adapt binary search to find the minimum value
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] >= nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
