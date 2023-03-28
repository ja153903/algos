class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda i: (i[0], i[1]))

        result = []

        for interval in intervals:
            if not result:
                result.append(interval)
            else:
                if result[-1][1] >= interval[0]:
                    result[-1] = [
                        min(result[-1][0], interval[0]),
                        max(result[-1][1], interval[1]),
                    ]
                else:
                    result.append(interval)

        return result
