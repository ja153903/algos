from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        This problem exhibits very basic application
        of sliding window technique.
        """
        if len(t) > len(s):
            return ""

        min_start, min_length = 0, float("inf")
        start = 0

        counter = Counter(t)
        target = len(t)

        for end, char in enumerate(s):
            counter[char] -= 1
            if counter[char] >= 0:
                target -= 1

            while target == 0:
                current_window_size = end - start + 1
                if current_window_size < min_length:
                    min_length = current_window_size
                    min_start = start

                counter[s[start]] += 1
                if counter[s[start]] > 0:
                    target += 1

                start += 1

        if min_length == float("inf"):
            return ""

        return s[min_start : min_start + min_length]
