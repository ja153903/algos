from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        This problem is rather interesting

        The idea here is to keep track of the most frequency character
        since that will let us know how many characters we would need to replace
        in the existing window.

        For example, if we have the string: 'AABA', we know that the most frequent character
        thus far is 'A' with a frequency of 3 and if k = 1, then we know that we can only replace
        the 'B' with an 'A'. But now suppose that we have the substring 'AABAB', given that our
        maximum frequency is still 3 and k is 1, we know that our window is invalid because
        there are too many characters that would need to be replaced i.e. because we have 2 Bs
        we know that we can't replace all of them given that we only have 1 replacement.
        """
        freq = Counter()

        start = 0
        max_freq = 0
        ans = 0

        for end, char in enumerate(s):
            freq[char] += 1
            max_freq = max(max_freq, freq[char])

            while end - start + 1 - max_freq > k:
                freq[s[start]] -= 1
                start += 1

            ans = max(ans, end - start + 1)

        return ans
