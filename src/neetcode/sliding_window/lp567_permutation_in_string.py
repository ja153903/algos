from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        To check if s2 ontains a permutation of s1, we need to iterate
        over s2 and check if there are characters that belong to s1 with valid frequency
        """
        freq = Counter(s1)
        start = 0

        for end, ch in enumerate(s2):
            freq[ch] -= 1

            if self._is_all_zero(freq):
                return True

            while end - start + 1 >= len(s1):
                freq[s2[start]] += 1
                start += 1

        return False

    def _is_all_zero(self, freq: Counter) -> bool:
        for value in freq.values():
            if value != 0:
                return False
        return True
