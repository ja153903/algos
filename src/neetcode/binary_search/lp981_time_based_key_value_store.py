from collections import defaultdict, namedtuple

Time = namedtuple("Time", ["value", "timestamp"])


class TimeMap:
    def __init__(self) -> None:
        self._map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._map[key].append(Time(value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self._map:
            return ""

        times = self._map[key]

        # we want to do binary search to find the rightmost
        # value less then timestamp

        left, right = 0, len(times) - 1

        while left < right:
            # this will bias the mid so that we can get the rightmost value
            mid = left + (right - left + 1) // 2

            if times[mid].timestamp <= timestamp:
                left = mid
            else:
                right = mid - 1

        return times[left].value if times[left].timestamp <= timestamp else ""
