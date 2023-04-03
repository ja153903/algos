class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # classic monotonic stack problem
        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                result[stack[-1]] = i - stack[-1]
                stack.pop()

            stack.append(i)

        return result
