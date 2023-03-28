class Solution:
    def insert(
        self, intervals: list[list[int]], new_interval: list[int]
    ) -> list[list[int]]:
        if not intervals:
            return [new_interval]

        # if we're trying to insert an interval into an existing set of intervals
        # we should first iterate first until
        result = []

        # suppose that we have the following list of intervals:
        # [[1, 3], [6, 9]] and we want to insert [2, 5]
        i, n = 0, len(intervals)

        # add those intervals that are clearly less
        while i < n and intervals[i][1] < new_interval[0]:
            result.append(intervals[i])
            i += 1

        # NOTE: Take note of this part of the algorithm. This is the clever part.
        # update the interval we want to merge as we go along the list of intervals
        # this way we can just insert 1 interval
        while i < n and intervals[i][0] <= new_interval[1]:
            new_interval = [
                min(intervals[i][0], new_interval[0]),
                max(intervals[i][1], new_interval[1]),
            ]
            i += 1

        result.append(new_interval)

        # if there are any other intervals to take care of, do them here.
        while i < n:
            result.append(intervals[i])
            i += 1

        return result
