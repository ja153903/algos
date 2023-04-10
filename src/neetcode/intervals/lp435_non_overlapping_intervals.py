class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        """
        Given an array of intervals where intervals[i] = [start_i, end_i],
        return the minimum number of intervals you need to remove to make
        the rest of the intervals non-overlapping.
        """

        n = len(intervals)

        intervals.sort(key=lambda i: i[1])

        ans = 1
        prev = intervals[0]

        for curr in intervals[1:]:
            # check if the previous interval does not overlap with the current one
            if prev[1] <= curr[0]:
                ans += 1
                prev = curr

        return n - ans
