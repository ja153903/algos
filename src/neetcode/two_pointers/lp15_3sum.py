class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []

        nums.sort()

        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                j, k = i + 1, len(nums) - 1

                while j < k:
                    _sum = nums[i] + nums[j] + nums[k]
                    if _sum == 0:
                        result.append([nums[i], nums[j], nums[k]])

                        while j < k and nums[j] == nums[j + 1]:
                            j += 1

                        while j < k and nums[k] == nums[k - 1]:
                            k -= 1

                        j += 1
                        k -= 1
                    elif _sum < 0:
                        j += 1
                    else:
                        k -= 1

        return result
