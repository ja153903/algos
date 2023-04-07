class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # we know its rotated, so we can find the minimum in O(log n)
        # by doing binary search
        # once we find the minimum, we can use that value as a pivot point
        # because if the first element is shifted by p, then all elements are going to
        # be shifted by (p % n) where n is the length of the array
        # given this, we can then just do binary search looking for the target
        n = len(nums)
        left, right = 0, n - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        p = left

        left, right = 0, n - 1

        while left <= right:
            mid = left + (right - left) // 2
            true_mid = (mid + p) % n

            if nums[true_mid] == target:
                return true_mid
            elif nums[true_mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
