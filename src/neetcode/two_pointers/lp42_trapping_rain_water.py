class Solution:
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        ans = 0

        maxleft, maxright = height[left], height[right]

        while left < right:
            if height[left] < height[right]:
                if height[left] > maxleft:
                    maxleft = height[left]
                else:
                    ans += maxleft - height[left]
                    left += 1
            else:
                if height[right] > maxright:
                    maxright = height[right]
                else:
                    ans += maxright - height[right]
                    right -= 1

        return ans
